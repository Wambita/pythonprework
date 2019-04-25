#  how to create empty dictionary
my_dict = {} #1
my_dict = dict() #2

# Creating a dictionary with keys and values
my_cat = {'name':'Mr Sniffles','age':18, 'color':'black'}

#Accessing values from dictionary
print(my_cat['name']) #1

cat_name = my_cat['name']
print(cat_name) # 2

#Adding items to a dict
birthdays = {"fana":"June 10", "Charity":"December 23"}
birthdays["Louisah"]="July 11"
print(birthdays)

#Getting indivdual keys in the dictionary
print(birthdays.keys())

#We can convert the keys  into a list using the list() function.
print(list(birthdays.keys()))