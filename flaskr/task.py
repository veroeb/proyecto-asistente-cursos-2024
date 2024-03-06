import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('task', __name__, url_prefix='/task')  ## Creates a blueprint named 'task'


@bp.route('/text', methods=['GET'])
def text_correction():
    if request.method == 'GET':
        text = request.form['text']
        task_request = request.form['taskRequest']
        db = get_db()
        error = None

        if not text:
            error = 'Username is required.'
        elif not task_request:
            error = 'Password is required.'

        if error is None:
            try:#text processing logic
                return True
            except db.IntegrityError:
                error = f"Some errors happened during task processing."
            else:
                return True

        flash(error)

    return True
