from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/index", methods=['GET', 'POST'])
def hello1():
   if request.method == 'POST':
     Fname = request.form.get('fname')
     Lname = request.form.get('lname')
     return render_template('index.html', Fname=Fname, Lname=Lname)
@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')

@app.route("/contactus")
def contactus():
    return render_template('contactus.html')