
import json
def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []

def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
#ADD student
def studentAdd():
  roll=int(input("Enter your roll number:"))
  name=input(" your Name:")
  department=input("your department:")
  semester=int(input("your semester:"))
  cgpa=float(input("Your C-GPA:"))
  student={
     "roll":roll,
     "name":name,
     "department":department,
     "semester":semester,
     "cgpa":cgpa
   }
  students.append(student)
  save_students()
  print("Student added successfully")
#View student
def viewStudent():
  for student in students:
    print(
      f"roll:{student['roll']} |"
      f"name:{student['name']} |"
      f"cgpa:{student['cgpa']}"
              )
#search student
def searchStudent():
  roll=int(input("Enter the student roll you wnat to search:"))
  for student in students:
    if student["roll"]==roll:
      print(f"Name:{student['name']}")
      print(f"department:{student['department']}")
      print(f"semester:{student['semester']}")
      print(f"cgpa:{student['cgpa']}")
      return
  print("Student not found")
#Delete student
def deleteStudent():
  roll=int(input("Enter roll to delete:"))
  for student in students:
    if student["roll"]==roll:
      students.remove(student)
      save_students()
      print("student deleted")
      return
  print("student not found")
#Main menu
def mainMenu():
   while True:
      print("STUDENT MANAGEMENT SYSTEM")
      print("1.Add Student")
      print("2.View all student")
      print("3.Search student")
      print("4.Delete student")
      print("5.Exit")
      choice=int(input("Enter yiur choice number:"))
      match choice:
         case 1:
            studentAdd()
         case 2:
            viewStudent()
         case 3:
            searchStudent()
         case 4:
            deleteStudent()
         case 5:
            print("Thank you for choosing Student management syste")
            break
students=load_students()
mainMenu()