#In Python an empty value is automatically considered to be False. Consider this code:
#When we run this code, nothing prints to the console.
name = ""
list_a = []

if list_a:
    print("I will not run ")
else:
    print("I am empty")    

#This is because the if statement only runs if the output evaluates to be True, and since our list is empty the condition evaluates to False    