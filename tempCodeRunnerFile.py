import json
def loadStudent():
  with open("haider.json","r") as file:
    return json.load(file)
def saveStudent():
  with open("haider.json","w") as file:
    json.dump(students,file,indent=6)

#ADD Student
def studentAdd():
    name=input("Enter the student name:")
    roll=int(input("Id number:"))
    department=input("Department")
    semester=int(input("Semester"))
    cgpa=float(input("CGPA:"))

    if len(students)==0:
       studentId=1
    else:
       largestId=0
       for student in students:
          if student["id"]>largestId:
             largestId=student["id"]
       studentId=largestId+1
    

    student={
      "name":name,
      "roll":roll,
      "department":department,
      "semester":semester,
      "cgpa":cgpa
    }

    students.append(student)
    saveStudent()
    print("Student added successfully")
    print(f"student Id:{studentId}")
#View student
def viewStudent():
   if len(students)==0:
      print("No student found")
      return
   else:
      print("ALL STUDENT")
      for student in students:
       print(
         f"Name:{student['nmae']}|"
         f"Roll:{student['roll']}|"
         f"Department:{student['department']}|"
         f"Semester:{student['semester']}|"
         f"CGPA:{student['cgpa']}"
       )
#Search Student
def searchStudent():
   studentId=int(input("Enter Id you want to search:"))
   for student in students:
    if student["id"]==studentId:
       print(

          f"Name:{student['name']}|"
          f"Roll:{student['roll']}|"
          f"Department:{student['department']}|"
          f"Semester:{student['semester']}|"
          f"CGPA:{student['cgpa']}"
       )
       return
    else:
       print("Id not found")
#update student
def updateStudent():
   studentId=int(input("Enter the studen  Id:"))
   for student in students:
      if student["id"]==studentId:
         print("Enter the update information:")
         student["name"]=input("Enter the new name:")
         student["roll"]=input("Enter the new roll")
         student["department"]=input("Enter the new department:")
         student["semseter"]=int(input("Enter the new semester:"))
         student["cgpa"]=float(input("Enter the new cgpa:"))
         saveStudent()
         print("Student Information successfuly")
         return
      else:
         print("Student no found")
#delete student
def deleteStudent():
   studentId=int(input("Enter your id you want delete:"))
   for student in students:
      if student["id"]==studentId:
         students.remove(student)
         saveStudent()
         print("Student delete successfully")
         return
      else:
         print("Student not found")
#average cgpa
def averageCgpa():
   if len(students)==0:
      print("Student not found")
      return
   else:
      total=0
      for student in students:
         total= total +student["cgpa"]
      average=total/len(students)
      print(f"Average CGPA:{average:.2f}")
#Highest CGPA
def highestCgpa():
   if len(students)==0:
         print("Student not found")
         return
   else:
      highest=students[0]
      for student in students:
         if student["cgpa"]>highest:
            highest=student
      print(
               f"Name:{highest['nmae']}|"
               f"Roll:{highest['roll']}|"
               f"Department:{highest['department']}|"
               f"Semester:{highest['semester']}|"
               f"CGPA:{highest['cgpa']}"
             )
#Main menu
def main():
   while True:
      print("STUDENT MANAGEMENT SYSTEM")
      print("1.Add student")
      print("2.View student")
      print("3.Search student")
      print("4.Update student")
      print("5.Delete student")
      print("6.Average student")
      print("7.Highest CGPA")
      choice=input("Enter your choice:")
      if choice==1:
         studentAdd()
      elif choice==2:
         viewStudent()
      elif choice==3:
         searchStudent()
      elif choice==4:
         updateStudent()
      elif choice==5:
         deleteStudent()
      elif choice==6:
         averageCgpa()
      elif choice==7:
         highestCgpa()
      elif choice==8:
         print("Thank you")
         break
      else:
         print("Invalid")
students=loadStudent()  
main() 

     
         
      