#Basic Python programs

# 1) Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
name = input("Enter your name : ")
age = int(input("Enter your age : "))
num = int(input("Enter the number of times the o/p to be printed : "))
year = str((2017 - age)+100)
for n in range(num):
    
    print(name + " will be 100 years old in " + year)

# 2) Odd or even
    
num = int(input("Enter a number : "))
check = int(input("Enter a number : "))
if(num%2 == 0):
    print("The entered number number is even!!")
else:
    print("The entered number is odd!!")

if(num%4 ==0):
    print("The entered number is multiple of 4!!")
    
if(num%check ==0):
    print(check,"divides", num, "evenly!!")
    
else:
    print(check,"does not divide", num, "evenly!!")
    
# 3) List Less Than Ten
    
a = [1,1,2,3,5,8,13,21,34,55,89]
new_list = []
num = int(input("Enter a number : "))
for n in a:
    if(n<num):
        new_list.append(n)
        
print("The numbers in the list that are less than 10 are : ",new_list)

