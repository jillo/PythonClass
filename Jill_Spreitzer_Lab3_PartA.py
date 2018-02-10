# Program for Lab Exercise 3
# This program converts US measures to metric measures using input from a user,
# and validates that the input provided by the user matches specified parameters

# Declare minimum allowed values for each entry
MIN_MILES = 0
MAX_TEMP = 1000
MIN_GALLONS = 0
MIN_POUNDS = 0
MIN_INCHES = 0

# Greet the user and get their name
name = input("Hello, what is your name? ")

# Say hi to the user and begin with the first question
print("\nHi", name, end=", ")

# Ask the user how many miles are to be converted to kilometers
miles = float(input("please tell me how many miles you want converted to kilometers, using positive numbers only: "))

# Check that the miles data entered is valid, if not, return error message and stop program
if miles >= MIN_MILES:

    # Convert the requested miles to kilometers and print the converted results, continue program
    milesToKm = miles * 1.6
    print("\n", name, end=", \n")
    print(miles, "miles is equal to", milesToKm, "kilometers.\n")

    # Ask the user what Fahrenheit temperature is to be converted to Celcius
    fahrenheitTemp = float(input("Please tell me what Fahrenheit temperature (up to 1000), you would like converted to Celcius: "))

    # Check that the temperature data entered is valid, if not, return error message and stop program
    if fahrenheitTemp <= MAX_TEMP:

        # Convert the requested Fahrenheit temperature to Celcius and print the converted results, continue program
        fahrenheitToCelcius = (fahrenheitTemp -32) * 5/9
        print("\n", name, end=", \n")
        print(fahrenheitTemp, "degrees Fahrenheit is equal to", fahrenheitToCelcius, "degrees Celcius.\n")

        # Ask the user how many gallons are to be converted to liters
        gallons = float(input("Please tell me how many gallons you would like converted to liters, using positive numbers only: "))

        # Check that the gallons data entered is valid, if not, return error message and stop program
        if gallons >= MIN_GALLONS:
            
            # Convert the requested gallons to liters and print the converted results, continue program
            gallonsToLiters = gallons * 3.9
            print("\n", name, end=", \n")
            print(gallons, "gallons is equal to", gallonsToLiters, "liters.\n")

            # Ask the user how many pounds are to be converted to kilograms
            pounds = float(input("Please tell me how many pounds you would like converted to kilograms, using positive numbers only: "))

            # Check that the pounds data entered is valid, if not, return error message and stop program
            if pounds >= MIN_POUNDS:

                # Convert the requested pounds to kilograms and print the converted results, continue program
                poundsToKilograms = pounds * .45
                print("\n", name, end=", \n")
                print(pounds, "pounds is equal to", poundsToKilograms, "kilograms.\n")

                # Ask the user how many inches are to be converted to centimeters
                inches = float(input("Please tell me how many inches you would like converted to centimeters, using positive numbers only: "))

                # Check that the inches data entered is valid, if not, return error message and stop program
                if inches >= MIN_INCHES:

                    # Convert the requested inches to centimeters and print the converted results, continue program
                    inchesToCentimeters = inches * 2.54
                    print("\n", name, end=", \n")
                    print(inches, "inches is equal to", inchesToCentimeters, "centimeters.\n")
                    
                    # Print a closing statement
                    print("Isn't this fun?!?")

                else:
                    print("The inches you entered is invalid and the program will now end. Goodbye!")

            else:
                print("The pounds you entered is invalid and the program will now end. Goodbye!")

        else:
            print("The gallons you entered is invalid and the program will now end. Goodbye!")
            
    else:
        print("The temperature you entered is invalid and the program will now end. Goodbye!")
        
else:
    print("The miles you entered is invalid and the program will now end. Goodbye!")






