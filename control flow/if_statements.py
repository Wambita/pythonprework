#If  statements
#  runs only when the condition passed to it evaluates to true
print("if statements")
print("Enter your height in inches" )
height = int(input())

if height > 70 :
    print ("You are so tall!!!!")

 # if .. else   
 # runs only when the condition passed evaluates to false
print("if... else statements")
print("Enter your height in inches" )
height = int(input())

if height > 70 :
    print ("You are so tall!!!!")
else:
    print("You are really short!!!")

# elif 
# used when we have more than one condition to check for
print("elif statements")
print("Enter your height in inches" )
height = int(input())

if height > 70 :
    print ("You are so tall!!!!")
elif height > 60:
    print("You are of average height!!!")
else:   
    print("You are really short")

 #To run the code type this in terminal python3.6 if_statements.py   
