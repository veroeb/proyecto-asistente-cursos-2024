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
- [Codespell](https://github.com/codespell-project/codespell)
- [Flake8](https://flake8.pycqa.org/en/latest/)
- [Black](https://github.com/adamchainz/blacken-docs)
- [Isort](https://github.com/PyCQA/isort)
- pip install flake8 (aca se puede tirar el siguiente comando python -m flake8 flaskr/auth.py [cumple con el PEP-8 de Python])
- pip install black (para un archivo black flaskr/auth.py o para varios black flaskr/ y mirar siguiente pagina https://www.freecodecamp.org/espanol/news/como-autoformatear-tu-codigo-python-con-black/)
- pip install isort (isort flaskr/blog.py o python -m isort src/app.py --check-only)
- pip install pydocstyle
- Seguir investigando en https://seraph13.medium.com/desarrollar-c%C3%B3digo-python-limpio-con-pre-commit-6d760a39aa08

Si realizamos algun cambio en el archivo ``` .pre-commit-config.yaml ``` recordemos que debemos poner el siguiente comando
para actualizar ``` pre-commit autoupdate ```


Webgafia:
1. https://pre-commit.com/


