def get_age():
    print("How old are you ")
    age = int(input())
    return age

print(get_age())
#The program works fine if we enter a number. But what if a user enters a name
# We get a ValueError because we put in a non integer string and the int()constructor cannot convert the string to integer.

#This error is difficult to understand. Let us create a more understandable error message
def get_age():
    print("How old are you ")
    try:
        age = int(input())
        return age
    except ValueError:
        return "That was not a valid input"

print(get_age())       