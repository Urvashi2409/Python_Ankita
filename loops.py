# for loops  
# while loops  
# 1 till 10 

# for i in range(1, 11):
#     print(i, end="/")

# multiplication table of 3 using for loop 
# for i in range(1, 11):
#     result = 3*i 
#     print(f"3*{i} = {result}")


# for i in range(1, 11):
#     print(i)

# print(i)

# for i in range(1, 11):
#     x = 34
#     print(x + i)

# print(x)

# num = int(input("Enter a number "))
# isprime = True 
# for i in range(2, num):
#     if num != i and num % i == 0:
#         isprime = False 

# if isprime == True:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

# Q: print all the prime numbers present upto a particular number  
# num = int(input("Enter a number "))

# # nested for loops 
# for i in range(1, num+1):
#     isprime = True 
#     for j in range(2, i):
#         if i != j and i % j == 0:
#             isprime = False 
#     if isprime == True:
#         print(f"{i} is a prime number") 
#     else:
#         print(f"{i} is not a prime number")       


# Q. Ask the user about number till which he wants the multiplication tables and also till what number they want upto what digit 
# num1 = int(input("Enter the number till which you want the multiplication tables"))
# num2 = int(input("Enter the number till which you want to multiply"))

# # num1 = upto which number we want multiplication tables 
# # num2 = upto what number we should multiply vertically 

# for i in range(2, num1+1):
#     for j in range(1, num2+1):
#         result = i * j 
#         print(f"{i} * {j} = {result}")
#     print("*" * 8)

# for loop for list, string , tuples 

mylist = [1,2,3,4,4]
# len(mylist)

# for i in range(len(mylist)):
#     print(mylist[i])

# for i in mylist: 
#     print(i)
