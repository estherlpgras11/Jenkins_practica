# Código para frontend

Tenemos una aplicación web escrita en [vue](https://vuejs.org/v2/guide/) que consultará la api de backend. Para comenzar a usar la aplicación web necesitaremos instalar la última versión de [npm](https://www.npmjs.com/).

## Dependencias

Antes de nada, debemos instalar las dependencias necesarias para ejecutar nuestra aplicación web. Para ello, ejecutaremos el siguiente comando

``` bash
# install dependencies
npm install
```

## Linters

Podemos ejecutar los linters de vue con el siguiente comando:

``` bash
npm run lint
```

## Tests

Podemos ejecutar los tests unitarios, de integración, o ambos de la siguiente manera:

``` bash
# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

NOTA: para los tests de integración hace falta tener _chromedriver_ instalado en el path _/usr/local/bin/chromedriver_

## Servidor local

Para que el servidor local funcione, hace falta tener la API de backend levantada, si no las consultas serán vacías.

La manera de ejecutar el servidor en modo desarrollo es la siguiente:

``` bash
# serve with hot reload at localhost:8080
npm run dev
```

## Generar artefacto

Podemos generar tanto el contendo estático como la imagen de Docker a partir de nginx.

### Contenido estático

Si queremos subir nuestra web a un servidor web (o, por ejemplo, AWS S3) podemos construir nuestro sitio web con el siguiente comando:

``` bash
# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

### Contenido en contenedor de nginx

Existe un dockerfile en el repositorio para servir el contenido estático. Para ello puede generar una release con el siguiente comando:

`docker build --no-cache -t frontend-test:$(cat version) .`

## Publicar artefacto

Para publicar un artefacto en un repositorio de artefactos, cree un nuevo tag y suba el artefacto al repositorio (sustituya _nexus.url:port_ por su dirección de repositorio de artefactos):

```
docker tag frontend-test:$(cat version) nexus.url:port/frontend-test:$(cat version)
docker push nexus.url:port/frontend-test:$(cat version)
```
