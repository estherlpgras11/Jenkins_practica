pipeline {

  agent{
    label "mac"
  }

    options {
        timeout(time: 10, unit: 'MINUTES')
        timestamps() 
    }

  environment {
      DOCKER_REGISTRY = 'localhost:8082'
  }

  parameters {
      string(name: 'registryUrl', defaultValue: env.DOCKER_REGISTRY, description: 'Docker registry url')
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


    stage('Prepare') {
        steps {
            script{
              echo "unit test"
             }
           }
        }     


    stage('Unit test') {
        steps {
            script{
              echo "unit test"
              sh '. .env/bin/activate; behave integration/features'
                // sh '. .env/bin/activate; pyb -o run_unit_tests coverage'
            }
            // junit 'target/reports/TEST-*xml'
        }
    }



    stage('Package') {
        steps {
            script{
                echo "Package"
            }
        }
    }



/*
      stage('Verify') {
          steps {
              script{
                  sh '. .env/bin/activate; pyb -o verify'
              }
          }
      }
*/
  }

    stage('Upload') {
        steps {
            withCredentials([usernamePassword(credentialsId: 'nexus',
            usernameVariable: 'TWINE_USERNAME', passwordVariable: 'TWINE_PASSWORD')]) {
                sh '. .env/bin/activate; pyb -o upload'
                sh "docker login -u ${TWINE_USERNAME} -p ${TWINE_PASSWORD} ${params.registryUrl}"
                sh "docker tag acme_master_web:latest ${params.registryUrl}/acme_master_web:1.0"
                sh "docker push ${params.registryUrl}/acme_master_web:1.0"
            }
        }
    }

    post {

     always {
       sh 'echo "This will always run"'
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
              
     }
     unstable {
      sh 'echo "This will run only if the run was marked as unstable"'
     }
     changed {
      sh 'echo "This will run only if the state of the Pipeline has changed"'
     }
  }
  post {
    cleanup {
      cleanWs()
    }

  //   success {
  //     slackSend color: 'good', channel: 'ciclo-desarrollo-ci-cd', message: ":heavy_check_mark: Build [${BUILD_NUMBER}](${BUILD_URL}) passed"
  //     updateGitlabCommitStatus state: 'success'
  //     script {
  //       if (env.GIT_BRANCH == 'master') {
  //         slackSend color: 'good', channel: 'ciclo-desarrollo-ci-cd', message: "Version ${version} uploaded successfully to nexus"
  //       }
  //     }

  //     publishHTML (target: [
  //       allowMissing: false,
  //       alwaysLinkToLastBuild: false,
  //       keepAll: true,
  //       reportDir: 'target/reports/cicd_coverage_html',
  //       reportFiles: 'index.html',
  //       reportName: 'Coverage' 
  //     ])
  //   }

  //   unstable {
  //     slackSend color: 'warning', channel: 'ciclo-desarrollo-ci-cd', message: ":warning: Build [${BUILD_NUMBER}](${BUILD_URL}) failed tests"
  //     updateGitlabCommitStatus state: 'failed'
  //   }

  //   failure {
  //     slackSend color: 'danger', channel: 'ciclo-desarrollo-ci-cd', message: ":x: Build [${BUILD_NUMBER}](${BUILD_URL}console) failed"
  //     updateGitlabCommitStatus state: 'failed'
  //   }
  // }
}
