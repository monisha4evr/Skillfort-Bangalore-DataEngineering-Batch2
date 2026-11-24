operator is used to perform Mathematical Operations 

a=b+c 

b+c => Expression
b,c => operands 
+   => addition Operation

types of Operator 
1. Arithmetic operator (+,-,*)
2. Assignment operator (== , += ... )
3. Comparision operator (= , > < >= <= etc..)
4. Logical operator (and or not)
5. Membership operator   (in , not in)
6. identity operator (is, is not)
7. Bitwise operator

1. Arithmetic operator 

addition 
subtraction
multiplication
division (Quotient)
modulo Division (remainder)
Floor division (//)
Exponential (**)


a=10
b=40
print("Addition",a+b)
print("subtraction",50-10)
print("multiplication",10*5)
# print("division",5/0)  ZeroDivisionError: division by zero
print("division",5/2)
print("floor division",5//2)
print("modulo diviion",5/2)
print(5**2)


2. Assignment operator (== , += ... )

a=10
print(a)

a,b=20,10

print(a)
print(b)


a=10
b=20
print(a)
print(b)
a,b=b,a 
print("After swap")
print(a)
print(b)

a=b=c=10
print(a)
print(b)
print(c)

a=50
a+=10 #(a=a+10)
print(a)

# 3. Comparision operator (= , > < >= <= etc..)
#     - it compare 2 values and return Boolean Value (True / False)

a=10
b=50
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a!=b)
print(a==b)

4. Logical operator (and or not) 

and  

True + True = True
True + False = False 
False + True = False
False + False = False 
or 
True - True = True
True - False = True 
False - True = True
False - False = False 

not 

True => False 
False => True

a=10 
b=20 
c=30 
print(a>b and b>c)

# a>b => False 
# b>c => False 
# False + False => False
a=50 
b=20 
c=30 
print(a>b or  b>c)

a>b => True 
b>c => False 
True

a=10
print(not a)

a=' '
print(not a)

a=[]
print(not a)


age =19
voter_id =True 
print(age>=18 and voter_id )

5. Membership operator   (in , not in) 

a=[1,2,3,4,5]
print(4 in a)
print(9 in a)


a=('apple','orange','banana','kiwi')
print("Guava" in a)
print('kiwi' not in a)

a="Flower"
print('w' in a)

a=1234
print(3 in a) # TypeError: argument of type 'int' is not a container or iterable


6. identity operator (is, is not) 

a=10
b=10
print(a is b)

a=[1,2,3]
b=[1,2,3]

print(a is b)


a=(1,2,3)
b=(1,2,3)
print(a is b)

c=a
print(c is a)


c=[1,2,3]
d=c.copy()
print(d is c)
print(d is not c)


7. Bitwise operator 
perform operation based on Binary values

and => & 
or => | 
not ~ 
xor ^ 
left shift <<
right shift  >>


a=2
print(a<<2)
print(a>>2)