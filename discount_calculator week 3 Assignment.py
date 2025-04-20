# Function to calculate the final price after applying the discount
def calculate_discount(price, discount_percent):
    # If the discount percentage is 20% or higher, apply the discount
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount  # Calculate the final price after discount
        return final_price
    else:
        return price  # If the discount is less than 20%, return the original price

# Ask the user to enter the original price and discount percentage
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the result
print(f"The final price is: {final_price}")
