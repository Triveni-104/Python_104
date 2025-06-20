students = {}
n = int(input("enter how many students "))

for i in range(n):
    name=input("enter the Name of the student :")
    firstname= input("Enter the firstname: ")
    lastname= input("Enter the lastname: ")
    gender = input("Enter gender: ")
    contact = int(input("Enter contact: "))
    date_of_birth = input("Enter the date of birth: ")
    highest_qualification = input("Enter the highest qualification: ")
    current_qualification = input("Enter the current qualification: ")
    mail_id = input("Enter EMAIL ID: ")
    password= input("Enter password: ")


    students[name] = {"First Name": firstname,"Last Name": lastname,"Gender": gender,"Contact": contact,"Date of Birth": date_of_birth,"Highest Qualification": highest_qualification,"Current Qualification": current_qualification,"Email ID": mail_id,"Password": password}
print("\nStudent details entered:")
for student, details in students.items():
    print(f"\nStudent Name: {students}")