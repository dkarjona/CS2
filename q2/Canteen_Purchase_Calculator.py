# Problem 1: The Canteen Purchase Calculator
def calculate_total(price, quantity):
    return price * quantity


def calculate_change(payment, total):
    return payment - total


price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
payment = float(input("Enter amount paid: "))

total = calculate_total(price, quantity)

result = calculate_change(payment, total)

print(f"Total Cost: PHP {total:.2f}")

if result >= 0:
    print(f"Change: PHP {result:.2f}")
else:
    print(f"Additional amount needed: PHP {-result:.2f}
    
# DOCUMENTATION QUESTIONS:

# 1. What does each function do?
# calculate_total() multiplies the price by the quantity.
# calculate_change() subtracts the total cost from the payment.

# 2. What is the difference between parameters and arguments?
# Parameters are the variable names inside a function definition, such as price and quantity. Arguments are the actual values passed when calling the function, such as 35 and 3.

# 3. Where is the returned total stored, and how is it reused?
# The returned total is stored in the variable 'total'.
# It is reused as an argument in calculate_change() and displayed as the total cost.

# 4. Why separate total calculation from change calculation?
# Separating the functions makes the program easier to read,test, debug, and maintain. Each function has one clear job.
