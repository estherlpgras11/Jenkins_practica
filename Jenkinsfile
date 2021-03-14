pipeline {

  agent{
    label "mac"
  }

    triggers {
          pollSCM('') 
      }

    options {
        timeout(time: 10, unit: 'MINUTES')
        timestamps() 
    }
    environment {
          DOCKER_REGISTRY = 'localhost:8082'
      }

    parameters {
          string(name: 'registryUrl', defaultValue: 'localhost:8082', description: 'Docker registry url')
      }

  stages {

        stage("Install dependencies") {
          steps {
            sh """
            virtualenv .env
            . .env/bin/activate
            pip install -r integration/requirements.txt
            """
          }
        }
 
        stage('Build') {
          steps {
            // sh '/usr/local/bin/docker-compose up --build'
            sh "docker-compose build"
            sh "docker-compose up -d"
          }
        }

        stage('Unit test') {
            steps {
                script{
                  echo "unit test"
                  sh '. .env/bin/activate; behave integration/features --junit'
                }
  
            }            
        }


        stage('Building image') {
              steps{
                script {
                  version = readFile('__VERSION__').trim()
                }
                  sh "docker build --no-cache -t acme:${version} ./frontend "
              }
            }

        stage('Upload') {
              steps {
                script {
                   version = readFile('__VERSION__').trim()
                }
                withCredentials([usernamePassword(credentialsId: 'nexus', usernameVariable: 'TWINE_USERNAME', passwordVariable: 'TWINE_PASSWORD')]) {
                    sh "docker login -u ${TWINE_USERNAME} -p ${TWINE_PASSWORD} ${params.registryUrl}"
                    sh "docker tag acme:${version} ${params.registryUrl}/acme:${version}"
                    sh "docker push ${params.registryUrl}/acme:${version}"
                }
              }
              
        }

        stage('Stop') {
          steps {
            echo "STOP"
            sh "docker-compose stop"
            sh "docker-compose rm -f"
          }
        }
  }

    post {

     always {
       sh 'echo "This will always run"'
       junit 'reports/*.xml'
      }
      cleanup {
      cleanWs()
    }

     success {
      sh 'echo "This will run only if successful"'
              script {
                    if (currentBuild.currentResult == 'SUCCESS') { // Other values: SUCCESS, UNSTABLE, FAILURE
                        // Send an email only if the build status has changed from green/unstable to red
                        emailext subject: '$DEFAULT_SUBJECT',
                            body: '$DEFAULT_CONTENT',
                            recipientProviders: [
                                [$class: 'CulpritsRecipientProvider'],
                                [$class: 'DevelopersRecipientProvider'],
                                [$class: 'RequesterRecipientProvider']
                            ], 
                            replyTo: '$DEFAULT_REPLYTO',
                            to: '$DEFAULT_RECIPIENTS'
                    }
                }
     }
     failure {
      sh 'echo "This will run only if failed"'
      sh 'echo "This will run only if successful"'
              script {
                    if (currentBuild.currentResult == 'SUCCESS') { // Other values: SUCCESS, UNSTABLE, FAILURE
                        // Send an email only if the build status has changed from green/unstable to red
                        emailext subject: '$DEFAULT_SUBJECT',
                            body: '$DEFAULT_CONTENT',
                            recipientProviders: [
                                [$class: 'CulpritsRecipientProvider'],
                                [$class: 'DevelopersRecipientProvider'],
                                [$class: 'RequesterRecipientProvider']
                            ], 
                            replyTo: '$DEFAULT_REPLYTO',
                            to: '$DEFAULT_RECIPIENTS'
                    }
                }
              
     }
     unstable {
      sh 'echo "This will run only if the run was marked as unstable"'
     }
     changed {
      sh 'echo "This will run only if the state of the Pipeline has changed"'
     }
  }

}

