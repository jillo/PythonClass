# Guessing Game Program

# This program generates a random number and gives the user as many
# tries as it takes to guess the number (and tracks this number), giving
# the user feedback on their guesses to help them get closer and
# eventually guess the number.

import random


def main():

    get_name()

    start_game()

    # Print a closing statement
    print("\nThank you for playing Jill's number guessing game.  Goodbye!")


# Get the user's name, say Hello
def get_name():
    # Greet the user and get their name
    name = input("Hello, what is your name? ")

    # Say hi to the user and begin with the first question
    print("\nHi", name, end=", ")


def start_game():
    # Ask user if they would like to play a game, creating a variable to control the loop.
    keep_going = input('\n\nWould you like to play a game?\n(Enter "y" or "Y" for yes): ')

    # Start the guessing game with the user
    while keep_going == 'y' or keep_going == 'Y':

        # Initialize the guess_counter
        guess_counter = 0

        # Get a random integer
        number = random.randint(1,1000)

        # Tell user to guess a number
        guess = int(input('\nI am thinking of a whole number between ' +
                          '1 and 1000.  \nGuess what number I am thinking of! Enter your guess now:\n'))

        # Increase the guess_counter by 1
        guess_counter += 1

        while guess != number:

            if guess < number:
                if guess >= number - 10:
                    guess = int(input("You're getting warm but are a little too low.  Guess again! "))
                else:
                    guess = int(input('Too low, guess again! '))

            elif guess > number:
                if guess <= number + 10:
                    guess = int(input("You're getting warm but are a little too high.  Guess again! "))
                else:
                    guess = int(input('Too high, guess again! '))

            # Increase the guess_counter by 1
            guess_counter += 1

        print("Congratulations!  You guessed it!",
              "It only took you", guess_counter, "tries to guess the number.")

        # Ask if the user would like to play again
        keep_going = input('\nWould you like to play again? (Enter "y" or "Y" for yes):\n')


# Call the main function
main()
