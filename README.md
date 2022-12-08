![Logo Henry](_src/logo-henry-white-lg.png)

# PI01-DTS05 DATA ENGINEERING

---

## Introducción

Este es el primer proyecto individual de la cohorte 5 de la carrera de data sciense en Henry. El mismo consiste en la realización de una API que permita hacer una serie de consultas sobre

---

## Estructura

Inicialmente se realiza un proceso de ETL con `Python` y los datos se cargan en una base de datos `SQLite`, luego la API creada con el framework de `FastAPI` se comunica con la base de datos y realiza las consultas necesarias.

![Diagrama](_src/Diagrama%20en%20blanco.png)

---

## Instalación

El primer paso es clonar el repositorio, puede hacerlo con el comando:

```cmd
git clone https://github.com/agusdm97/PI01-DTS05.git
```

Luego tiene que decidir si va a utilizar `Docker` o no.

### Con docker (recomendado)

Para construir la imagen ejecute el siguiente comando:

```cmd
docker build -t myimage .
```

Luego, para correr el contenedor ejecute el siguiente comando:

```cmd
docker run -d --name mycontainer -p 80:80 myimage
```

Listo, ahora puede entrar a la aplicación mediante el siguiente enlace:

[Link a la aplicación](http://localhost:80/docs)

### Sin docker

Cree un entorno virtual de `python3.10.5`, activelo y luego instale las dependencias ubicadas en el archivo requirements.txt con el siguiente comando:

```cmd
pip install -r requirements.txt
```

Dirijase a la carpeta app mediante el siguiente comando:

```cmd
cd app
```

Por ultimo, ejecute el siguiente comando:

```cmd
uvicorn main:app --reload
```

Listo, ahora puede entrar a la aplicación mediante el siguiente enlace:

[Link a la aplicación](http://localhost:8000/docs)
