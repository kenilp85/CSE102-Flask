from flask import Flask 
from flask import render_template

app = Flask(__name__, template_folder='template')

@app.route('/')
def listfiles():
    studentdata = [[1,"vraj","Ahmedabad"],[2,"Dev", "Vadodara"],[3,"Dhruvit","Jamnagar"]]
# The below portion will provide output in the terminal this is to demonstrate another way to implement list read
    for x in studentdata:
        for y in x:
            print(y)  

    return render_template('View-Data.html', studentdata = studentdata) 