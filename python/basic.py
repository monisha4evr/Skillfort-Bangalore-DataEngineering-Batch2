print("Simple Addition")
a=10
b=50
c=a+b

print(a,b,c)

a=10
b=10
print(id(a))
print(id(b))


a=10.5
b=10.5

print(id(a))
print(id(b))

a=10
print(id(a))
a=20
print(id(a))


a=[1,2,3,4]
print(id(a))
a.append(5)
print(id(a))

print(type(a)) 


a=10
b=10.5

print(id(a),id(b))


a=[10,20,30]
b=[10,20,30]
print(id(a),id(b))


a=(10,20,30)
b=(10,20,30)
print(id(a),id(b))


a={10,20,"apple",True,20.5}
b={10,20,"apple",True,20.5}
print(id(a),id(b))





