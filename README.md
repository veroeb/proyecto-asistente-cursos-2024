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

# 🔨  Herramientas utilizadas en proyecto 🔨
## Calidad de código

### Pre-Commit
Git hook scripts are useful for identifying simple issues before submission to code review. [1]
Los Hooks que utilizaremos para poder identificar y tener una revision de codigo durante los commits.
Para ello deberemos utilizar el siguiente comando de installacion de pre-commit: ``` pip install pre-commit ```
Esto sera suficiente para que al momento que cualquier desarrollador intente hacer un commit se ejecute el
archivo ``` .pre-commit-config.yaml ```
En este archivo se encuentran algunos complementos como:
- [Flake8](https://flake8.pycqa.org/en/latest/)

Si realizamos algun cambio en el archivo ``` .pre-commit-config.yaml ``` recordemos que debemos poner el siguiente comando
para actualizar ``` pre-commit autoupdate ```


Webgafia:
1. https://pre-commit.com/
