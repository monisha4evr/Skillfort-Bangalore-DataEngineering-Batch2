python 
- high level programming Language 
- interpreter  (partially interpreted) -pvm (Python Pirtual Machine)  compile -> bytecode -> pvm (line by line read)
- General purpose programming language 
- cross platform support


features:
- simple and readable syntax 
- cross platform 
- multiple Paradigms (top down (functional) and botton up (oops) )

rules:
1. case sensitive  
2. Identation is important 
3. no need for { } 
4. statement automatically ends in a new line 
5. to save : .py 


print('hello World')

variable : 
    container 

a=10
print("A value",a) 
print(id(a))
b=10
print(b)
print(id(b))


a="apple"
print(a)
print(id(a))

print(b)
print(id(b))



a=10
print(id(a))
a=20
print(id(a))

a=[10,20,30,'apple',True]
print(id(a))
print(a)
a.append(1)
print(id(a))
print(a)


datatype 
1. integer - int 
2. decimal - float  
3. string (sequence of character ) => str 
4. Boolean - True / False 
5. None -> no value / return Nothing None Type 
6. list 
7. tuple 
8. set 
9. dictionary (map) dict 
10. complex 


numeric 
1. int 
2. float 
3. complex 

sequence 
1. str 
2. list 
3. tuple 
4. range 

set 

map - key - value pair (dict)

immutable 

int  - whole number (0-9 + , - )
float
tuple  ()
str 

mutable  (2 variable dont share same memory even they hold same values)
list - []
set -set()
dict -{}

ordered , unordered  

ordered  unordered  (set)
list   
tuple 
dict 



a=12.5
print(type(a))

a="12.5"
print(type(a))

a=+10
print(type(a))

a=True
print(type(a))



a=10
b=10
print(id(a))
print(id(b))


a=[1,2,3,4] 
b=[1,2,3,4]
print(id(a))
print(id(b))


a=(1,2,3)
b=(1,2,3)
print(id(a),id(b))


a="apple"
b="apple"
print(id(a),id(b))


a=True
b=True
print(id(a),id(b))


a=[10,20,30]
b=[10,20,30]
print(id(a),id(b)) 


type casting 

 - convert one datatype  to another data type 

1. implicit  (automatic)
2. explicit (manual)

implicit 

a=10
b=12.5

print(a+b)


a=10
b=2 
c=a/b 
print(c)

explicit 

a=10
b=20
print(a+b)


a="10"
b="20"
print(a+b)


a=int("10")
b=int("20")
print(a+b)


a=int("apple") #  ValueError: invalid literal for int() with base 10: 'apple'
print(a)


a=int("+10")
print(a)


a=int("*10")
print(a)


a=int("10.5")  # ValueError: invalid literal for int() with base 10: '10.5'
print(a)

a=float("10.5")  
print(a)

a=int(10.5)
print(a)