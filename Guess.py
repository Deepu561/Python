#Guess the number game
import random

print("Guess the number\n")
n = int(input("Enter the number of your guess\n:"))
num = random.randint(1,9)
count = 0
while True:
    
    count += 1
    
    if(num == n):
        print("Right Guess!!!\n")
    elif(num > n):
        print("Too low\n")
    elif(num < n):
        print("Too High\n")
        
    if(input("Do you want to exit\n")) != "exit":
        n = int(input("Enter the number of your guess\n:"))
        
    else:
        print("Game Over\n")
        break
print("The number of guess taken by user are\n",count)


