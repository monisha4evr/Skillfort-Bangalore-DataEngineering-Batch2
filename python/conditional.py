Conditional statement 
 - execution made on condition 
- execute a block on some condition

Types of condition

if 
if else 
if elif  else 
nested if 


match case 
tenerary operator


simple if

Syntax:

if condition : 
    pass 

age = 18 
if age>=18:
    pass
print("Example for if condition")


age = 12
if age>=18:
    print("Age is above or equals to 18")
print("Example for if condition")


Syntax:

if condition :
   pass
   # statement 
else : 
   pass
   # statement 


age = 12
if age>=18:
    print("Age is above or equals to 18")
else :
    print("age id below 18")
print("Example for if condition") 


print(19%2)

number=19
if number % 2 == 0 :
   print("Even number")
else:
   print("Odd number")


print("if Example")
if 1 :
   print("Execute True Block")
print("if Example ends here ")



print("if Example")
if False :
   print("Execute Statement 1")
else:
   print("I am in else Block")
print("if Example ends here ")

age=18
has_voter_id=False
if  age>=18 and has_voter_id:
   print("you are eligible to Vote")
else:
   print("not Eligible")

if elif else 

if condition :
   pass
elif condition2 :
   pass
elif condition3 :
   pass
else :
   pass 



# >=90 => "A grade
# >80 <90 => "B grade"
# >70 <80 => "c grade"
# <70 fail

marks=90
if marks>=70 and marks <80:
   print("c grade")
elif marks>80 and marks<90:
   print("B grade")
elif marks>=90:
   print(" A grade")
else: 
   print("Fail")

# wrong example
marks=90
if marks>=70 :  # u have to give 90 first
   print("c grade")
elif marks>80 :
   print("B grade")
elif marks>=90:
   print(" A grade")
else: 
   print("Fail")


# correct way
marks=90
if marks>=90 :  # u have to give 90 first
   print("A grade")
elif marks>80 :
   print("B grade")
elif marks>=70:
   print(" C grade")
else: 
   print("Fail")

a=160
b=90
c=210

if a>b and a>c:
   print("A is Greater")
elif b>c:
   print("B is Greater")
else :
   print("C is greater")


nested if 
if inside if 

Syntax:
if condition:
   if condition:
      pass
else:
   pass


age=12
has_voter_id=False
if  age>=18 :
    if has_voter_id:
        print("you are eligible to Vote")
    else:
       print("Voter Id is needed")

else:
   print("Below 18")


Ternary :
number=18
if number%2==0:
   print("Even")
else:
   print("odd")

Syntax: 

condition_if_true if condition else condition_if_false  

num=20
print("Even" if num%2==0 else "Odd")


mathc case:
-- to check multiple condition based on case 

day=9
match day:
    case 1 | 2 | 3 |4 |5:
      print("Its Weekday")
    case 0 |7 :
        print ("its weekend")
    case _ :
      print("invalid number")


task 1: 
    1. find whether number is positive or negative 
    2. find the given string is palindrome ( madam ) 
    3. check if the value is even then add +10 if odd means multiply by 2 


a=16
print(a>>2)
print(2 << 3)