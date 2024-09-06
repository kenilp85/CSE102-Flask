from sqlalchemy import create_engine
from sqlalchemy import text
engine = create_engine("sqlite:///student.db", echo=True)

while(True):
    c = int(input("Enter Your Choice: \n1. Insert \n2. Delete \n3. Update \n4. View\n5. Exit\n"))
    # print(c)

    if(c == 1):
        print("performing Insert Operation")
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        with engine.connect() as conn:
            conn.execute(text("insert into student_details(id, name) values ("+str(id)+",'"+ name +"')"))
            conn.commit()

    elif(c == 2):
        print("Performimg delete operation")
        id = int(input("Enter ID: "))
        with engine.connect() as conn:
            conn.execute(text("delete from student_details where id="+str(id)+""))
            conn.commit()

    elif(c == 3):
        print("Performing Update Operation")
        id = int(input("Enter Id "))
        name = input("Enter Nam ")
        with engine.connect() as conn:
            conn.execute(text("UPDATE student_details SET id='" + name + "' where id=" + str(id) + ""))
            conn.commit()

    elif(c == 4):
        print("Performing View Operation")
        with engine.connect() as conn:
            result = conn.execute(text("SELECT count(*) FROM student_details"))
            n=0
            for row in result:
                n = row[0]
                if(n == 0):
                    print("No Data Found")
                else:
                    print(""+ str(n) + " Data Found")
                    result1 = conn.execute(text("SELECT id,name FROM student_details"))
                    for row1 in result1:
                        print(f"Student No. : {row1.id} Name : {row1.name}")
    elif(c == 5):
        print("Thank for using terminal")
        break
    else:
        print("Wrong Choice")