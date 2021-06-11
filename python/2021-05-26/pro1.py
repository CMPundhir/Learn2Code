print("run python in sublime")
print("Python in sublime is buttery smooth")

# slicing
name = "Chander Mohan Pundhir"
print("Name:",name)

print(name[1:5])
print(name[:5])
print(name[-1])
print(name[-5])
print(name[-5:-1])


age = 12
# print("My name is "+name +" and i am "+age+" years old")
print("My name is",name,"and i am",age,"years old")

intro = "My name is {name} and i am {age} years old"
print(intro.format(name = name, age = age)) # named

intro = "My name is {} and i am {} years old"
print(intro.format(name, age))  # positional

intro = "My name is {1} and i am {0} years old"
print(intro.format(age, name))  # positional

# second method
intro = f"My name is {name} and i am {age} years old"
print(intro)  # positional


print("I am good and i am \"God\"")

