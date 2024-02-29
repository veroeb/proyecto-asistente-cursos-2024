from flask import (
  Blueprint, flash, g, redirect, render_template, request, url_for, jsonify, send_file
)
from werkzeug.exceptions import abort
import requests
import os
import pandas as pd
import whisper
import m3u8
import subprocess
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
  db = get_db()
  posts = db.execute(
      'SELECT p.id, title, body, created, author_id, username'
      ' FROM post p JOIN user u ON p.author_id = u.id'
      ' ORDER BY created DESC'
  ).fetchall()
  return render_template('blog/index.html', posts=posts)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
  if request.method == 'POST':
    title = request.form['title']
    body = request.form['body']
    error = None

    if not title:
      error = 'Title is required.'

    if error is not None:
      flash(error)
    else:
      db = get_db()
      db.execute(
          'INSERT INTO post (title, body, author_id)'
          ' VALUES (?, ?, ?)',
          (title, body, g.user['id'])
      )
      db.commit()
      return redirect(url_for('blog.index'))

  return render_template('blog/create.html')

def downloadVideo2(url_video):
  responseURL = requests.get(url_video)
  m3u8_master = m3u8.loads(responseURL.text)
  print('playlist: ', m3u8_master.data['playlists'])
  playlist_url = m3u8_master.data['playlists'][0]['uri']
  responseURL = requests.get(playlist_url)
  playlist = m3u8.loads(responseURL.text)
  responseURL = requests.get(playlist.data['segments'][0]['uri'])
  with open('vid1.ts', 'wb') as archivo:
    for segment in playlist.data['segments']:
      url = segment['uri']
      responseURL = requests.get(url)
      archivo.write(responseURL.content)
  subprocess.run(['ffmpeg', '-i', 'vid1.ts', 'vid1.mp4'])


def downloadVideo(url_video):
  # Realizar una solicitud GET para descargar el video
  responseURL = requests.get(url_video, stream=True)

  if responseURL.status_code == 200:
    # Guardar el video en un archivo temporal
    temporal_directory = os.path.join(os.getcwd(), 'temp')
    os.makedirs(temporal_directory, exist_ok=True)
    temporal_file = os.path.join(temporal_directory, 'video_temp.mp4')

    with open(temporal_file, 'wb') as archivo:
      for fragment in responseURL.iter_content(chunk_size=256):
        archivo.write(fragment)

    return temporal_file
  else:
    return None


def transcribeVideo(file_path):
  # Obtener la ruta absoluta del archivo
  absolute_path = os.path.abspath(file_path)

  # Cargar el modelo Whisper
  model = whisper.load_model("medium")

  # Imprimir la ruta para verificar
  print("path: ", absolute_path)

  # Transcribir el video
  result = model.transcribe(absolute_path)

  var1 = pd.DataFrame(result['segments'])
  var1.to_csv('archivo1.csv', index=False)
  var = pd.DataFrame(result['segments'])['id', 'start', 'end', 'text']
  var.to_csv('archivo2.csv', index=False)

def verificar_existencia_archivo(ruta):
  return os.path.isfile(ruta)
@bp.route('/transcribeVideo', methods=['POST'])
def initializeTranscribeVideo():
  # Obtener la URL del video desde el cuerpo de la solicitud
  body = request.get_json()

  if not body or 'url' not in body:
    return jsonify(
        {'error': 'Se requiere la URL del video en el cuerpo de la solicitud'}), 400

  url_video = body['url']

  # Descargar el video
  # archivo_temporal = downloadVideo(url_video)

  if verificar_existencia_archivo('temp/video_temp.mp4'):
    print("Archivo existe")
    transcribeVideo("temp/video_temp.mp4")
  else:
    return jsonify({'error': f'Error al descargar el video desde {url_video}'}), 500


def get_post(id, check_author=True):
  post = get_db().execute(
      'SELECT p.id, title, body, created, author_id, username'
      ' FROM post p JOIN user u ON p.author_id = u.id'
      ' WHERE p.id = ?',
      (id,)
  ).fetchone()

  if post is None:
    abort(404, f"Post id {id} doesn't exist.")

  if check_author and post['author_id'] != g.user['id']:
    abort(403)

  return post


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
  post = get_post(id)

  if request.method == 'POST':
    title = request.form['title']
    body = request.form['body']
    error = None

    if not title:
      error = 'Title is required.'

    if error is not None:
      flash(error)
    else:
      db = get_db()
      db.execute(
          'UPDATE post SET title = ?, body = ?'
          ' WHERE id = ?',
          (title, body, id)
      )
      db.commit()
      return redirect(url_for('blog.index'))

  return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
  get_post(id)
  db = get_db()
  db.execute('DELETE FROM post WHERE id = ?', (id,))
  db.commit()
  return redirect(url_for('blog.index'))
