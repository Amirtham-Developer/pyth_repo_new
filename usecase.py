1. The following program throws an indentation error. Correct it and make sure it prints properly

teams = ['Data', 'AI', 'DevOps']
for t in teams:
    print('Hello', t, 'Team from Inceptez Technologies')
    print('Keep Learning and Exploring!')
    
2.Add single-line and multi-line comments to describe what the below code does for Inceptez Technologies’ training tracker.

#total number of student from Inceptez Technologies
students = 100
#total number of trainer from Inceptez Technologies
trainers = 2
'''add total number of student
and total number of trainer from Inceptez Technologies
print the overeall count'''
total = students + trainers
print(total)

3.Use Case 2:
Convert the below block into a “dead code” using comments, then re-activate it later to print

#print("Welcome to Inceptez Python Learning") #It will not run

print("Welcome to Inceptez Python Learning") #It will run 

C. Playing with Quotes
Use Case 1:
Create three string variables that correctly store and print:
var1="This is jeeva's python code"
var2='This code was written by "Jeeva"'
var3=""" This is "Infosys's" company's property"""
print(var1,var2,var3)

Use Case 2:
Write a multiline string using triple quotes that prints:

print(""" Welcome to Inceptez Technologies!
Python Training: Basics
Enjoy your learning journey""")

D. Let's learn all about VARIABLES
Use Case 1:

name="Jeeva"
course_name="Python Fundamentals"
Training_Ins="Inceptez Technologies"
print(f"{name} is learning the course{course_name} at the institute{Training_Ins}")


Use Case 2:
Demonstrate dynamic inference, dynamic typing using with fee by applying .18 gst  and prove strongly typing character also by operating it with Eighteen percent gst

fee = 45000
dynamic typing
fee=45000
gst_amt=1.5
amt=fee*gst_amt #fee is int type and gst_amt is float type we can multiple both of them 
print(type(amt))


#Dynamic inference
fee=45000
print(type(fee))#Python automatically treats fee as a number Dynamic inference

#it is not strong type

fee=45000
print(fee+"eightien percent gst")#Error can't string and int
--------------------------------------------------------------------------------------------------------------------------------------
E. Variables Naming Conventions
Use Case 1:
Identify which variable names below are invalid for Inceptez’s student database:

1) 2student = 'Ravi'
2) _student_id = 1001
3) studentName = 'Priya'
4) class name = 'Python'
5) inceptez_batch = 'Morning

1)option 1 and 4 

2student

Invalid because variable names cannot start with a number.

class name

Invalid because variable names cannot contain spaces.

Also, class is a reserved keyword in Python.

Use Case 2:
Declare 3 variables following naming styles for Inceptez projects:

PascalCase: DataEngineeringBatch
camelCase: dataEngineeringBatch
snake_case: data_engineering_batch

DataEngineeringBatch="Morning Batch"
dataEngineeringBatch="Morning Batch"
data_engineering_batch="Morning Batch"

---------------------------------------------------------------------------------------------------------------------------------------
F. Type identification & Casting
Use Case 1:
Write a program that asks for an employee’s age.
1. Checks its type is of string
2. Converts it to int
3. Prints the years pending for retirement, for eg. 60 is the retirement age.
Example:
Enter your age: 40
You will retire in 20 years at Inceptez Technologies.


#ask age input from user
age=input("enter your age:")
retirement_age=60
if type(age)==str:
    age=int(age)
    year_left=retirement_age-age
    if year_left>0:
        print(f"You will retire in {year_left} years at Inceptez Technologies")
    else:
            print("already retirement")
            
            
 Use Case 2 (Debug):
Fix the type error in the following code for salary calculation:

salary = '50000'
bonus = 10000
salary=int(salary)
print('Total Salary in Inceptez:', salary + bonus)  
            
---------------------------------------------------------------------------------------------------------------------------------------------

G. Standard Input & output options
Use Case 1:
Write a Python program that takes two inputs:

student_name=input("enter your name:")
course_name=input("enter your course name:")

print(f" {student_name} welcome to the {course_name} batch at Inceptez Technologies")

Use Case 2:
Rewrite the following using the format() function instead of   f-string:

print('The Python course at Inceptez Technologies costs {} rupees'.format(fee))

----------------------------------------------------------------------------------------------------------------------------

Use Case 1 — Employee Salary Breakdown Using Numeric & String Types
Employee Salary Breakdown
a. Write a program that asks the user for:
employee_name (string)
base_salary (float)
hra_percent (integer)
bonus_amount (float)

