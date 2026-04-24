import random

while True:
    worded = {"r": "rock", "p": "paper", "s": "scissors"}
    choice = input("Rock, paper, scissors? (r/p/s): ").lower()

    if choice not in ("r", "p", "s"):
        print("Invalid choice!")
        continue

    user = worded[choice]

    print(f"You chose {user}!")

    computer = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose {computer}!")

    if user == computer:
        print("It's a draw!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You win! 🎉")
    else:
        print("You lose! 😢")

    again = input("Play again? (y/n): ").lower()
    if again == "n":
        print("Thanks for playing!")
        break