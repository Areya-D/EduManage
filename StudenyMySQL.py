import mysql.connector

myDB = mysql.connector.connect(
    host = "localhost",
    user = "root", 
    passwd = "root113", 
    database = "studentdb"
)
myCursor = myDB.cursor()

##database manipulation methods
def addStu():
    info = ["Last name: ", "First name: ", "Major: ", "Classification: ", "ID: "]
    iType = []
    print("Please enter the students' information")
    for i in (info):
        j = input(i)
        iType.append(j)
       
    sqlFormula = "INSERT INTO students (lname, fname, major, class, ID) VALUES(%s, %s, %s, %s, %s)" 
    student = (iType[0], iType[1], iType[2], iType[3], iType[4])
    
    myCursor.execute(sqlFormula, student)
    myDB.commit()

def searchStu():
    ID = input("Type the students' ID: ")
    sqlFormula = "SELECT * FROM students WHERE ID = %s"
    
    myCursor.execute(sqlFormula, (ID,))
    result = myCursor.fetchall()
    
    for row in result:
        print(row)

def removeStu(): 
    ID = input("Type the students' ID: ")
    sqlFormula = "DELETE FROM students WHERE ID = %s"
    myCursor.execute(sqlFormula, (ID,))
    myDB.commit()

def editStu(option):
    ID = input("Type the students' ID: ")    
    if option == 1:
        fname = input("Type new first name here: ")
        sqlFormula = "UPDATES students SET fname = %s WHERE ID = %s"
        myCursor.execute(sqlFormula, (fname,ID,))
        myDB.commit()
    elif option == 2:
        lname = input("Type new last name here: ")
        sqlFormula = "UPDATES students SET lname = %s WHERE ID = %s"
        myCursor.execute(sqlFormula, (lname,ID,))
        myDB.commit()
    elif option == 3:
        major = input("Type new major here: ")
        sqlFormula = "UPDATES students SET major = %s WHERE ID = %s"
        myCursor.execute(sqlFormula, (major,ID,))
        myDB.commit()
    elif option == 4:
        year = input("Type new classification here: ")
        sqlFormula = "UPDATES students SET class = %s WHERE ID = %s"
        myCursor.execute(sqlFormula, (year,ID,))
        myDB.commit()
    elif option == 5:
        newID = input("Type new ID here: ")
        sqlFormula = "UPDATES students SET ID = %s WHERE ID = %s"
        myCursor.execute(sqlFormula, (newID,ID,))
        myDB.commit()


##function for printing menu 
def menu():
    print("1. Add student to database")
    print("2. Search student in database")
    print("3. Remove student from database")
    print("4. Edit student information")
    


print("Welcome to EduManage!")
menu()
choice = int(input("Please Select One of the Options From the Menu: "))
if choice == 1:
    addStu()
elif choice == 2:
    searchStu()
elif choice == 3:
    removeStu()
elif choice == 4:
    option = input("Which of the following do you want to update:\n 1. First Name\n 2. Last Name\n 3. Major\n 4. Class\n 5. ID\n")
    editStu(option)