# Práctica final CI/CD

He realizado esta práctica en **local** utilizando imágenes docker de **Jenkins** y **Nexus**.
: 
- Pipeline para testear el frontend
- Pipeline para testear el backend
- Pipeline para pasar los test de integración

## Configuración en Jenkins

* Crear las credenciales de **Nexus** y **Gitlab**:
![credentials](screenshots/credentials.jpg?raw=true "")

* Crear una **pipeline multibranch** añadiendo la url del repositorio de Gitlab y especificando que use las credenciales creadas para Gitlab en el paso anterior.
![pipeline](screenshots/acme_pipeline.jpg?raw=true "")

* Crear un agent llamado "mac".
![agent](screenshots/agent_slave.jpg?raw=true "")

* Dar permiso a mi repositorio local para que al hacer el build Jenkins pueda descargarse las imagenes de docker:
``` bash
sudo chmod 777 /usr/local/bin/docker
sudo chmod 777 /var/run/docker.sock
```

* Instalar el plugin **Chromedriver** en Jenkins para que lo instale en todos los agentes
![chromedriver](screenshots/chromedriver.jpg?raw=true "")

* Realizamos la integración de Jenkins con nuestra cuenta de email para que pueda enviarnos notificaciones:
![gmail1](screenshots/gmail.jpg?raw=true "")
![gmail2](screenshots/gmail2.jpg?raw=true "")
