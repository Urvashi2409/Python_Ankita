
# list slicing 
# print(mylist[6])

# end point is not included 

# print(mylist[start: end: steps])
# print(mylist[2:5])

# print(mylist[-1])

# print(mylist[-4:-1])

# print(mylist[-4:])

# 4,3,12 

# print(mylist[2::-1])

# 7,9,11 

# print(mylist[5:10:2])

# p, 10, 6 


# print(mylist[12:3:-4])

# print(mylist[::-1])

# print(mylist[:-7])

# 12, 6, 10, p 
# print(mylist[0:13:4])

# list functions  

# lists are mutable  = you can change them 
# mylist = [12, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, "Python", "p", 0.8, True]
# 1. add something in  list : at the end of list  = append
# mylist.append(3)
# insert function: takes index and value 
# mylist.insert(4, 14) 
# update 
# mylist[2] = 3
# works on value 
# mylist.remove("Python")
# works on indexes 
# mylist.pop(3)

# if nothing then last 
# mylist.pop()
# mylist.reverse()


# mylist.sort(reverse=True)
# print(mylist)

# print(mylist.count(12))

# mylist2 = [9,9,9,9,9]

# mylist.extend(mylist2)
# print(mylist)

# mylist.clear()

# values are copied 
# newlist = mylist.copy()
# print(newlist)

# mylist[3] = 20
# print(mylist)
# print(newlist)

# newlist = mylist
# mylist[3] = 20
# print(mylist)
# print(newlist)
# print(newlist)

mylist = [12, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 12,3, [23, 45, 67]]

# del mylist 
# del mylist[0]

print(mylist[-1][1])