# 🎓 Student Result System

# Is project mein aap use karenge:

# 1. Student Name | input

# 2. Marks | variables

# 3. Total Marks | operators

# 4. Percentage | arithmetic

# 5. Grade | if-elif-else

# 6. Result Display | functions

# -----------------------------------

# Student List

# -----------------------------------

students = []

# -----------------------------------

# Add Student Information Function

# -----------------------------------

def Add_student():

  name = input("Enter student name: ")

  students.append({
     "name": name
})

  print("Student added successfully")

# -----------------------------------

# Add Marks Function

# -----------------------------------

def Add_marks():
   name = input("Enter student name: ")

   for student in students:

    if student["name"] == name:

      math = int(input("Enter Math marks: "))
      python = int(input("Enter Python marks: "))
      urdu = int(input("Enter Urdu marks: "))
      english = int(input("Enter English marks: "))

      student["math"] = math
      student["python"] = python
      student["urdu"] = urdu
      student["english"] = english

      print("Marks added successfully")
      return

    print("Student not found")

# -----------------------------------

# Add Total Marks Function

# -----------------------------------

def Add_totalmarks():

  name = input("Enter student name: ")

  for student in students:

   if student["name"] == name:

    total = (
        student["math"]
        + student["english"]
        + student["urdu"]
        + student["python"]
    )

    student["total"] = total

    print("Total marks:", total)
    return

  print("Student not found")

# -----------------------------------

# Add Percentage Function

# -----------------------------------

def Add_percentage():

  name = input("Enter student name: ")

  for student in students:

   if student["name"] == name:

    percentage = (student["total"] / 400) * 100

    student["percentage"] = percentage

    print("Percentage:", round(percentage, 2), "%")
    return

   print("Student not found")

# -----------------------------------

# Add Grade Function

# -----------------------------------
def Add_grade():

    name = input("Enter student name: ")

    for student in students:

        if student["name"] == name:

            percentage = student["percentage"]

            if percentage >= 80:
                grade = "A"

            elif percentage >= 70:
                grade = "B"

            elif percentage >= 60:
                grade = "C"

            elif percentage >= 50:
                grade = "D"

            else:
                grade = "Fail"

            student["grade"] = grade

            print("Grade:", grade)
            return

    print("Student not found")
# -----------------------------------

# Add Result Display Function

# -----------------------------------

def Add_result():

   name = input("Enter student name: ")

   for student in students:

      if student["name"] == name:

        print("\n==============================")
        print("   STUDENT RESULT")
        print("==============================")

        print("Name       :", student["name"])
        print("Math       :", student["math"])
        print("Python     :", student["python"])
        print("Urdu       :", student["urdu"])
        print("English    :", student["english"])

        print("------------------------------")

        print("Total Marks:", student["total"])
        print("Percentage :", round(student["percentage"], 2), "%")
        print("grade :", student["grade"])

        print("==============================")

        return

   print("Student not found")

# -----------------------------------

# Main Program

# -----------------------------------

while True:

   print("\nWelcome to Student Result System")
   print("1. Add Student")
   print("2. Add Marks")
   print("3. Add Total Marks")
   print("4. Add Percentage")
   print("5. Add Grade")
   print("6. Show Result")
   print("7. Exit")

   choice = input("Enter your choice: ")

   if choice == "1":
      Add_student()

   elif choice == "2":
      Add_marks()

   elif choice == "3":
      Add_totalmarks()

   elif choice == "4":
      Add_percentage()

   elif choice == "5":
      Add_grade()

   elif choice == "6":
      Add_result()

   elif choice == "7":
     print("Keep it up! ❤️")
     break

   else:
      print("Invalid choice, please try again.")