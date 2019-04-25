'''
in a team of members 20, some numbers are taken 
and want to display the numbers that are not taken
so others don't pick the picked numbers
'''

# taken numbers 
numTaken = [3,5,7,11,13]

print("Available numbers")

#loop
for i in range (1,21):
    if i in numTaken:
        continue
    print(i)
#We want to print numbers from 1-20, but skip over the numbers in the numTaken list. We've written a standard for loop, with a twist. If the current number i is in the numTaken list, the print() statement directly under the continue is not executed. This is because every time continue is called, Python jumps back up to the top of the loop.