# This file contains the functions that perform measurement conversions


def MilesToKm(miles):
    # Convert the requested miles to kilometers and print the converted results
    milesToKm = miles * 1.6
    return milesToKm


def FahToCel(fahrenheitTemp):
    # Convert the requested Fahrenheit temperature to Celsius and print the converted results
    fahrenheitToCelsius = (fahrenheitTemp - 32) * 5 / 9
    return fahrenheitToCelsius


def GalToLit(gallons):
    # Convert the requested gallons to liters and print the converted results
    gallonsToLiters = gallons * 3.9
    return gallonsToLiters


def PoundsToKg(pounds):
    # Convert the requested pounds to kilograms and print the converted results
    poundsToKilograms = pounds * .45
    return poundsToKilograms


def InchesToCm(inches):
    # Convert the requested inches to centimeters and print the converted results
    inchesToCentimeters = inches * 2.54
    return inchesToCentimeters