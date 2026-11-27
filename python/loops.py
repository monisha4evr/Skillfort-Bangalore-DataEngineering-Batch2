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

5. 
a="banana"
temp={}
for i in a:
    if i not in temp:
        temp[i]=1
    else:
        temp[i]+=1

print(temp)

a="banana"
count={}
for c in a:
    count[c]=count.get(c,0)+1
print(count)


# jumping statement  

1. break # break the iteration
2. continue  # skip the current iteration
3. pass  # ignore indendation error 

1. break 

for i in range(1,11):
    print(i)
    if i==5:
        break

for i in range(1,11):
    if i==5:
        continue
    print(i)
   

Nested Loop 
    - Loop inside Loop 


* * *
* * * 
* * * 



for i in range(3):
    for j in range(3):
        print(f" ({i}{j})",end="")
    print()

execution flow()
--------------- 
step 1: 

i=0 
    j=0    0 1 2
    j=1  
    j=2

i=1 
    j=0   0 1 2 
    j=1   
    j=2

i=2 

    j=0  0 1 2
    j =1 
    j=2



for i in range(3):
    for j in range(3):
        print("*",end="")
    print()


0 0 0
1 1 1
2 2 2

for i in range(3):
    for j in range(3):
        print(i,end="")
    print()

123
123
123

for i in range(1,4):
    for j in range(1,4):
        print(j,end="")
    print()


* 
* * 
* * *  

for i in range(3):
    for j in range(i+1):
        print("*",end=" ")
    print()

execution flow:
step 
i = [0,1,2]
i=0 
    j=0+1= 1 [0]  *
i=1 
    j=1+1 =2 [0,1]
    j=0   * * 
    j=1   
i=2 
    j=2+1 =3 [0,1,2]
    j=0  * * * 
    j=1  
    j=2

* * * 
* * 
* 

outer =3 
inner controlled by outer 

for i in range(3,0,-1): # [3,2,1]
    for j in range(i):
        print("*",end=' ')
    print()




a=[1,2,3]
print(a*3)


a="123"
print(a*3)
#print(a+3) # TypeError: can only concatenate str (not "int") to str


for i in range(1,4):
    print("*"*i)

  *
 **
***

***
 ** 
  * 

  * 
 ***
*****
 ***
  *

A 
AB 
ABC 

print(chr(65))
print(chr(66))

print(ord('A'))


# list comprehension

Syntax: [expression for variable in iterables]

a=[1,2,3,4,5,6] 

print([i*2 for i in a ])

print([i for i in a if i>3])

print(["Even" if i%2==0 else "Odd" for i in a])


# dictionary comprehension

Syntax: {key:value for variable in iterables} 

a=[1,2,3,4,5,6] 
print({i:i*2 for i in a })


Task 1. combine both list without build in
a=[1,2,3]
b=[4,5,6]

zip()
a=['dhanasekar','madhan',"Gnasehwari",'sowmy'] 
b=['chennai','AP','Bangalore','Kadapa','Thanjai']

print(list(zip(a,b)))
print(dict(zip(a,b)))

for i,j in zip(a,b):
    print(i,j)


# 1 dhanasekar
# 2 madhan
# 3 Gnasehwari
# 4 Sowmy

a=['Dhanasekar','Madhan ',"Gnasehwari",'Sowmy'] 
c=1

for i in a:
    print(c,i)
    c+=1

enumerate
- it return 2 values 
1. index position 
2. Value

a=['Dhanasekar','Madhan ',"Gnasehwari",'Sowmy'] 
for i,j in enumerate(a,start=1):
    print(i,j)





