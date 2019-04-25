print("Welcome to magic 8 ball what would you like to be sure about?(Ask a yes/no question)")
question = input()

import random
list_answers = ["It is certain.","Most likely.","My sources say no."," Outlook not so good.","Cannot predict now.","Better not tell you now.","You may rely on it.","Signs point to yes."," Don't count on it.","Outlook good."]      

print (random.choice(list_answers))

