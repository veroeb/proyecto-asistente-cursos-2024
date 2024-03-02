# Proyecto Asistente Virtual para Cursos 2024


# prueba de registro
# user: admin, password: admin123

Para hacer el proyecto ejecutable debemos correr el siguiente comando:
pip install -e .

Si nos da un error del tipo:
Getting requirements to build editable ... error
  error: subprocess-exited-with-error
  ...
  error: Multiple top-level packages discovered in a flat-layout: ['flaskr', 'instance'].

Debemos eliminar la carpeta instance que se creo al correr el comando flask --app flaskr init-db


# Pasos para levantar el proyecto de forma local:

1- Abrir una terminal en el proyecto y ejecutar:
  pip install flask

2- Ingresar a la carpeta flaskr mediante el comando:
  cd flaskr

3- Si no tenemos la DB creada de forma local, ejecutar el siguiente comando:
  flask --app flaskr init-db

4- Finalmente, ejecutar el siguiente comando:
  flask --app __init__ run

  Se desplegar el proyecto en una URL local, donde podemos hacer llamadas a los correspondientes servicios.