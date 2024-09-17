import configparser

import openai
from flask import Blueprint, flash, jsonify, request
from openai import OpenAI

from flaskr.db import get_db

bp = Blueprint("task", __name__, url_prefix="/task")  # Creates a blueprint named 'task'

config = configparser.ConfigParser()
config.read("../config.ini")
openai.api_key = config["openai"]["api_key"]


@bp.route("/correction", methods=["POST"])
def text_CU():
    data = request.json
    task = data.get("task")
    rubric = data.get("rubric")
    if not task:
        return jsonify({"error": "The task text is required."}), 400
    if not rubric:
        return jsonify({"error": "The rubric is required."}), 400

    try:

        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": rubric},
                {"role": "user", "content": task},
            ],
            temperature=0.1,
            stream=False,
        )
        if response.choices:
            assistant_message = response.choices[0].message.content
            return jsonify({"correction": assistant_message})
        else:
            return jsonify({"error": "Failed to get a response from the OpenAI API."}), 500
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

        flash(error)

    return True
