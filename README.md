# Proyecto Asistente Virtual para Cursos 2024

Para hacer el proyecto ejecutable debemos correr el siguiente comando:
pip install -e .

Si nos da un error del tipo:
Getting requirements to build editable ... error
  error: subprocess-exited-with-error
  ...
  error: Multiple top-level packages discovered in a flat-layout: ['flaskr', 'instance'].

Debemos eliminar la carpeta instance que se creo al correr el comando flask --app flaskr init-db


# Pasos para levantar el proyecto de forma local:

1- Verificar que al ejecutar el comando `flask --version` obtengamos algo similar a la siguiente respuesta:
  ```
  Python 3.12.1 
  Flask 3.0.2   
  Werkzeug 3.0.1
  ```
  
  En caso de no obtener esta respuesta, ejecutar `pip install flask`

2- Si no tenemos la DB creada de forma local, ejecutar el siguiente comando:
  `flask --app flaskr init-db`

3- Ingresar a la carpeta flaskr mediante el comando:
  `cd flaskr`

4- Finalmente, ejecutar el siguiente comando:
  `flask --app __init__ run`

  Se desplegar el proyecto en una URL local, donde podemos hacer llamadas a los correspondientes servicios.

# Pruebas
Para poder probar correctamente, primero debes registrarte y luego ingresar desde la pantalla de login.