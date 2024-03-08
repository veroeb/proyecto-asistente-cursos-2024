import openai
from flask import Blueprint, flash, request, jsonify
import os
from openai import OpenAI
from flaskr.db import get_db

bp = Blueprint("task", __name__, url_prefix="/task")  # Creates a blueprint named 'task'
openai.api_key = os.getenv("OPENAI_API_KEY")


# Rúbrica predeterminada
#predeterminada = "Eres un profesor de un curso de educación intermedia y debes corregir una tarea que te va a pasar el usuario en una escala de 0 a 100 donde 60 es el mínimo de aprobación. Además de la nota debes darle un concepto a la tarea."
@bp.route("/correction", methods=["POST"])
def text_CU():
    data = request.json
    tarea = data.get("tarea")
    rubrica= data.get("rubrica")
    #rubrica = data.get('rubrica', predeterminada)  # Usa rúbrica proporcionada o la predeterminada
    if not tarea:
        return jsonify({"error": "El texto de la tarea es requerido."}), 400
    if not rubrica:
        return jsonify({"error": "La rúbrica es requerida."}), 400

    try:
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": rubrica},
                {"role": "user", "content": tarea},
            ],
            temperature=0.1,
            stream=False,
        )
        if response.choices:
            assistant_message = response.choices[0].message.content  # segun documentaicon
            return jsonify({"corrección": assistant_message})
        else:
            return jsonify({"error": "No se pudo obtener una respuesta de la API de OpenAI."}), 500
    except openai.error.OpenAIError as e:
        return jsonify({"error": str(e)}), 500






@bp.route("/text", methods=["GET"])
def text_correction():
    if request.method == "GET":
        text = request.form["text"]
        task_request = request.form["taskRequest"]
        db = get_db()
        error = None

        if not text:
            error = "Username is required."
        elif not task_request:
            error = "Password is required."

        if error is None:
            try:  # text processing logic
                return True
            except db.IntegrityError:
                error = "Some errors happened during task processing. {}"
            else:
                return True

        flash(error)

    return True
