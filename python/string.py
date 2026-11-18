enclosed by single or double  or triple quotes 


a= 'car'
b="apple"
c=''' where there is 
a will 
there is a way '''

print(a,b)
print(c)

# comment 
# comment 
# comment line

'''
print(a,b)
print(c)
'''

# indexing
a="apple"
print(a[3])

b="python is interesting"
print(b[-9:-7])

print(b[::-1])
print(b[::4])
print(b[-6])

# Slicing 
# Syntax: [start : end : step]

print(b[7:9])
print(b[0:])
print(b[:9])
print(b[::2])

a="apple"
print(a[2:])
print(a[::2])

a="Good"
b="morning" 
print(a+" "+b)

# String methods

# case conversion
a="apple"
print(a.capitalize())
print(a.upper())
b="BANANA"
print(b.lower())
c="Python is easy to LeARN"
print(c.title())
print(len(c))

# del c 
# print(c) NameError: name 'c' is not defined

# search 
1. find()
2. index()

a="pineapple"

print(a.count('p'))

print(a.find('p'))
print(a.rfind('p'))
print(a.find("P"))
print(a.find('z'))

print(a.index('p'))
print(a.index('z')) # ValueError: substring not found 


print("Jasmine".startswith('J'))
print("Jasmine".endswith('a'))

# Remove spaces 
a= " madhan "
print(a)
print(a.strip())
print(a.lstrip())
print(a.rstrip())

# replace
a="i like Java"
print(a.replace("Java","Python"))

# split 

a="apple,orange,banana,grapes"
print(a.split(','))
print(a.rsplit(",",2))
print(a.rsplit(",",1))

print("sowmy@gmail.com".partition('@'))
print("sowmy@gmail.com".partition('.'))
print("gnaneshwari.15@gmail.com".partition('.'))
print("gnaneshwari.15@gmail.com".rpartition('.'))

# checking 
a="1234"
print(a.isnumeric())

a="12aa"
print(a.isnumeric())


a="abc"
print(a.isalpha())

a="abc123"
print(a.isalpha())


# alignment 
a="apple"
print(a.zfill(7))
a.r

# format
a=10
b=20
c=a+b

print(" a value is",a,"b value is ",b,"C value is",c)
print(f" a value is {a} b value is {b} c value is {c} ")


# join

fruits=['apple','orange','mango']

print(" ".join(fruits))
print("@".join(fruits))
