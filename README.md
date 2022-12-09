![Logo Henry](_src/logo-henry-white-lg.png)

# PI01-DTS05 DATA ENGINEERING

## Introducción

En el marco del primer proyecto individual de la carrera de Data Science en Henry se solicito a los alumnos la creación de una `API` que responda consultas sobre los datos provistos. Estos datos originalmete provienen de diversas fuentes y requieren un proceso de `ETL` para poder se consultados desde una `Base de datos`.

## Estructura

Inicialmente se realiza un proceso de ETL con `Python` y los datos se cargan en una base de datos `SQLite`, luego la API creada con el framework de `FastAPI` se comunica con la base de datos y realiza las consultas necesarias.

![Diagrama](_src/Diagrama%20en%20blanco.png)

## Instalación

El primer paso es clonar el repositorio, puede hacerse utilizando el comando:

```cmd
git clone https://github.com/agusdm97/PI01-DTS05.git
```

Luego se decide la utilización o no de `Docker`.

### Con docker (recomendado)

Para construir la imagen se ejecuta el siguiente comando:

```cmd
docker build -t myimage .
```

Para correr el contenedor se ejecuta el siguiente comando:

```cmd
docker run -d --name mycontainer -p 80:80 myimage
```

Finalizados estos pasos, se accede a la aplicación mediante el siguiente enlace:

[Link a la aplicación](http://localhost:80/docs)

### Sin docker

Se requiere de la creación y activación de un entorno virtual de `python3.10.5`; luego, de la instalación de las dependencias ubicadas en el archivo requirements.txt con el siguiente comando:

```cmd
pip install -r requirements.txt
```

Dirigirse a la carpeta `app` mediante el siguiente comando:

```cmd
cd app
```

Por ultimo, se ejecuta el siguiente comando:

```cmd
uvicorn main:app --reload
```

Finalizados estos pasos se accede a la aplicación mediante el siguiente enlace:

[Link a la aplicación](http://localhost:8000/docs)
