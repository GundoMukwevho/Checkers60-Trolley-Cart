# Checkers360 App.

# Dictionary for the shopping cart


shopping_trolleycart = {}


# Here is where we defiine and create a function to add items to the shopping cart :

def add_item(): 

    item_name = input ("Enter the item name: ").capitalize()

    
    try:
        price = float(input(f"Enter the price for {item_name}: "))
        quantity = int(input(f"Enter the quantity for {item_name}: "))

# Using an exception handling for if the incorrect input format is submitted
    except ValueError:
    
        print("Invalid input! Price must be in numbers and or quantity must be an integer.")
        return
    
    if item_name in shopping_trolleycart:

        shopping_trolleycart[item_name]["quantity"] += quantity

        print(f"Updated {item_name}, new quantity: {shopping_trolleycart[item_name]['quantity']}")
    else:
        shopping_trolleycart[item_name] = {"price": price, "quantity": quantity}
        print(f"{item_name} has been added to the cart.")

# This is where I am defining and creating a function to display cart contents


def view_cart():
    
    if not shopping_trolleycart:
        
        print("The cart is empty.")
        
        
        return
    
    print("\n--- Your cart contents: ---\n")
    total_cost = 0
    
    for item, details in shopping_trolleycart.items():
        item_total = details["price"] * details["quantity"]
        total_cost += item_total
        
        
        print(f"{item}:\t Price = R{details['price']:.2f}, "
              f"Quantity = {details['quantity']}, "
              f"Total = R{item_total:.2f}")
    print(f"---------------------\nCart Total = R{total_cost:.2f}")
    

# This is where we are defining and creating a function to calculate and display total

def calculate_total():
    total = sum(details["price"] * details["quantity"] for details in shopping_trolleycart.values())
    print(f"\nTotal value of cart = R{total:.2f}")

# Main program loop
def main():
    while True:
        print("\n--- Checkers360 Shopping Cart ---")
        print("\n1. Add item")
        print("\n2. View cart")
        print("\n3. Calculate total")
        print("\n4. Checkout and Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("Checking out... Thank you for shopping at Checkers!")
            break
        else:
            print("Invalid choice. Please select between 1-4.")

# Run program
if __name__ == "__main__":
    main()
#1234