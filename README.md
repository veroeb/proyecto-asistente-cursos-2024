# Proyecto Asistente Virtual para Cursos 2024

# 👣 Steps to Set Up the Project Locally 👣

1- Verify that running the command flask --version yields a response similar to the following::
  ```
  Python 3.12.1
  Flask 3.0.2
  Werkzeug 3.0.1
  ```

  If this response is not obtained, run
  ```
  pip install flask
  ```
2- If the local database is not created, execute the following command:
  ```
  flask --app flaskr init-db
  ```

3- Navigate to the flaskr folder using the command:
  ```
  cd flaskr
  ```

4- Finally, execute the following command:
  ```
  flask --app __init__ run
  ```

The project will be deployed to a local URL, allowing us to make calls to the corresponding services.

## Testing
To test properly, you must first register and then log in from the login screen.

# 🔨 Tools Used in the Project 🔨
## Configuration of pyCharm IDE
1. Configure the Python interpreter:
   Navigate to File -> Settings -> Project -> Python interpreter -> Add interpreter ->
   Add local interpreter -> System Interpreter, and select  ``` Pyhton 3.9 ```.
2. Configure Code Quality: Go to File -> Settings -> Editor -> Code Style -> Python:
   1. Tabs and Indents:
      - Tab size: 2
      - Indent: 2
      - Continuation indent: 4
   2. Wrapping and Braces
      - Hard wrap at: 89


# 🎯 Code Quality 🎯
### Pre-Commit
Git hook scripts are useful for identifying simple issues before submission to code
review. [1] The hooks we will use to identify and review code during commits. To achieve
this, we should use the following pre-commit installation command: `pip install
pre-commit`. This will be sufficient so that whenever any developer tries to make a
commit, the file `.pre-commit-config.yaml` is executed. In this file, there are some
additional plugins such as:
- [Flake8](https://flake8.pycqa.org/en/latest/)

If we make any changes to the `.pre-commit-config.yaml` file, remember to execute the
following command to update: `pre-commit autoupdate` and `pre-commit run --all-files`


Webgafia:
1. https://pre-commit.com/


# 📝Testing the Text Correction Endpoint 📝
## watch the following video on YouTube for demo:
[View Test Demonstration](https://youtu.be/KHVTzukxFfw)

1- Navigate to the flaskr folder using the command:
  ```
  cd flaskr
  ```

2- Execute the following command to run the development server:
  ```
  flask --app __init__ run
  ```
3- On Windows:
Open Command Prompt: Press Win + R, type cmd, and hit Enter.
Send a POST Request: Copy and paste the following curl command into your Command Prompt. This command sends a task to the correction endpoint, along with a custom rubric for evaluation.
  ```
curl -X POST "http://localhost:5000/task/correction" -H "Content-Type: application/json" -d "{\"task\": \"Las palabras graves, también conocidas como palabras llanas, son aquellas en las que la sílaba tónica es la penúltima. Un ejemplo de palabra grave es árbol, donde la sílaba ár es la que lleva la mayor fuerza de voz. A diferencia de las palabras agudas, las graves no llevan tilde excepto cuando terminan en consonante que no sea n, s o vocal.\", \"rubric\": \"Eres un profesor de educación intermedia. Debes corregir la tarea que te pasa el alumno en una escala de 0 a 100 donde 60 es el mínimo de aprobación. Debes ser muy exigente con la nota, Además de la nota debes darle un concepto a la tarea. La respuesta esperada debe ser una nota y luego un comentario con observaciones. \"}"
  ```
