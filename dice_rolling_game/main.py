import random

while True:
    choice = input("roll the dice? (y/n): ").lower()
    if choice == "y":
        dice_roll = random.randint(1, 6)
        print(f"You rolled a {dice_roll}!")
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Please enter 'y' or 'n'.")