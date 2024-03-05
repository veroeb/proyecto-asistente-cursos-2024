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

# 🔨  Herramientas utilizadas en proyecto 🔨
## Configuracion de IDE pyCharm
1. Configurar el interpreter de Python: Dirigirse a File->Settings->Project->Python
   interpreter -> Add interpreter -> Add local interpreter -> System Interpreter y
   seleccionamos ``` Pyhton 3.9 ```.
2. Configurar Code Quality : File -> Settings -> Editor -> Code Style -> Python:
   1. Tabs and Indents:
      - Tab size: 2
      - Indent: 2
      - Continuation indent: 4
   2. Wrapping and Braces
      - Hard wrap at: 89


## Calidad de código

### Pre-Commit
Git hook scripts are useful for identifying simple issues before submission to code review. [1]
Los Hooks que utilizaremos para poder identificar y tener una revision de codigo durante los commits.
Para ello deberemos utilizar el siguiente comando de installacion de pre-commit: ``` pip install pre-commit ```
Esto sera suficiente para que al momento que cualquier desarrollador intente hacer un commit se ejecute el
archivo ``` .pre-commit-config.yaml ```
En este archivo se encuentran algunos complementos adicionales como:
- [Flake8](https://flake8.pycqa.org/en/latest/)

Si realizamos algun cambio en el archivo ``` .pre-commit-config.yaml ``` recordemos que debemos poner el siguiente comando
para actualizar ``` pre-commit autoupdate ``` y ``` pre-commit run --all-files ```


Webgafia:
1. https://pre-commit.com/
