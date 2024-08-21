from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/savedata', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        temp = 'static/temp/' + str(secure_filename(f.filename))
        f.save(temp)
        return 'file uploaded successfully'

@app.route('/listfiles')
def listfiles():
    entries = os.listdir('static/temp/')
    return render_template('List-Files.html', entries=entries)