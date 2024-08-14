from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
import os


app = Flask(__name__, template_folder='templates')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def hello():
     return render_template('index.html')

@app.route("/index")
def index():
     return render_template('index.html')

@app.route('/savedata', methods=['GET', 'POST'])
def savedata():
    if request.method == 'POST':
        filename = request.form.get('filename')
        filecontent = request.form.get('filecontent')
        filepath  = 'static/temp/' +filename+ '.txt'
        f = open(filepath, "a")
        f.write(filecontent)
        f.close()
        message = 'File is Created'
        return render_template('Display-Data.html', message=message,filepath=filepath)
    if request.method == 'GET':
        return render_template('get-is-not-supported.html')
    
@app.route('/listfiles')
def listfiles():
    entries = os.listdir('static/temp/')
    return render_template('List-Files.html', entries=entries)