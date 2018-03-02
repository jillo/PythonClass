# Program for Lab Exercise 4a

# This program converts US measures to metric measures using input from a user,
# and validates that the input provided by the user matches specified parameters.
# The user has 3 tries per measurement to enter a valid value,
# after which the program will end.


# Declare minimum allowed values for each entry
MIN_MILES = 0
MAX_TEMP = 1000
MIN_GALLONS = 0
MIN_POUNDS = 0
MIN_INCHES = 0

# Declares the maximum number of attempts the user is allowed to enter valid data 
MAX_ATTEMPTS = 3

# Initialize the attempt_counter accumulator to 0
attempt_counter = 0

# Greet the user and get their name
name = input("Hello, what is your name? ")

# Say hi to the user and begin with the first question
print("\nHi", name, end=", ")

# Set the continue_program variable to true
continue_program = True

get_miles_input = True
get_temperature_input = True
get_gallons_input = True
get_pounds_input = True
get_inches_input = True

# Start the while loop to get the miles input from the user
while attempt_counter < MAX_ATTEMPTS and get_miles_input == True:

    # Ask the user how many miles are to be converted to kilometers
    miles = float(input("\nPlease tell me how many miles you want converted to " +
                        "kilometers, using positive numbers only: "))

    # This if-statement is the error handling
    # Check if the miles data entered is invalid, if so, start an attempt_counter
    # If the attempt_counter reaches 3, return error message and stop program
    if miles < MIN_MILES:

        # Set the attempt_counter accumulator to 1
        attempt_counter += 1

        if attempt_counter < MAX_ATTEMPTS:
            print("\nThe miles you entered is invalid, please try again; you have",
                  MAX_ATTEMPTS - attempt_counter, "more tries/try allowed.")
        else:
            print("\nYou have reached your maximum number of tries and",
                  "the program will now end.")

            # Set the continue_program variable to false to end the program
            continue_program = False

    else:
        # Convert the requested miles to kilometers and print the converted results, continue program
        milesToKm = miles * 1.6
        print("\n", name, end=", \n")
        print(miles, "miles is equal to", milesToKm, "kilometers.")

        # Set get_miles_input to false so that the while loop will exit and the
        # program will continue
        get_miles_input = False

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This begins the Fahrenheit-to-Celsius section of the program

# Check that the continue_program variable is true
if(continue_program == True):

    # Reset the attempt_counter accumulator to 0
    attempt_counter = 0

    # Start the while loop to get the temperature input from the user
    while attempt_counter < MAX_ATTEMPTS and get_temperature_input == True:
        
        # Ask the user what Fahrenheit temperature is to be converted to Celsius
        fahrenheitTemp = float(input("\nPlease tell me what Fahrenheit temperature " +
                                     "(up to 1000), you would like converted " +
                                     "to Celsius: "))

        # This if-statement is the error handling
        # Check if the temperature data entered is invalid, if so, start
        # an attempt_counter. If the attempt_counter reaches 3, return
        # error message and stop program
        if fahrenheitTemp > MAX_TEMP:
                
            # Set the attempt_counter accumulator to 1
            attempt_counter += 1

            if attempt_counter < MAX_ATTEMPTS:
                print("\nThe temperature you entered is invalid, please try again;",
                      "you have", MAX_ATTEMPTS - attempt_counter, "more tries/try allowed.")

            else:
                print("You have reached your maximum number of tries and",
                      "the program will now end.")
                
                # Set the continue_program variable to false to end the program
                continue_program = False

        else:
            # Convert the requested Fahrenheit temperature to Celsius and print the converted results, continue program
            fahrenheitToCelsius = (fahrenheitTemp -32) * 5/9
            print("\n", name, end=", \n")
            print(fahrenheitTemp, "degrees Fahrenheit is equal to",
                  fahrenheitToCelsius, "degrees Celsius.")

            
            # Set get_temperature_input to false so that the while loop will exit and the
            # program will continue
            get_temperature_input = False  

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This begins the gallons-to-liters  section of the program

