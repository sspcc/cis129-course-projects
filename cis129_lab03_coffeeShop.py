# Name: Saul Soria
# Assignment: cis129_lab03_coffeeShop.py
# Purpose: To create a coffee shop program that will calculate the total price of the
# order.

print("***************************************")
print("My Coffee and Muffin Shop")
# How many coffees, muffins, cookies, and/or cookies are being bought.
numberofCoffeesBought = input("Number of coffees bought? ")
print(numberofCoffeesBought)
numberofMuffinsBought = input("Number of muffins bought? ")
print(numberofMuffinsBought)
numberofDonutsBought = input("Number of donuts bought? ")
print(numberofDonutsBought)
numberofCookiesBought = input("Number of cookies bought? ")
print(numberofCookiesBought)
print("***************************************\n")
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
# Using the string (numberofCoffeesBought) and converting it into an integer to retrieve
# how many coffees were bought and if the number is equal to 1, then the word "Coffee"
# will be used. If the number is not 1, then the word "Coffees" will be used."
if int(numberofCoffeesBought) == 1:
    coffee_number = "Coffee"
else:
    coffee_number = "Coffees"
# Using a function to pull the input of "numberofCoffeesBought" to determine the
# quantity of coffees purchased and then using {coffee_number} to retrieve the word
# "Coffee" or "Coffees" to be used in the print statement. int(numberofCoffeesBought) is
# used to convert the string to an integer which multiplies the integer by the price of
# the coffee (5) and :.2f is used to format the cost of the coffee(s) to include two
# decimal places.
print(f"{numberofCoffeesBought} {coffee_number} at $5 each: $ " +
    f"{int(numberofCoffeesBought) * 5:.2f}")
# Using the string (numberofMuffinsBought) and converting it into an integer to retrieve
# how many muffins were bought and if the number is equal to 1, then the word "Muffin"
# will be used. If the number is not 1, then the word "Muffins" will be used."
if int(numberofMuffinsBought) == 1:
    muffin_number = "Muffin"
else:
    muffin_number = "Muffins"
# Using a function to pull the input of "numberofMuffinsBought" to determine the
# quantity of muffins purchased and then using {muffin_number} to retrieve the word
# "Muffin" or "Muffins" to be used in the print statement. int(numberofMuffinsBought) is
# used to convert the string to an integer which multiplies the integer by the price of
# the muffin (4) and :.2f is used to format the cost of the muffin(s) to include two
# decimal places.
print(f"{numberofMuffinsBought} {muffin_number} at $4 each: $ " +
    f"{int(numberofMuffinsBought) * 4:.2f}")
# Using the string (numberofDonutsBought) and converting it into an integer to retrieve
# how many donuts were bought and if the number is equal to 1, then the word "Donut"
# will be used. If the number is not 1, then the word "Donuts" will be used."
if int(numberofDonutsBought) == 1:
    donut_number = "Donut"
else:
    donut_number = "Donuts"
# Using a function to pull the input of "numberofDonutsBought" to determine the
# quantity of donuts purchased and then using {donut_number} to retrieve the word
# "Donut" or "Donuts" to be used in the print statement. int(numberofDonutsBought) is
# used to convert the string to an integer which multiplies the integer by the price of
# the donut (3) and :.2f is used to format the cost of the donut(s) to include two
# decimal places.
print(f"{numberofDonutsBought} {donut_number} at $3 each: $ " +
    f"{int(numberofDonutsBought) * 3:.2f}")
# Using the string (numberofCookiesBought) and converting it into an integer to retrieve
# how many coffees were bought and if the number is equal to 1, then the word "Cookie"
# will be used. If the number is not 1, then the word "Cookies" will be used."
if int(numberofCookiesBought) == 1:
    cookie_number = "Cookie"
else:
    cookie_number = "Cookies"
# Using a function to pull the input of "numberofCookiesBought" to determine the
# quantity of coffees purchased and then using {cookie_number} to retrieve the word
# "Coookie" or "Cookies" to be used in the print statement. int(numberofCookiesBought)
# is used to convert the string to an integer which multiplies the integer by the price
# of the coffee (1) and :.2f is used to format the cost of the coffee(s) to include two
# decimal places.
print(f"{numberofCookiesBought} {cookie_number} at $1 each: $ " +
    f"{int(numberofCookiesBought) * 1:.2f}")
# Gathering the total cost of the coffees, muffins, donuts and cookies and assigning
# them to total_cost.
total_cost = (int(numberofCoffeesBought) * 5) + (int(numberofMuffinsBought) * 4
    + (int(numberofDonutsBought) * 3) + (int(numberofCookiesBought) * 1))
# Gathering the input from total_cost and multiplying it by .06 (the current tax rate)
# to get the tax amount. This value is assigned to the word tax and it is then formatted
# it to include two decimal places.
tax = total_cost * 0.06
formatted_tax = "%.2f" % tax
# Printing the tax amount on the receipt
print("6% tax: $ " + formatted_tax)
print("---------")
# Printing the total cost of the coffees and muffins including tax formatted to include
# two decimal places.
print(f"Total: $ {total_cost + tax:.2f}")
print("***************************************")
