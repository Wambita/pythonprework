tuple_a = ["a","b","c","d"] #strings
tuple_b = [1,2,3,4,5] # numbers
tuple_c = [1,"west",34,"longitude"]#mixed
tuple_d = [["a","b","c","d"],[1,2,3,4,5],[1,"west",34,"longitude"]] #nested tuple

tuple_a.extend(tuple_b)#Joining tuple using extend() method
tuple_a.append("e") #adding values to a string
print(tuple_a) #prints both tuple a and b
print(tuple_b) # prints only tuple b

tuple_b.reverse() # reverse the tuple 
print(tuple_b) # prints reversed tuple b

#Sorting function it sorts from first to last
tuple_sort = [1,8,6,7,5,3,4,2]
print(tuple_sort)
tuple_sort.sort()

tuple_5 = ["h","f","g","a","c","b","e","d"]
tuple_5.sort()
print(tuple_5)