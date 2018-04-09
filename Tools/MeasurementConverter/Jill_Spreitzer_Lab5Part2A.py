# Program for Lab Exercise 5b

# This program uses functions, and converts US measures to metric measures
# using input from a user, and validates that the input provided by the user
# matches specified parameters.
# The user has 3 tries per measurement to enter a valid value,
# after which the program will end.

import converter


def main():

    # Declare minimum allowed values for each entry
    min_miles = 0
    max_temp = 1000
    min_gallons = 0
    min_pounds = 0
    min_inches = 0

    # Declares the maximum number of attempts the user is allowed to enter valid data
    max_attempts = 3

    # Initialize the attempt_counter accumulator to 0
    attempt_counter = 0

    # Set the continue_program variable to true
    continue_program = True

    get_miles_input = True
    get_temperature_input = True
    get_gallons_input = True
    get_pounds_input = True
    get_inches_input = True

    # Greet the user and get their name
    name = input("Hello, what is your name? ")

    # Say hi to the user and begin with the first question
    print("\nHi", name, end=", ")

    # Start the while loop to get the miles input from the user
    while attempt_counter < max_attempts and get_miles_input == True:

        # Ask the user how many miles are to be converted to kilometers
        miles = float(input("\nPlease tell me how many miles you want converted to " +
                            "kilometers, using positive numbers only: "))

        # This if-statement is the error handling
        # Check if the miles data entered is invalid, if so, start an attempt_counter
        # If the attempt_counter reaches 3, return error message and stop program
        if miles < min_miles:

            # Add 1 to the attempt_counter
            attempt_counter += 1

            if attempt_counter < max_attempts:
                print("\nThe miles you entered is invalid, please try again; you have",
                      max_attempts - attempt_counter, "more tries/try allowed.")
            else:
                print("\nYou have reached your maximum number of tries and",
                      "the program will now end.")

                # Set the continue_program variable to false to end the program
                continue_program = False

        else:
            # Call the function that converts miles to kilometers, pass in the "miles" value, and
            # get the returned value
            print("\n", name, end=", \n")
            kilometers = converter.MilesToKm(miles)

            # Print the kilometers
            print(miles, "miles is equal to", kilometers, "kilometers.")

            # Set get_miles_input to false so that the while loop will exit and the
            # program will continue
            get_miles_input = False

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # This begins the Fahrenheit-to-Celsius section of the program

    # Check that the continue_program variable is true
    if continue_program == True:

        # Reset the attempt_counter accumulator to 0
        attempt_counter = 0

        # Start the while loop to get the temperature input from the user
        while attempt_counter < max_attempts and get_temperature_input == True:

            # Ask the user what Fahrenheit temperature is to be converted to Celsius
            fahrenheitTemp = float(input("\nPlease tell me what Fahrenheit temperature " +
                                         "(up to 1000), you would like converted " +
                                         "to Celsius: "))

            # This if-statement is the error handling
            # Check if the temperature data entered is invalid, if so, start
            # an attempt_counter. If the attempt_counter reaches 3, return
            # error message and stop program
            if fahrenheitTemp > max_temp:

                # Add 1 to the attempt_counter
                attempt_counter += 1

                if attempt_counter < max_attempts:
                    print("\nThe temperature you entered is invalid, please try again;",
                          "you have", max_attempts - attempt_counter, "more tries/try allowed.")

                else:
                    print("\nYou have reached your maximum number of tries and",
                          "the program will now end.")

                    # Set the continue_program variable to false to end the program
                    continue_program = False

            else:
                # Call the function that converts Fahrenheit temperature to Celsius, pass in the
                # "fahrenheitTemp" value, and get the returned value
                print("\n", name, end=", \n")
                celsius = converter.FahToCel(fahrenheitTemp)

                # Print the Celsius temperature
                print(fahrenheitTemp, "degrees Fahrenheit is equal to",
                      celsius, "degrees Celsius.")

                # Set get_temperature_input to false so that the while loop will exit and the
                # program will continue
                get_temperature_input = False

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # This begins the gallons-to-liters  section of the program

    # Check that the continue_program variable is true
    if (continue_program == True):

        # Reset the attempt_counter accumulator to 0
        attempt_counter = 0

        # Start the while loop to get the gallons input from the user
        while attempt_counter < max_attempts and get_gallons_input == True:

            # Ask the user how many gallons are to be converted to liters
            gallons = float(input("\nPlease tell me how many gallons " +
                                  "you would like converted to liters, " +
                                  "using positive numbers only: "))

            # This if-statement is the error handling
            # Check if the gallons data entered is invalid, if so, start
            # an attempt_counter. If the attempt_counter reaches 3, return
            # error message and stop program
            if gallons < min_gallons:

                # Add 1 to the attempt_counter
                attempt_counter += 1

                if attempt_counter < max_attempts:
                    print("\nThe gallons you entered is invalid, please try again;",
                          "you have", max_attempts - attempt_counter, "more tries/try allowed.")

                else:
                    print("\nYou have reached your maximum number of tries and " +
                          "the program will now end.")

                    # Set the continue_program variable to false to end the program
                    continue_program = False

            else:
                # Call the function that converts gallons to liters, pass in the "gallons" value,
                # and get the returned value
                print("\n", name, end=", \n")
                liters = converter.GalToLit(gallons)

                # Print the liters
                print(gallons, "gallons is equal to", liters, "liters.")

                # Set get_gallons_input to false so that the while loop will exit and the
                # program will continue
                get_gallons_input = False

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # This begins the pounds-to-kilograms section of the program

    # Check that the continue_program variable is true
    if (continue_program == True):

        # Reset the attempt_counter accumulator to 0
        attempt_counter = 0

        # Start the while loop to get the pounds input from the user
        while attempt_counter < max_attempts and get_pounds_input == True:

            # Ask the user how many pounds are to be converted to kilograms
            pounds = float(input("\nPlease tell me how many pounds you would like " +
                                 "converted to kilograms, using positive numbers only: "))

            # This if-statement is the error handling
            # Check if the pounds data entered is invalid, if so, start
            # an attempt_counter. If the attempt_counter reaches 3, return
            # error message and stop program
            if pounds < min_pounds:

                # Add 1 to the attempt_counter
                attempt_counter += 1

                if attempt_counter < max_attempts:
                    print("\nThe pounds you entered is invalid, please try again; you have",
                          max_attempts - attempt_counter, "more tries/try allowed.")
                else:
                    print("\nYou have reached your maximum number of tries and",
                          "the program will now end.")

                    # Set the continue_program variable to false to end the program
                    continue_program = False

            else:
                # Call the function that converts pounds to kilograms, pass in the "pounds" value,
                # and get the returned value
                print("\n", name, end=", \n")
                kilograms = converter.PoundsToKg(pounds)

                # Print the kilograms
                print(pounds, "pounds is equal to", kilograms, "kilograms.")

                # Set get_pounds_input to false so that the while loop will exit and the
                # program will continue
                get_pounds_input = False

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # This begins the inches-to-centimeters section of the program

    # Check that the continue_program variable is true
    if (continue_program == True):

        # Reset the attempt_counter accumulator to 0
        attempt_counter = 0

        # Start the while loop to get the inches input from the user
        while attempt_counter < max_attempts and get_inches_input == True:

            # Ask the user how many inches are to be converted to centimeters
            inches = float(input("\nPlease tell me how many inches you would like " +
                                 "converted to centimeters, using positive numbers only: "))

            # This if-statement is the error handling
            # Check if the inches data entered is invalid, if so, start
            # an attempt_counter. If the attempt_counter reaches 3, return
            # error message and stop program
            if inches < min_inches:

                # Add 1 to the attempt_counter
                attempt_counter += 1

                if attempt_counter < max_attempts:
                    print("\nThe inches you entered is invalid, please try again; you have",
                          max_attempts - attempt_counter, "more tries/try allowed.")
                else:
                    print("\nYou have reached your maximum number of tries and",
                          "the program will now end.")

                    # Set the continue_program variable to false to end the program
                    continue_program = False

            else:
                # Call the function that converts inches to centimeters, pass in "inches" value
                print("\n", name, end=", \n")
                centimeters = converter.InchesToCm(inches)

                # Print the centimeters
                print(inches, "inches is equal to", centimeters, "centimeters.")

                # Set get_inches_input to false so that the while loop will exit and the
                # program will continue
                get_inches_input = False

    # Print a closing statement
    print("\nThank you for using Jill's converter program. Goodbye!")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This is the end of the main function and
# begins the other function definitions




# Call the main function
main()
