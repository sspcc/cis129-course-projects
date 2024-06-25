# Saul Soria
# 06/23/24
# Program calculating the total payout of bottles collected at a store throughout a given week.
# Lab 5 The Bottle Return Program
total_bottles = 0
total_payout = 0
keep_going = "y"

while keep_going == "y":
    # Begins each week with 0 bottles.
    total_bottles = 0

    # The number of days the bottles will be collected for (7).
    NBR_OF_DAYS = 7
    for day in range(1, NBR_OF_DAYS + 1):
        today_bottles = int(
            input(f"Enter number of bottles returned for day #{day}: "))
        total_bottles += today_bottles

    # Calculates the payout.
    PAYOUT_PER_BOTTLE = 0.10
    total_payout = total_bottles * PAYOUT_PER_BOTTLE

    # Prints results
    print(f"Total number of bottles collected: {total_bottles}")
    print(f"Total payout amount: ${total_payout:.2f}")

    # Prompt user to continue or end program
    keep_going = input(
        "Do you want to enter another week’s worth of data? (Enter y or n): ")
