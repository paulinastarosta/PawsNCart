# A list of dictionaries representing available stock in the store, each item with its name and price
stock_list = [
    {"item": "Cat Food", "price": 25.75},
    {"item": "Cat Treat", "price": 4.50},
    {"item": "Cat Toy", "price": 5.50},
    {"item": "Cat Bed", "price": 29.99},
    {"item": "Cat Bowl", "price": 4.50},
    {"item": "Dog Food", "price": 69.50},
    {"item": "Dog Treat", "price": 4.35},
    {"item": "Dog Toy", "price": 7.50},
    {"item": "Dog Bed", "price": 45.99},
    {"item": "Dog Bowl", "price": 5.50},
]

# Initialize an empty list to store the items added to the cart
cart = []

# A boolean flag to control the loop for the user interface
done = False

# Initial greeting message printed to the user
print("Welcome to Paws n Cart!")
print("\n")  # Adding a blank line for better readability

# Main program loop that runs until 'done' is set to True
while not done:
    print("-" * 80)  # Print a separator for better readability
    print("This is your shopping cart")
    # Calculate the total price of the items in the cart
    total_price = sum(item['price'] * item['quantity'] for item in cart) if cart else 0
    # Iterate over each item in the cart and print its details
    for item in cart:
        print(f"Item: {item['item']:15} Price: £{item['price']:.2f} Quantity: {item['quantity']}")
    # Inform the user if the cart is empty
    print("Your cart is empty.") if not cart else None
    print(f"Total price: £{total_price:.2f}")
    print("-" * 80)
    print("\nWould you like to: ")
    # Print options for the user to select from
    print("1. See a full range of our stock")
    print("2. Add an item(s) to your cart")
    print("3. Remove item(s) from your cart")
    print("4. Checkout")

    # Input to choose an option
    choice = input("Please enter the number of the option you would like to choose:\n")

    if choice == "1":
        # If the user wants to see the full range of stock
        for item in stock_list:
            print(f"Item: {item['item']:15} Price: £{item['price']:.2f}")
    elif choice == "2":
        # Option to add items to the cart
        item_name = input("What item would you like to add to your cart: ").strip().lower()
        found = False
        for available_item in stock_list:
            if available_item['item'].lower() == item_name:
                quantity = int(input(f"How many {available_item['item']} would you like to add? "))
                if quantity > 0:
                    for cart_item in cart:
                        if cart_item['item'] == available_item['item']:
                            cart_item['quantity'] += quantity
                            found = True
                            break
                    if not found:
                        cart.append({'item': available_item['item'], 'price': available_item['price'], 'quantity': quantity})
                    print(f"{quantity} {available_item['item'].capitalize()}(s) have been added to your basket!")
                    found = True
                else:
                    print("Please enter a valid quantity.")
                break
        if not found:
            print("Sorry, that item is not available.")
    elif choice == "3":
        # Option to remove items from the cart
        if cart:
            remove_item = input("Which item would you like to remove from your cart: ").strip().lower()
            found = False
            for cart_item in cart:
                if cart_item['item'].lower() == remove_item:
                    quantity_to_remove = int(input(f"How many {cart_item['item']} would you like to remove? "))
                    if quantity_to_remove > 0 and quantity_to_remove <= cart_item['quantity']:
                        if quantity_to_remove == cart_item['quantity']:
                            cart.remove(cart_item)
                        else:
                            cart_item['quantity'] -= quantity_to_remove
                        print(f"{quantity_to_remove} {cart_item['item'].capitalize()}(s) have been removed from your basket!")
                        found = True
                    else:
                        print("Please enter a valid quantity to remove.")
                    break
            if not found:
                print("Item not found in your cart!")
        else:
            print("Your cart is already empty.")
    elif choice == "4":
        # Checkout and end the session
        print("Thank you for shopping at Paws N Cart")
        done = True
    else:
        # Input validation for an incorrect menu option
        print("That is not a valid option.")
