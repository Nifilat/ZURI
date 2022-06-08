import random


while True:
    print("Welcome to a simple Rock-Paper-Scissors game\n")
    R = 'rock'
    P = 'paper'
    S = 'scissors'
    possible_choices = [R, P, S]

    print("R for Rock,\nP for paper, and\nS for scissors \n")
    user_choice = input(
        "Enter a choice: (R, P , S): ")
    if user_choice == 'R':
        users_choice = R
    elif user_choice == 'P':
        users_choice = P
    elif user_choice == 'S':
        users_choice = S

    if user_choice not in ('R', 'S', 'P'):
        print("Invalid Input, choose from the choices below:\n")
        continue

    else:
        computer_choice = random.choice(possible_choices)
        print("Computer chose " + computer_choice)
        print(f"Player ({users_choice}) : CPU ({computer_choice}).")

        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")

        elif user_choice == 'R':
            if computer_choice == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")

        elif user_choice == 'P':
            if computer_choice == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")

        elif user_choice == 'S':
            if computer_choice == 'paper':
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break
