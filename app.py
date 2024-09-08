# Ask user's name
Name = input("What is your name? ")

# For the type of application the user wants to use
ask_you_the_type_of_application_needed = input("\n\nWhat type of application do you need? (Calculator, Age Checker, String Manipulator, and a Quiz app.): ").lower()

# Calculator App
if ask_you_the_type_of_application_needed == "calculator":
    print(f"Welcome To the calculator app, {Name}!")
    a = float(input("Enter the first number: ")) 
    b = float(input("Enter the second number: ")) 
    which_operation = input("Which operation do you want to perform? (addition, subtraction, multiplication, division, exponential, square roots, modulus): ").lower()

    # Perform the chosen operation
    if which_operation == "addition".lower():
        result = a + b
        print(f"The sum of {a} and {b} is {result}")
    elif which_operation == "subtraction".lower():
        result = a - b
        print(f"The difference between {a} and {b} is {result}")
    elif which_operation == "multiplication":
        result = a * b
        print(f"The product of {a} and {b} is {result}")
    elif which_operation == "division":
        if b != 0:
            result = a / b
            print(f"The quotient of {a} and {b} is {result}")
        else:
            print("Error! Division by zero is not allowed.")
    elif which_operation == "exponential":
        result = a ** b
        print(f"The result of {a} raised to the power of {b} is {result}")
    elif which_operation == "square roots":
        result = a ** 0.5
        print(f"The square root of {a} is {result}")
    elif which_operation == "modulus":
        result = a % b
        print(f"The remainder of {a} divided by {b} is {result}")
    else:
        print(f"Sorry {Name}, that operation is not supported.")

# Age Checker App
elif ask_you_the_type_of_application_needed == "age checker":
    print(f"Welcome to the age checker app, {Name}!")
    how_old_are_you = int(input("Enter your age: "))
    if how_old_are_you <= 12:
        print(f"You are still a child, {Name}!")
    elif how_old_are_you <= 18:
        print(f"You are a teenager, {Name}!")
    elif how_old_are_you <= 60:
        print(f"You are an adult, {Name}!")
    else:
        print(f"You are a senior citizen, {Name}!")
        print("Invalid input! Please enter a valid age.")
        
# String Manipulator App
elif ask_you_the_type_of_application_needed == "string manipulator":
    print(f"Welcome to the string manipulator app, {Name}!")

    # Ask the user what typw of converstion they want to perform
    choice = input("Which function do you want to use? (upper, lower, reverse letter, length): ").lower()

    word = input(f"Enter a word, {Name}: ")

    # code logic for performing the operation
    if choice == "upper":
        print(f"The uppercase of {word} is {word.upper()}")
    elif choice == "lower":
        print(f"The lowercase of {word} is {word.lower()}")
    elif choice == "reverse letter":
        reversed_string = word[::-1]
        print(f"The reversed string of {word} is {reversed_string}")
    elif choice == "length":
        print(f"The length of the word '{word}' is {len(word)}")
    else:
        print("Invalid option selected.")

# Quiz App
elif ask_you_the_type_of_application_needed == "quiz app":
    print("Welcome to the Quiz app!")
    print("Please choose from the following options:")
    print("1. Take a Quiz")
    print("2. Exit")

    # Ask the user to choose an option
    option = input("Enter the number of your choice: ").strip()

    if option == "1":
        #variable to store score
        score = 0
        print("\nQuiz Time!")
        print("Answer the following questions:")

        # Question 1
        print("\n1. How many days do we do programming in a week for Danu Breed class?")
        answer = input("(a) 1\n(b) 10\n(c) 2\nYour answer: ").strip().lower()
        if answer == 'c':
            score += 1
            print("Correct!")
        else:
            print("Wrong! The correct answer is 2.")

        # Question 2
        print("\n2. How many days are there in a week?")
        answer = input("(a) 4\n(b) 6\n(c) 7\nYour answer: ").strip().lower()
        if answer == 'c':  # The correct answer is 'c'
            score += 1
            print("Correct!")
        else:
            print("Wrong! The correct answer is 'c' (7).")
            
        # Total score
        print(f"\nYour final score is: {score}/2")
        if score == 2:
            print("Excellent! You got all the answers right!")
        elif score == 1:
            print("Good job! You got 1 out of 2 right.")
        else:
            print("Better luck next time. You got none right.")

    elif option == "2":
        print("Goodbye! Have a great day!")
    else:
        print("Invalid option. Please restart the program and choose a valid option.")

# picks none of the listed apps
else:
    print(f"Please enter one of the following apps: Calculator, Age Checker, String Manipulator, or Quiz App, {Name}")

# Project: Treasure Island Game

#Ask user for name
name = input("What is your name? ")
print(f"Welcome to the Treasure Island Game, {name}!")
#instructions
print("Your mission is to find the treasure.")
print("You are at a crossroad. Where do you want to go?")

#Ask user for choice
choice = input("Type 'left' or 'right': ").lower()
#If user chooses left
if choice == "left":
    print("You come to a lake. There is an island in the middle of the lake.")
    print("Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    choice = input("What do you choose? ").lower()
    if choice == "wait":
        print("You arrive at the island unharmed.")
        print("There is a house with 3 doors. One red, one yellow, and one blue.")
        choice = input("Which color do you choose? Type 'red', 'yellow', or 'blue': ").lower()
        if choice == "yellow":
            print("You enter a room of beasts. Game Over.")
        elif choice == "red":
            print("You found the treasure! You win!")
        elif choice == "blue":
            print("It's a room full of fire. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
#If user chooses right
else:
    print("You fell into a hole. Game Over.")
