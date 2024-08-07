from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello():
     return render_template('Index.html')

@app.route("/viewdata",methods=['GET', 'POST'])
def hello1():
    if request.method=='GET':
        fullname=request.args.get('fname')
        return render_template('Veiw-Data.html',fullname=fullname)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
