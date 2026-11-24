welcome 

print("welcome")
print("welcome")
print("welcome")
print("welcome")
print("welcome")
print("welcome")
print("welcome")

2 types :

for 
while 

Syntax:
-------

for var in iterable : 
    #statement
    pass  

a=[1,2,3,4,5]

for i in a:
    print(i)

exection flow:
iteration 1: 
i=1    =1 
i=2    =2
upto 
i= 5     =5


range(start,stop,step)

start => initial value 
stop => n+1 (last value is excluded)
step => jump 

for i in range(1,11):
    print(i,"welcome") 

# 0 2 4 6 8 10
for i in range(0,11,2):
    print(i)

# 2*1=2
tbl=5
n=10
for i in range(1,n+1):#[1,2,3,4,5]
    print(f" {tbl} * {i} = {tbl*i}")

a=(10,20,30,40)
for i in a:
    print(i)

a={12,23,23,43,56,6,12}
for i in a:
    print(i)

# 10 9 8 7 6 5 4 3 2 1 

for i in range(10,0,-1):
    print(i) 


print([1,2,3] * 3)
print("123"*3)

a="flower"
for i in a:
    print(i)

a=123
for i in a:
    print(i)  # TypeError: 'int' object is not iterable 


a=str(123)
for i in  a:
    print(i) 


for i in range(1,4):
    print("*"*i)

for i in range(3,0,-1):
    print("*"*i) 

while loop 

intialize 
while condition :
    incr/decre 

# 1 2 3 4 5

i=1
while i<=5:
    print(i)
    i+=1 # i=i+1

i=10
while i>=1:
    print(i)
    i-=1 # i=i+1



task 1. 

find the even number between 1 to 10 use for loop 
find vowels in word "python" 
count number of character in "Python is interesting to learn" without built in function
count vowels and consonent in "where there is a will there is a way" 
count number of occurance "banana" Expected output {b:1 ,a:3,n:2}

