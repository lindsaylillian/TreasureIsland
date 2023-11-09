print("WELCOME TO OUR TREASURE ISLAND GAME")
print("Your mission is to find the treasure")
question1 = input("You are at a crossroad. What direction would you like to go? Type 'left' or 'right': ")

if question1.lower() == "left":  # Use .lower() to make the input case-insensitive
    choice2 = input("You've reached a lake. Do you want to swim or wait for a boat? ")

    if choice2.lower() == "wait":  # Use .lower() to make the input case-insensitive
        choice3 = input("You've waited for the boat, and now you're across the lake. You see a lion. Do you want to 'shoot' or 'run'? ")

        if choice3.lower() == "shoot":  # Use .lower() to make the input case-insensitive
            print("Congratulations, you win!")
        else:
            print("You lose the game.")
    else:
        print("You lose the game.")
else:
    print("You've lost the game.")
