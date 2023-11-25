def get_height():
    while True:
        height = input("Height: ")  # Prompt the user to enter the height
        if height.isdigit() and 1 <= int(height) <= 8:  # Check if the input is a positive integer between 1 and 8
            return int(height)  # Return the valid height
        else:
            print("Invalid input. Please enter a positive integer between 1 and 8.")  # Error message for invalid input


def print_pyramid(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "#" * i)  # Print spaces and hashes to form the half-pyramid


height = get_height()  # Get the valid height from the user
print_pyramid(height)  # Generate and print the half-pyramid