#asking user inputs
employee_name=input("enter employee name:")#it should be string`
base_salary=input("enter base salary:") #it should be float
hra_percent=input("enter hra percent:")# it shuuld be int
bonus_amount=input("enter bonus amount:")# it should be float

#type checking

print (type(employee_name))
print (type(base_salary))
print (type(hra_percent))
print (type(bonus_amount))

# type conversion
base_salary = float(base_salary)   # convert user input to float
hra_percent = int(hra_percent)     # convert user input to int
bonus_amount = float(bonus_amount) # convert user input to float

print (type(base_salary))
print (type(hra_percent))
print (type(bonus_amount))

B. Convert inputs to the correct datatype if required.

HRA = base_salary * (hra_percent / 100)
Total_Salary = base_salary + HRA + bonus_amount

C. Print the output like this:

print((f"Employee:{employee_name} Base Salary:{base_salary} HRA:{HRA} bonus:{bonus_amount} Total_Salary_payable:{Total_Salary}"))

Use Case 2: Student Result Classification

Tamil=input("Enter tamil mark:")
English=input("Enter english mark:")
Maths=input("Enter maths mark:")
science=input("Enter science mark:")
social_science=input("Enter s.science mark:")

B. Check if the value can be converted to float.
#type conversion
Tamil=float(Tamil)
English=float(English)
Maths=float(Maths)
science=float(science)
social_science=float(social_science)

total=Tamil+English+Maths+science+social_science
percentage=total/5
# type checking
print (type(Tamil))
print (type(English))
print (type(Maths))
print (type(science))
print (type(social_science))

#C. Then classify:
if percentage>=90:
    print("Outstanding")
elif percentage>=75:
    print("Excelent")
elif percentage>=50:
    print("pass")
elif percentage<50:
    print("fail")

else:
    print("Invalid marks entered ")

Use Case 3: Bug Fixing — Datatype Mismatch

item_name = input("Enter product name: ")
price = input("Enter price per item: ")
quantity = input("Enter quantity: ")
#type conversion
price=float(price)
quantity=int(quantity)
total_cost = price * quantity
print("You purchased " + str(quantity) + " units of " + item_name)
#print(f"You purchased {quantity} units of {item_name}")
print("Total payable: " +str( total_cost))
#print(f"Total payablee{total_cost}"}
print("Total payable: " + total_cost)
--------------------------------------------------------
#Use Case 1: Internet Data Usage Calculator
#Write a program that asks the user for:
#Total monthly data limit (in GB)
#Data used so far (in GB)

monthly_data_limit=int(input("Enter monthly data limit:"))
used=float(input("Enter used data:"))
#Calculate using arithmetic operators:
Remaining_data = monthly_data_limit - used
round_remaining_data = round(Remaining_data,2)
Usage_percentage = (used / monthly_data_limit) * 100
rounded_percentage = round(Usage_percentage, 2)
#Print
print(f"Remaining data is {round_remaining_data} GB")
print(f"Usage percentage is {rounded_percentage}%")

if Usage_percentage>=80:
    print(f"Warning:{round_remaining_data}% GB Data Remaining High usage, consider upgrading your plan.")


#Use Case 2: Shopping Discount Calculation

product_price=float(input("Enter product price"))
discount_percent=int(input("Enter discount precentage"))

#Using assignment and arithmetic operators, calculate:
 discount_amount = (product_price * discount_percent) / 100
 final_price = product_price - discount_amount
#Print:
    
 print(f"Original price{product_pric} , discount applied {discount_amount} , and final payable amount is{final_price}.
 
#Use Case 3 (Bug Fixing): Logical and Comparison Operator Errors
#The following code should determine voting eligibility, but it contains operator mistakes. Fix it.
#Incorrect code:

age = int(input("Enter age: "))
citizen = input("Are you an Indian citizen? (yes/no)").lower()
if age >= 18 and citizen == "yes":
 print("Eligible to vote")
else:
 print("Not eligible")
 
 ------------------------------------------------------------------------------------------------------------------------
#K. Conditional Structure
#Use Case 1: Banking Eligibility Check
#Write a program that asks the user for:Age,Monthly income

age=int(input("Enter your age:"))
monthly_income=int(input("Enter monthly income:"))

if age<18:
    print("Not eligible for a bank account")
elif age>= 18 and monthly_income<15000:
    print("Eligible for basic savings account")
elif age>= 18 and monthly_income >=15000 and monthly_income <50000:
    print("Eligible for savings + salary account")
elif age>= 18 and monthly_income>50000:
    print("Eligible for premium account")




 
 
