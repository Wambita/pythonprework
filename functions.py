 #we have created a function with no arguments and in the function we have a print statement that outputs a string"
def fun_a():
    print("Hello")

fun_a() 

#passing arguments1
def fan_a(a,b):
    print(a+b)

fan_a(1,4) 

#passing arguments that are already defined (keyword arguments)
def add(a=1, b=4):
    print(a+b)

add (a=6,b=7);   

#We could also call the function without passing any parameters. Then the default keyword arguments values will be passed in
def subtract (a=15,b=2):
    print(a-b)

subtract()

#creating an empty function
def empty ():
    pass

 # functions that return something 
def divide (a,b):
    return a/b  

division = divide(27,9) 

print(division)  


