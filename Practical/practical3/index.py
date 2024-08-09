from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello():
     return render_template('index.html')

@app.route("/verify",methods=['GET', 'POST'])
def hello1():
    if request.method=='POST':
        fullname = request.form.get('nm')
        age = request.form.get('age')
        return render_template('verify.html',fullname=fullname, age=int(age))