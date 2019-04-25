# isalpha() :returns True if the string consists of letters only and is not blank
kpop = "Ilikekpopmusic"
print( kpop.isalpha() )

#isalnum() - returns True if the string consists of numbers and letters and is not blank
password = "7538mary"
print( password.isalnum() )

#isdecimal() - returns True if the string contains only numeric characters
numbers = "123452"
print(numbers.isdecimal() )

#isspace() - returns True if the string contains only space,tabs or new lines
tabs = "        "
print( tabs.isspace() )

#istitle() - returns True if the string contains words that start with uppercase letters
title = "I Love Bts Music"
print( title.istitle() )
titles = "I Love BTS Music"
print( titles.istitle() )
