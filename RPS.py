#Rock Papers Scissors Game

player_1 = input("Player 1 please enter rock, paper or scissor : ")
player_2 = input("Player 2 please enter rock, paper or scissor : ")

while True:
    
    if(player_1 == player_2):
            print("It's a TIE!!")
            
    elif(player_1 == "rock"):
        if(player_2 == "scissor"):
            print("Player 1 wins")
        else:
            print("Player 2 wins")
            
    elif(player_1 == "paper"):
        if(player_2 == "rock"):
            print("Player 1 wins")
        else:
            print("Player 2 wins")
            
    elif(player_1 == "scissor"):
        if(player_2 == "paper"):
            print("Player 1 wins")
        else:
            print("Player 2 wins")
            
    else:
        print("Invalid Input")
        
    if(input("Do you want to continue, yes or no?\n"))=="yes":
        player_1 = input("Enter rock, paper or scissor : ")
        player_2 = input("Enter rock, paper or scissor : ")
    
    else:
        print("Game over")
        break
    
        
