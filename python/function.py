# Function 
# - Reusable block of code ,
# - used to perform some specific Task 

Syntax: 

# declaration/definiton
def function_name():
    pass 

# calling Function
function_name()



def greet():
    print("welcome") 

for i in range(3):
    greet()



types of Function 
1. built -in 
2. user-defined 
3. lambda 
4. Recursion 

1. built -in 
    print()
    input()
    len() 

2. user-defined  


# return : keyword 
it returns the value to the calling function 

def test():
    print(" i am inside function")
    return 'apple'
    print("I am example for test function")

t=test()
print(t)

print(test())


# argument   - actual value  (calling function)
# parameter - Alias Value (Declaration part )


def greet(name):  # parameter
    print("Welcome ",name)

a="Sowmy"
greet(a)  # argument

greet("Madhan")





rules: 
1. argument count must match with Parameter count 


def greet(name):  # parameter
    print("Welcome ",name)

a="Sowmy"
greet(a)  # argument

greet("Madhan","Kadapa")


types: 
1. with argument without return 
2. without argument with return 
3. with argument with return
4. without argument without return


1. with argument without return 

def display(name,city):
    print(name,city) 

display("Sowmy","Andra")




name="sowmy"
city="Andra"
def display(name,city):
    print(name,city) 
display()  # TypeError: display() missing 2 required positional arguments: 'name' and 'city'


name="sowmy"
city="Andra"
def display():
    print(name,city) 
display() 


name="sowmy"
city="Andra"
def display():
    name="Gnaneshwari"
    course="DE"
    print(name,city,course) 
display() 

print(course)


2. without argument with return 

def display():
    a=10
    b=20 
    return(a+b)

print(display())


def display():
    a=10
    b=20 
    return a,b

z=display()
print(z)

t,u=display()
print(t,u)

a=[10,20,30]
for i in a :
    print(i)

a=[10,20,30,40]
a,b,c,d = a
print(a)
print(b)
print(c)


3. with argument with return 

def add(m,n):
    return m+n 

a=add(10,20)
print(a)

4. without argument without return

def display():
    name="Sowmy"
    print("Welcome ",name)

display()


types of arguments:
1. Positional  argument 
2. keyword argument 
3. default argument 
4. aribitary argument

1. Positional  argument 

- based on position

def test(a,b,c,d):
    print(a,b,c,d)

test(10,20,30,40)

2. keyword argument 
- key=value pair

def sample(a,b,c,d):
    print(a,b,c,d)

sample(d=10,a=30,c=20,b=90)
sample(d=10,o=30,n=20,m=90) # TypeError: sample() got an unexpected keyword argument 'o'


3. default argument 

def check (a,b,c=0):
    print(a,b,c)

check(10,20)
check(10,20,30) 

4. aribitary argument

1. variable length

def sample(a,*b):
    print(a,b)

sample(1,2,3,4,5)

2. keyword length

def sample(a,**b):
    print(a,b)

sample(a=1,b=2,c=3,d=4,e=5) 

# positional only

def test(a,b,/,c,d):
    print(a,b,c,d)

test(10,20,d=30,c=40) # (/)left side arguments  considered as Positional only argument
test(b=10,20,d=30,c=40) # Positional argument cannot appear after keyword arguments
test(b=10,a=20,d=30,c=40) # TypeError: test() got some positional-only arguments passed as keyword arguments: 'a, b'


# keyword only 

def sample(*,a,b,c,d): # (*) right side arguments considered as keyword only argument
    print(a,b,c,d)
sample(d=10,a=30,c=20,b=90)
sample(10,a=30,c=20,b=90) # TypeError: sample() takes 0 positional arguments but 1 positional argument (and 3 keyword-only arguments) were given


lambda:
    -- simple and short version 
    -- Anonymous function 

    -- it takes n number of arguments 
    -- it perform single expression 
    -- no need to give return keyword

syntax: lambda arguments:expression



def add(a,b):
    return(a+b)

print(type(add))
print(add())


add=lambda a,b:a+b 
print(type(add))
print(add(10,20))



Recursion 
higher order function 
