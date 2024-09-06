from flask import Flask
from flask import render_template
from sqlalchemy import create_engine
from sqlalchemy import text
engine = create_engine("sqlite:///student.db", echo=True)



app = Flask(__name__, template_folder='templates')
    
@app.route('/')
def listfiles():
        studentdata = []
        with engine.connect() as conn:
            result = conn.execute(text("SELECT count(*) FROM student_details"))
            n = 0
            result1 = conn.execute(text("SELECT id, name FROM student_details"))
            for row in result1:
                    n += 1
                    studentdata.append(row)
    # n = len(studentdata) -1
        return render_template('View-Data.html', studentdata=studentdata,n=n)

# with engine.connect() as conn:
#             result = conn.execute(text("SELECT count(*) FROM student_details"))
#             n=0
#             for row in result:
#                 n = row[0]
#                 if(n == 0):
#                     print("No Data Found")
#                 else:
#                     print(""+ str(n) + " Data Found")
#                     result1 = conn.execute(text("SELECT id,name FROM student_details"))
#                     for row1 in result1:
#                         print(f"Student No. : {row1.id} Name : {row1.name}")