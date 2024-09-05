from sqlalchemy import create_engine
from sqlalchemy import text
engine = create_engine("sqlite:///student.db", echo=True)

c = int(input("Enter Your Choice: \n1. Insert \n2. Delete \n3. Update \n4. View\n"))
print(c)

if(c == 1):
    print("performing Insert Operation")
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    with engine.connect() as conn:
        conn.execute(text("insert into student_details(id, name) values ("+str(id)+",'"+ name +"')"))
        conn.commit()