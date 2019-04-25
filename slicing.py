#A slice statement is enclosed with [] square brackets and has two parts first is the position where to start slicing and second is the position to stop but not including that position.
greetings = 'Hello Moringa!'

part_one = greetings[0:5]
print(part_one)
part_two= greetings[6:14]
print(part_two)
part_ones= greetings[-15:-9]
print(part_ones)
#You can also use negative indexes when slicing.In this code we start slicing counting backwards and get Moringa as our output
part_twos= greetings[-8:-1]
print(part_twos)
#We can also choose not to specify the start or end point of our slices. In this example, Python assumes that we want to slice from index 0, to the last item and automatically fills in that value.
part_one = greetings[0:]
print(part_one)
#We can also slice lists .Here we did not specify the beginning of our slice and python automatically filled that in to be at index 0.
number = [1,2,3,4,5,7,6]
four_digits = number[:4]
print(four_digits)





