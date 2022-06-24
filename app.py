 
from fileinput import filename
from unicodedata import name
from flask import Flask, redirect, render_template, request, send_from_directory, url_for
from helpers import detect_obj
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
import psycopg2

hostname = 'localhost'
database = 'cs50-final-project'
username = 'marikhomeriki'
pwd = 'admin'
port_id = 5432

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SECRET_KEY"] = 'supersecretkey'
app.config["UPLOAD_FOLDER"] = 'static/files'


conn = psycopg2.connect(
  host = hostname,
  dbname = database,
  user = username,
  password = pwd,
  port = port_id
  )
cur = conn.cursor()


class UploadFileForm(FlaskForm):
 file = FileField("File")
 submit = SubmitField("Upload File")



@app.route("/", methods=["GET", "POST"])
@app.route("/page.html", methods=["GET", "POST"])
def hello():
 form = UploadFileForm()
 
 if form.validate_on_submit():
   file = form.file.data
   file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
   name = file.filename
   url = 'static/files/'+name
   labels=detect_obj(url)
   q=detect_obj(url)
   labels = ', '.join(labels)
   quantity = len(q)
   insert_script = 'INSERT INTO photos (id, quantity, url, objects) VALUES (DEFAULT, %s, %s, %s)'
   insert_value = (quantity, url, labels)
   cur.execute(insert_script, insert_value)
   conn.commit()
   return render_template("upload.html", form=form, obj=labels, name=name, url=url)
 return render_template("upload.html", form=form)



@app.route("/display/<filename>")
def display_image(filename):
    return redirect(url_for('static', filename='files/'+filename), code=301)


@app.route("/index.html")
def index():
  cur.execute("SELECT id, quantity, url, objects FROM public.photos;")
  rows = cur.fetchall()
  return render_template("index.html", rows=rows)

if __name__ == '__app__':
    app.run(debug=True)
