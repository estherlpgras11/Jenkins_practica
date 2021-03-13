# Infrastructura necesaria para la ejecución de las prácticas

A continuación se detalla la infrastructura mínima para la ejecución de las prácticas

## Docker

Instalar la última versión disponible en su sistema operativo. En caso de tener que usar una IP local en vez de localhost (por ejemplo, cuando se usa máquina virtual para Docker), hay que cambiar los puertos de la parte de integración por la IP de dicha máquina. 

## Jenkins

Ver el repositorio [simple-jenkins](https://gitlab.keepcoding.io/cgarciaarano/simple-jenkins) para más información

## Opcionales

Se pueden instalar las herramientas si se desea ir más allá en la ejecución de la práctica. Las instrucciones son las siguientes:

 1. Existe un `docker-compose.yml` en este directorio con los siguientes componentes (NOTA: los tres componentes a la vez consumen bastantes recursos. Si no dispone de un equipo potente, con el servidor de Jenkins de la sección anterior es suficiente)::
   * Jenkins
   * Nexus
   * Gitlab CE
 2. Las instrucciones de configuración se encuentra [aquí](INSTALLATION.md)


### Nexus

Con Nexus tendremos un servidor de artefactos para poder versionar y descargar los diferentes componentes de nuestra práctica.

Seguir los pasos de [instalación](https://blog.sonatype.com/sonatype-nexus-installation-using-docker).

Para configurar *Nexus* como servidor de artefactos, seguir las instrucciones descritas [aquí](https://blog.sonatype.com/using-nexus-3-as-your-repository-part-3-docker-images).

### Gitlab

Instalaremos Gitlab en local para poder gestionar los _hooks_ que enviarán la información a nuestro servidor de Jenkins.

Para configurar *Gitlab CE* como gestor de control de versiones en docker siga las instrucciones descritas [aquí](https://docs.gitlab.com/omnibus/docker/)

## Bonus - Kubernetes

Si quiere probar algo mas "hardcore", se puede adaptar toda la práctica para Kubernetes (aunque queda fuera del ámbito de este tema). Si quiere realizar una prueba en local, se recomienda [Kubernetes in Docker](https://kubernetes.io/docs/setup/learning-environment/kind/)para la ejecución opcional en local. Otras opciones son aceptables tanto en local como en remoto. 


