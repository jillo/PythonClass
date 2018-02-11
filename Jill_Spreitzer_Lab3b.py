# Program for Lab Exercise 3 Part B        Jill Spreitzer           Feb 13, 2018

# This program calculates the monthly paycheck for salespeople, using
# a base salary along with conditional commissions and bonus amounts

# Declare constants for determining commission and bonus calculations

BASE_SALARY = 2000


# Get the salesperson's first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Get the sales amount
sales = int(input("Enter your monthly sales amount (whole numbers only): "))

# Get the number of vacation days taken in the last month
vacation_days = int(input("Enter how many vacation days you took in the last month (whole numbers only): "))

# Determine if deduction is required
if vacation_days > 3:
    deduction = True
    deducted_amount = 200

# Get the number of months the salesperson has been with the company
months_at_company = int(input("Enter the number of months you have been with the company: "))

# Determine the commission and bonus levels based on the sales amount and longevity with company

if sales > 1000000:
    bonus = 10000
    commission_rate = 0.35

elif sales >= 500001:
    bonus = 5000
    commission_rate = 0.28

elif sales >= 100001:
    bonus = 1000
    commission_rate = 0.15

elif sales >= 10000:
    bonus = 0
    commission_rate = 0.02

else:
    bonus = 0
    commission_rate = 0.00

# Determine if additional bonus will be paid
if months_at_company >= 60 and sales > 100000:
    additional_bonus = 1000    

# Print the paystub
# Print the salesperson's first and last name
print("Name:", first_name, last_name)

# Print the salesperson's longevity with the company
print("Longevity with company in months", months_at_company)

# Print the salesperson's base salary
print("Base Salary", BASE_SALARY)

# Print the salesperson's commission earned in dollars
# TESTING! STILL NEED TO FIX/CHANGE THIS TO THE FORMATTED AMOUNT, NOT THE RATE
print("Commission Rate", commission_rate)

# Print the salesperson's bonuses earned in dollars
# TESTING! STILL NEED TO FIX/CHANGE THIS TO FORMAT IT
print("Bonus Amount", bonus)

# Print the additional bonus amount
print("Additional Longevity Bonus", additional_bonus)


# Print the salesperson's deductions
print("Deduction for Vacation Days Taken", deducted_amount)

# Print the salesperson's total gross pay amount


