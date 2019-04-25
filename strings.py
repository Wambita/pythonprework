#embedding variables into strings {Formatting strings f-strings}
name = "Fana"
age = 17

print(f"my name is {name} and i am {age} years old")
"The f before the string stands for f-strings or formatted strings and allow us to put replacement fields {} with variable names inside our strings"

#Raw strings : are special type of string that allows us to ignore all escape characters \ and print them out
print ('Baby\'s day out')
print('Beyonce\'s lemonade stand') 
#Here we see a proper use of the escape \ character, by allowing us to add an apostrophe.But let us create a raw string and see what happens
print(r'beyonce\'s lemonade stand')
# We notice the r before the string. This means raw string. And in the output unlike the first example it prints out even the escape character.