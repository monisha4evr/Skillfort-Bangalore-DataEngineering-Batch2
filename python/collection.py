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


Collection methods

1. list 

1. append 
2. extend 
3. insert 

a=[1,2,3,4,5]
a.append(6)
print(a)
a.append([7,8])
print(a[6])

extend 
a=[1,2,3,4,5]
a.extend([6,7])
print(a)

insert
a=[1,2,3,4,5]
a.insert(3,9)
print(a) 


1. remove # remove based on value 
2. pop ()

a=[1,2,3,4]
a.remove(3)
print(a)

a=[1,2,3,4,5,6,7,8]
last_removed=a.pop()
print(last_removed)
print(a.pop())
print(a)
a.pop(5)
print(a)

a.clear()
print(a)
del a

print(a)

a=[1,2,2,3,3,3,3,3,4,5,6]
print(a.count(3))


assignment and copy 

a=[1,2,3]
b=a 
print(a)
print(b)
print(id(a))
print(id(b))


a=[10,20,30]
b=a 
b.append(50)
print(a) # [10, 20, 30, 50]


a=[1,2,3]
b=a.copy() 
print(a)
print(b)
print(id(a))
print(id(b))

a=[10,20,30]
b=a.copy() 
b.append(50)
print(a)
print(b)

index:
a=[20,40,50]
print(a.index(40))

sort 

a=[20,5,10,30,27]
a.sort()
print(a)

a.sort(reverse=True)
print(a)

a=["kiwi","apple","pineapple","banana"]
a.sort()
print(a) 
a.sort(reverse=True)
print(a)
a.sort(key=len)
print(a)

a=[1,2,3,4]
a.reverse()
print(a)


Tuple
a=(1,2,3,4)
print(a.index(3))
print(a.index(9))

a=(1,2,2,2,2,2)
print(a.count(2))

set
a={1,2,3,4,5}
a.add(9)
print(a)
a.update([10,20,30])
print(a)
a.clear()
print(a)

a={1,2,3,4,5}
a.remove(3)
print(a)
a.discard(1)
print(a)
a.discard(9)
print("discard",a)
a.remove(9)
print(a)


a={1,2,3}
b={3,4,5}
print(a.union(b))
print(a | b )

print(a.intersection(b))
print(a&b)

print(a.difference(b))
print(a-b)

print(a.symmetric_difference(b))
print(a ^ b)


dict 

a={
    "name":"apple",
    "color":"red",
    "price":300,
    "color_test":"purple"
}
a.setdefault('color_test',"green")
print(a)

a['origin']="Kashmir"
print(a)
a['price']=500
print(a)

a.update({'qty':30})
print(a)

print(a.keys())
print(a.values())
print(a.items())
print(a.get('price'))