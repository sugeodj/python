amount = -1

# Prompt the user to enter the amount owed in dollars
while amount < 0:
    try:
        amount = float(input("Enter amount owed (in dollars): "))
        if amount < 0:
            print("Invalid input. Please enter a non-negative number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

cents = int(amount * 100)  # Convert the amount to cents

coins = 0

coins += cents // 25  # Calculate the number of quarters and update the remaining cents
cents %= 25

coins += cents // 10  # Calculate the number of dimes and update the remaining cents
cents %= 10

coins += cents // 5  # Calculate the number of nickels and update the remaining cents
cents %= 5

coins += cents  # Add the remaining cents as pennies

print(coins)  # Print the total number of coins required
