collection:
    1. list 
    2. tuple 
    3. set 
    4. dict 


list  
    1. denoted by []
    2. ordered 
    3. allow duplicate 
    4. hetrogenous 
    5. mutable 

a=[10,20.5,"apple",True]

tuple
    1. denoted by ()
    2. ordered 
    3. allow duplicate 
    4. hetrogenous 
    5. Immutable 

a=(10,10.5,"apple",False)
print(type(a))

a=(1)
print(type(a)) # int

a=(1,)
print(type(a)) # tuple

set 
    1. denoted by {}
    2. un ordered 
    3. doesn't allow duplicate 
    4. hetreogenous 
    5. mutable 


a=set()
print(type(a))

a={}
print(type(a))

a={1,2,2,2,3,4,5,5}
print(a)

dict 

    1. denoted by {} => key value pair 
    2. key is unique,  value can be duplicate
    3. hetrogenous
    4. mutable
    5. ordered


a={"name":"apple",
   "price":101,
   "color":"green"}

print(a)
print(type(a))
