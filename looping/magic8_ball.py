print("Welcome to magic 8 ball what would you like to be sure about?(Ask a yes/no question)")
question =input()

import random
number = random.randint(1,10)

if number == 1 :
    print("It is certain.")
elif number == 2:
    print("Most likely.") 
elif number == 3:
    print("My sources say no. ")    
elif number == 4:
    print(" Outlook not so good.")    
elif number == 5:
    print("Cannot predict now.")    
elif number == 6:
    print("Better not tell you now.")    
elif number == 7:
    print("You may rely on it.")    
elif number == 8:
    print("Signs point to yes.")    
elif number == 9:
    print(" Don't count on it.")    
else:
    print("Outlook good.")            