# Check that the continue_program variable is true
if(continue_program == True):

    # Reset the attempt_counter accumulator to 0
    attempt_counter = 0

    # Start the while loop to get the gallons input from the user
    while attempt_counter < MAX_ATTEMPTS and get_gallons_input == True:

        # Ask the user how many gallons are to be converted to liters
        gallons = float(input("\nPlease tell me how many gallons " +
                              "you would like converted to liters, " +
                              "using positive numbers only: "))

        # This if-statement is the error handling
        # Check if the gallons data entered is invalid, if so, start
        # an attempt_counter. If the attempt_counter reaches 3, return
        # error message and stop program
        if gallons < MIN_GALLONS:
            
            # Set the attempt_counter accumulator to 1
            attempt_counter += 1

            if attempt_counter < MAX_ATTEMPTS:
                print("\nThe gallons you entered is invalid, please try again;",
                      "you have", MAX_ATTEMPTS - attempt_counter, "more tries/try allowed.")

            else:
                print("You have reached your maximum number of tries and " +
                      "the program will now end.")
                
                # Set the continue_program variable to false to end the program
                continue_program = False

        else:
            # Convert the requested gallons to liters and print the converted results, continue program
            gallonsToLiters = gallons * 3.9
            print("\n", name, end=", \n")
            print(gallons, "gallons is equal to", gallonsToLiters, "liters.\n")

            # Set get_gallons_input to false so that the while loop will exit and the
            # program will continue
            get_gallons_input = False

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This begins the pounds-to-kilograms section of the program

# Check that the continue_program variable is true
if(continue_program == True):

    # Reset the attempt_counter accumulator to 0
    attempt_counter = 0

    # Start the while loop to get the pounds input from the user
    while attempt_counter < MAX_ATTEMPTS and get_pounds_input == True:

        # Ask the user how many pounds are to be converted to kilograms
        pounds = float(input("Please tell me how many pounds you would like " +
                             "converted to kilograms, using positive numbers only: "))

        # This if-statement is the error handling
        # Check if the pounds data entered is invalid, if so, start
        # an attempt_counter. If the attempt_counter reaches 3, return
        # error message and stop program
        if pounds < MIN_POUNDS:
            
            # Set the attempt_counter accumulator to 1
            attempt_counter += 1

            if attempt_counter < MAX_ATTEMPTS:
                print("\nThe pounds you entered is invalid, please try again; you have",
                      MAX_ATTEMPTS - attempt_counter, "more tries/try allowed.")
            else:
                print("\nYou have reached your maximum number of tries and",
                  "the program will now end.")

                # Set the continue_program variable to false to end the program
                continue_program = False

        else:
            # Convert the requested pounds to kilograms and print the converted results, continue program
            poundsToKilograms = pounds * .45
            print("\n", name, end=", \n")
            print(pounds, "pounds is equal to", poundsToKilograms, "kilograms.\n")

            # Set get_pounds_input to false so that the while loop will exit and the
            # program will continue
            get_pounds_input = False

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This begins the inches-to-centimeters section of the program

# Check that the continue_program variable is true
if(continue_program == True):

    # Reset the attempt_counter accumulator to 0
    attempt_counter = 0

    # Start the while loop to get the inches input from the user
    while attempt_counter < MAX_ATTEMPTS and get_inches_input == True:

        # Ask the user how many inches are to be converted to centimeters
        inches = float(input("Please tell me how many inches you would like " +
                             "converted to centimeters, using positive numbers only: "))

        # This if-statement is the error handling
        # Check if the inches data entered is invalid, if so, start
        # an attempt_counter. If the attempt_counter reaches 3, return
        # error message and stop program
        if inches < MIN_INCHES:

            # Set the attempt_counter accumulator to 1
            attempt_counter += 1

            if attempt_counter < MAX_ATTEMPTS:
                print("\nThe inches you entered is invalid, please try again; you have",
                      MAX_ATTEMPTS - attempt_counter, "more tries/try allowed.")
            else:
                print("\nYou have reached your maximum number of tries and",
                  "the program will now end.")

                # Set the continue_program variable to false to end the program
                continue_program = False

        else:
            # Convert the requested inches to centimeters and print the converted results, continue program
            inchesToCentimeters = inches * 2.54
            print("\n", name, end=", \n")
            print(inches, "inches is equal to", inchesToCentimeters, "centimeters.\n")

            # Set get_inches_input to false so that the while loop will exit and the
            # program will continue
            get_inches_input = False
            

# Print a closing statement            
print("\nThank you for using Jill's converter program, Goodbye!") 
                  
