Type Conversion

converting one data type to another  

a="10"
print(type(a))
print(type(int(a)))

type :

1. implicit  (automatic)
2. Explicit  (manual )


implicit conversion

a=10.5
b=10.5
c=a+b 
print(c)
print("a holds",type(a))
print("b holds",type(b))
print("c holds",type(c))


a=10
b=2
c=a/b
print(c)
print("a holds",type(a))
print("b holds",type(b))
print("c holds",type(c))

2.Explicit (manual)

int() -> converts to integer 
float() -> converts to float 
str()-> converts to string 
bool()->converts to Bolean
list()-> converts to list 
tuple()->converts to tuple
set()->converts to set
dict()-> converts to dict 


a="apple"
print(int(a)) # ValueError: invalid literal for int() with base 10: 'apple' 

a="+10"
print(int(a))

a="-10"
print(int(a))

a="10.5"
print(int(a)) # ValueError: invalid literal for int() with base 10: '10.5'  


a="10.4"
print(float(a))

a="10"
print(float(a))


a="10a"
print(int(a)) # ValueError: invalid literal for int() with base 10: '10a' 


a=10
print(float(a))

a="apple"
print(float(a)) # ValueError: could not convert string to float: 'apple' 


a=[10,20,30]
print(tuple(a))


a=True 
print(str(a))


a="true"
print(bool(a))

a="apple"
print(bool(a))

a=""
print(bool(a))


a=" "
print(bool(a))

a="False"
print(bool(a))

a=False
print(bool(a))


Truthy and Falsy 
--------------- 


Falsy 

False 
0 
""
[]
{}
None


a=[]
print(bool(a)) 


a=[10,20,30]
print(int(a))

print(bool(-10))

print(bool(not [])) 

print(bool(None))