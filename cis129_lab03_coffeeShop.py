# Name: Saul Soria
# Assignment: cis129_lab03_coffeeShop.py
# Purpose: To create a coffee shop program that will calculate the total price of the
# order.

print("***************************************")
print("My Coffee and Muffin Shop")
# How many coffees and muffins are being bought.
numberofCoffeesBought = input("Number of coffees bought? ")
print(numberofCoffeesBought)
numberofMuffinsBought = input("Number of muffins bought? ")
print(numberofMuffinsBought)
print("***************************************\n")
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
# Using the string (numberofCoffeesBought) and converting it into an integer to retrieve
# how many coffees were bought and if the number is equal to 1, then the word "coffeee
# will be used. If the number is not 1, then the word "coffees" will be used."
if int(numberofCoffeesBought) == 1:
    coffee_number = "Coffee"
else:
    coffee_number = "Coffees"
# Using a function to pull the input of "numberofCoffeesBought" to determine the
# quantity of coffees purchased and then using {coffee_number} to retrieve the word
# "coffee" or "coffees" to be used in the print statement. int(numberofCoffeesBought) is
# used to convert the string to an integer which multiplies the integer by the price of
# the coffee (5) and :.2f is used to format the cost of the coffee(s) to include two
# decimal places.
print(f"{numberofCoffeesBought} {coffee_number} at $5 each: $ " +
    f"{int(numberofCoffeesBought) * 5:.2f}")
# Using the string (numberofMuffinsBought) and converting it into an integer to retrieve
# how many muffins were bought and if the number is equal to 1, then the word "muffin"
# will be used. If the number is not 1, then the word "muffins" will be used."
if int(numberofMuffinsBought) == 1:
    muffin_number = "Muffin"
else:
    muffin_number = "Muffins"
# Using a function to pull the input of "numberofMuffinsBought" to determine the
# quantity of muffins purchased and then using {muffin_number} to retrieve the word
# "muffin" or "muffins" to be used in the print statement. int(numberofMuffinsBought) is
# used to convert the string to an integer which multiplies the integer by the price of
# the muffin (4) and :.2f is used to format the cost of the muffin(s) to include two
# decimal places.
print(f"{numberofMuffinsBought} {muffin_number} at $4 each: $ " +
    f"{int(numberofMuffinsBought) * 4:.2f}")
# Gathering the total cost of the coffees and muffins and assigning them to total_cost.
total_cost = (int(numberofCoffeesBought) * 5) + (int(numberofMuffinsBought) *
                                                 4)
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
