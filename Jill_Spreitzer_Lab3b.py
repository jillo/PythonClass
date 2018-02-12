# Program for Lab Exercise 3 Part B        Jill Spreitzer           Feb 13, 2018

# This program calculates the monthly paycheck for salespeople, using
# a base salary along with conditional commissions and bonus amounts

# Declare constants for determining commission and bonus calculations

BASE_SALARY = 2000


# Get the salesperson's first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Get the sales amount
sales = int(input("Enter your monthly sales amount (whole numbers only, no punctuation): "))

# Get the number of vacation days taken in the last month
vacation_days = int(input("Enter how many vacation days you took in the last month (whole numbers only): "))

# Determine if deduction is required
if vacation_days > 3:
    deduction = True
    deducted_amount = 200
else:
    deduction = False
    deducted_amount = 0

# Get the number of months the salesperson has been with the company 
months_at_company = int(input("Enter the number of months you have been with the company: ")) 

# Determine if salesperson is elible for the bonus
if months_at_company >= 3:
    bonus = True
else:
    bonus = False

# Determine the commission and bonus levels based on the sales amount and longevity with company
if sales > 1000000:
    commission_rate = 0.35
    if bonus == True:
        bonus_amount = 10000
    else:
        bonus_amount = 0

elif sales >= 500001:
    commission_rate = 0.28
    if bonus == True:
        bonus_amount = 5000
    else:
        bonus_amount = 0    

elif sales >= 100001:
    commission_rate = 0.15
    if bonus == True:
        bonus_amount = 1000
    else:
        bonus_amount = 0

elif sales >= 10000:    # Sales of $100,000 or under do not get a bonus 
    commission_rate = 0.02
    bonus_amount = 0

else:
    commission_rate = 0.00
    bonus_amount = 0

# Calculate commission amount earned
commission = sales * commission_rate

# Determine if additional bonus will be paid
if months_at_company >= 60 and sales > 100000:
    additional_bonus = True
    additional_bonus_amount = 1000
else:
    additional_bonus = False
    additional_bonus_amount = 0

# Calculate total gross pay
total_gross_pay = BASE_SALARY + commission + bonus_amount + additional_bonus_amount - deducted_amount

# Print the paystub
# Print the salesperson's first and last name
print("\n\nName of Salesperson\t\t\t\t", first_name,  " ", last_name, sep='')

# Print the salesperson's longevity with the company
print("\nLongevity with company in months\t\t", months_at_company, sep='')

# Print the salesperson's base salary
print("\nBase Salary\t\t\t\t\t$", format(BASE_SALARY, ',.2f'),sep='')

# Print the salesperson's earned commission rate
print("\nCommission Rate\t\t\t\t\t", format(commission_rate, '.0%'),sep='')

# Print the salesperson's commission earned in dollars
print("\nCommission Earned\t\t\t\t$", format(commission, ',.2f'),sep='')

# Print the salesperson's bonus amount earned in dollars
print("\nBonus Amount Earned\t\t\t\t$", format(bonus_amount, ',.2f'),sep='')

# Print the additional bonus amount
if additional_bonus == True:
    print("\nAdditional Longevity Bonus Earned\t\t$", format(additional_bonus_amount, ',.2f'),sep='')

# Print the salesperson's deductions
if deduction == True:
    print("\nDeduction for Vacation Days Taken\t\t$", format(deducted_amount, ',.2f'),sep='')

# Print the salesperson's total gross pay amount
print("\nTotal Gross Pay\t\t\t\t\t$", format(total_gross_pay, ',.2f'),sep='')

