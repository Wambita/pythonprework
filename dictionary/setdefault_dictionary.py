#an application that counts every character in an input string. 

 #We prompt the user for an input. Then we create an empty dictionary named characters that will store each individual character and how many times it has been used. 
print("enter a string") 

input_string = input()

characters = {}

#Here we use a for loop to iterate through each individual character in the string. Then we use the setdefault() method to create a key for each character if the character does not exist in the dictionary. Then we set the default value for each as 0.
for character in input_string:
    characters.setdefault(character,0)
#Lastly we target the key that matches the character and add one to the value everytime the character is encountered.
    characters[character] = characters[character] + 1

print(characters)    

#python3.6 setdefault_dictionary.py