import random
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper" "scissor"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou  chose{user_action}, computer  chose {computer_action}.\n" )

    if user_action == computer_action:
            print(f"Both players selected{user_action}. It's a tie!")
    elif user_action == "rock":
       if computer_action == "scissors":
            print("Rock beats scissors! You win!")
       else:
            print("paper beats rock! You lose.")
    elif    user_action == "paper":
       if computer_action == "rock":
            print("paper covers rock! You win!")
       else:    
            print("scissors cuts papper! You lose.")
    elif user_action == "scissors":
       if computer_action == "paper":
            print("scissors cuts paper! you win")
       else: 
            print("rock smashes scissors! you lose!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
    
            


