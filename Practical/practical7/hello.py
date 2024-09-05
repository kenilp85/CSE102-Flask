from flask import Flask
from flask import render_template
import csv

app = Flask(__name__, template_folder='template')
    
@app.route('/')
def listfiles():
    with open('Data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        studentdata = []
        for row in csv_reader:
            studentdata.append(row)
    n = len(studentdata) -1
    return render_template('View-Data.html', studentdata=studentdata,n=n)
    
