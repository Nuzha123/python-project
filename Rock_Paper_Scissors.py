import random
options = ["rock","paper","scissors"]
user_score=0
computer_score=0
print( 'This is a programme to play ROCK PAPER SCISSORS done by Nuzha Mashood and Fathima Sana\n')
print('Winning rules of the game is')
print('Rock vs Paper -> Paper Wins')
print('Rock vs Scissors -> Rock Wins')
print( 'Paper vs Scissors -> Scissors Wins\n')
i=1
c=int(input("How many times you want to play(no. of chances):"))


while i<=c:
    user = input("Enter a choice (rock,paper,scissors):")
    
    computer = random.choice(options)
    print(f"\nYou chose {user}, computer chose {computer}.")

    if user == computer:
        print(f"Both players selected {user}. Its a tie!")
    elif user == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! you got a point. ")
            user_score+=1
        else:
            print("Paper covers rock! Computer got a point.")
            computer_score+=1
    elif user == "paper":
        if computer == "rock":
            print("Paper covers rock! you got a point.")
            user_score+=1
        else:
            print("Scissors cuts paper! Computer got a point.")
            computer_score+=1 
    elif user == "scissors":
        if computer == "paper":
             print("Scissors cuts paper! you got a point.")
             user_score+=1
        else:
             print("Rock smashes scissors! Computer got a point")
             computer_score+=1
    i+=1
    
print("\nScore Board")
print("User score is ",user_score)
print("Computer score is ",computer_score)

if user_score == computer_score:
    print("Its a tie!!")
elif user_score > computer_score:
    print("\nCONGRATULATIONS!! You won the game")
else:
    print("\nYou lost the game. Better luck next time!!")
