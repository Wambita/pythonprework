list_a = ["a","b","c","d"] #strings
list_b = [1,2,3,4,5] # numbers
list_c = [1,"west",34,"longitude"]#mixed
list_d = [["a","b","c","d"],[1,2,3,4,5],[1,"west",34,"longitude"]] #nested list

list_a.extend(list_b)#Joining list using extend() method
list_a.append("e") #adding values to a string
print(list_a) #prints both list a and b
print(list_b) # prints only list b

list_b.reverse() # reverse the list 
print(list_b) # prints reversed list b

#Sorting function it sorts from first to last
list_sort = [1,8,6,7,5,3,4,2]
print(list_sort)
list_sort.sort()

list_5 = ["h","f","g","a","c","b","e","d"]
list_5.sort()
print(list_5)

#call the module python3.6 list.py 


