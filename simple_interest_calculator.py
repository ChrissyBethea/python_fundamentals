"""
Simple Interest Calculator

This program asks the user for a principal amount, interest rate,
and time in years. It validates the user's input, calculates simple
interest, and displays the results.
"""

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


name = input("Enter your name: ").strip().title()

principal = get_number("Enter the principal amount: $")
rate = get_number("Enter the interest rate (%): ")
time = get_number("Enter the time in years: ")

interest = (principal * rate * time) / 100
total = principal + interest

name_length = len(name)
first_letter = name[0] if name else "N/A"

print(f"\nHello, {name}!")
print(f"Simple Interest: ${interest:.2f}")
print(f"Total Amount: ${total:.2f}")
print(f"Your name contains {name_length} characters.")
print(f"The first letter of your name is: {first_letter}")