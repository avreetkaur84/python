from datetime import datetime

# Define menu categories and their items
categories = {
    'Drink': [],
    'Cake': [],
    'Fast Food': [],
    'Ice Cream': [],
    'Salad': [],
    'Soup': [],
}
orders = []
total_sales = 0

# Helper functions for printing
def print_title(title):
    print("\n=== " + title.upper() + " ===")

def print_error(message):
    print("Error: " + message)

def print_success(message):
    print(message)

# Function to add menu items
def add_menu_item():
    while True:
        print_title("Select Category:-")
        print("\n1 --> Drink\n2 --> Cake\n3 --> Fast Food\n4 --> Ice Cream\n5 --> Salad\n6 --> Soup\n7 --> Done\n")
        category_input = input("Enter your category --> ").strip()

        if category_input == '7':
            break

        category_dict = {
            '1': 'Drink',
            '2': 'Cake',
            '3': 'Fast Food',
            '4': 'Ice Cream',
            '5': 'Salad',
            '6': 'Soup'
        }

        category = category_dict.get(category_input)

        if not category:
            print_error("Invalid category selection.")
            continue

        item = input("Enter item name for " + category + " (or 'done' to finish) --> ").strip().title()
        if item.lower() == 'done':
            break

        price_input = input("Enter price for " + item + " --> Rs ").strip()
        quantity_input = input("Enter quantity available for " + item + " --> ").strip()

        if price_input.replace('.', '', 1).isdigit() and quantity_input.isdigit():
            price = float(price_input)
            quantity = int(quantity_input)
            categories[category].append({'item': item, 'price': price, 'quantity': quantity})
            print_success("Item '" + item + "' added to " + category + " with " + str(quantity) + " quantity.\n")
        else:
            print_error("Invalid price or quantity. Please enter a valid number.")

# Function to remove a menu item
def remove_menu_item():
    while True:
        print_title("Remove Menu Item")
        category_input = input("Select a category to remove item from (1-6) or 'done' to finish --> ").strip()
        if category_input.lower() == 'done':
            break

        category_dict = {
            '1': 'Drink',
            '2': 'Cake',
            '3': 'Fast Food',
            '4': 'Ice Cream',
            '5': 'Salad',
            '6': 'Soup'
        }

        category = category_dict.get(category_input)

        if not category or category not in categories:
            print_error("Invalid category selection.")
            continue

        menu = categories[category]
        if not menu:
            print_error("No items found in this category.")
            continue

        display_menu()  # Show current menu
        item_number_input = input("Select the item number to remove --> ").strip()

        if item_number_input.isdigit():
            item_number = int(item_number_input)

            if item_number < 1 or item_number > len(menu):
                print_error("Invalid item number.")
                continue

            removed_item = menu.pop(item_number - 1)
            print_success("Item '" + removed_item['item'] + "' removed from the menu.")
        else:
            print_error("Invalid item number.")

# Function to restock menu items
def restock_item():
    while True:
        print_title("Restock Menu Item")
        category_input = input("Select a category to restock item from (1-6) or 'done' to finish --> ").strip()

        if category_input.lower() == 'done':
            break

        category_dict = {
            '1': 'Drink',
            '2': 'Cake',
            '3': 'Fast Food',
            '4': 'Ice Cream',
            '5': 'Salad',
            '6': 'Soup'
        }

        category = category_dict.get(category_input)

        if not category or category not in categories:
            print_error("Invalid category selection.")
            continue

        menu = categories[category]
        if not menu:
            print_error("No items found in this category.")
            continue

        display_menu()  # Show current menu
        item_number_input = input("Select the item number to restock --> ").strip()

        if item_number_input.isdigit():
            item_number = int(item_number_input)

            if item_number < 1 or item_number > len(menu):
                print_error("Invalid item number.")
                continue

            restock_quantity_input = input("Enter quantity to add for " + menu[item_number - 1]['item'] + " --> ").strip()

            if restock_quantity_input.isdigit():
                restock_quantity = int(restock_quantity_input)

                if restock_quantity > 0:
                    menu[item_number - 1]['quantity'] += restock_quantity
                    print_success(str(restock_quantity) + " units of " + menu[item_number - 1]['item'] + " have been added.\n")
                else:
                    print_error("Quantity must be a positive number.")
            else:
                print_error("Invalid quantity. Please enter a valid number.")
        else:
            print_error("Invalid item number.")

# Function to display menu items like a real café
def display_menu():
    print_title("Cafe Menu")
    for idx, (category, items) in enumerate(categories.items(), 1):
        print("\n--- " + category.upper() + " ---")
        print(f"{'No.':<4}{'Item':<20}{'Price (Rs)':<12}{'Quantity':<10}")
        print("-" * 49)
        for item_idx, item in enumerate(items, 1):
            print(f"{item_idx:<4}{item['item']:<20}Rs {item['price']:<10}{item['quantity']:<10}")
    print()


# Function to take an order
def take_order():
    global total_sales
    order = []
    customer_name = input("\nEnter Customer Name or Table Number --> ").strip()

    while True:
        display_menu()
        category_input = input("Enter the category number (1-6) to order from (or 'done' to finish) --> ").strip()

        if category_input.lower() == 'done':
            break

        if category_input not in ['1', '2', '3', '4', '5', '6']:
            print_error("Invalid category number. Please choose a number between 1 and 6.\n")
            continue

        category_dict = {
            '1': 'Drink',
            '2': 'Cake',
            '3': 'Fast Food',
            '4': 'Ice Cream',
            '5': 'Salad',
            '6': 'Soup'
        }

        category = category_dict.get(category_input)
        menu = categories[category]

        item_number_input = input("Select the item number from " + category + " --> ")
        
        if item_number_input.isdigit():
            item_number = int(item_number_input)

            if item_number < 1 or item_number > len(menu):
                print_error("Invalid item number. Please select a valid item.\n")
                continue

            item = menu[item_number - 1]
            quantity_input = input("Enter quantity for " + item['item'] + " --> ").strip()

            if quantity_input.isdigit():
                quantity = int(quantity_input)

                if quantity > 0:
                    # Check if the quantity is available
                    if quantity <= item['quantity']:
                        item_total = item['price'] * quantity
                        total_sales += item_total
                        order.append({'category': category, 'item': item['item'], 'quantity': quantity, 'total': item_total})

                        # Reduce the available quantity in the menu
                        item['quantity'] -= quantity

                        print_success(str(quantity) + " " + item['item'] + "(s) added to the order.\n")
                    else:
                        print_error("Only " + str(item['quantity']) + " " + item['item'] + "(s) available.\n")
                else:
                    print_error("Quantity must be a positive number.\n")
            else:
                print_error("Invalid quantity. Please enter a valid number.")
        else:
            print_error("Invalid item number.")

    orders.append({'customer': customer_name, 'order': order})

def generate_receipt(order_details):
    print_title("Receipt")
    customer_name = order_details['customer']
    order = order_details['order']
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("Customer: " + customer_name)
    print("Date/Time: " + date_time)
    print("-" * 40)
    print("Item\t\t\tQty\tTotal (Rs)")
    print("-" * 40)

    total_bill = 0
    for item in order:
        # Adjust spacing with \t for a cleaner display
        print(item['item'] + "\t\t" + str(item['quantity']) + "\tRs " + str(item['total']))
        total_bill += item['total']

    print("-" * 40)
    print("Total Bill: Rs " + str(total_bill))
    print("-" * 40)

# Function to display total sales at the end of the day
def display_total_sales():
    print_title("Daily Sales Report")
    print("Total Sales Today: Rs " + str(total_sales))

# Function to view order history
def view_order_history():
    print_title("Order History")
    if not orders:
        print_error("No orders have been placed yet.")
        return

    for order_idx in range(len(orders)):
        order_details = orders[order_idx]
        print("\nOrder #" + str(order_idx + 1) + " - Customer: " + order_details['customer'])
        print("-" * 40)
        for item in order_details['order']:
            # Adjust spacing with \t for better alignment
            print(item['item'] + "\t\t" + str(item['quantity']) + "\tRs " + str(item['total']))
        print("-" * 40)

# Function to cancel an order
def cancel_order():
    global total_sales
    print_title("Cancel Order")
    if not orders:
        print_error("No orders have been placed yet.")
        return

    view_order_history()
    order_number_input = input("Enter the order number to cancel --> ").strip()

    if order_number_input.isdigit():
        order_number = int(order_number_input)

        if order_number < 1 or order_number > len(orders):
            print_error("Invalid order number.")
            return

        # Get the selected order
        order_to_cancel = orders.pop(order_number - 1)

        # Restore item quantities
        for item in order_to_cancel['order']:
            category = item['category']
            for menu_item in categories[category]:
                if menu_item['item'] == item['item']:
                    menu_item['quantity'] += item['quantity']

        # Deduct from total sales
        refund_amount = sum(item['total'] for item in order_to_cancel['order'])
        total_sales -= refund_amount

        print_success("Order #" + str(order_number) + " has been canceled. Rs " + str(refund_amount) + " has been refunded.")
    else:
        print_error("Invalid input. Please enter a valid order number.")

# Main menu function
def main():
    while True:
        print_title("Cafe Management System")
        print("1 for  --> To Add Menu Item")
        print("2 for  --> To Remove Menu Item")
        print("3 for  --> To Restock Menu Item")
        print("4 for  --> To Display Menu")
        print("5 for  --> To Take Order")
        print("6 for  --> To View Order History")
        print("7 for  --> To Cancel Order")
        print("8 for  --> To Show Total Sales")
        print("9 for  --> To Exit")
        choice = input("Enter the given choices from above --> ").strip()
        if choice == '1':
            add_menu_item()
        elif choice == '2':
            remove_menu_item()
        elif choice == '3':
            restock_item()
        elif choice == '4':
            display_menu()
        elif choice == '5':
            take_order()
            for order in orders:
                generate_receipt(order)
        elif choice == '6':
            view_order_history()
        elif choice == '7':
            cancel_order()
        elif choice == '8':
            display_total_sales()
        elif choice == '9':
            print("Thank you for using the Café Management System. Have a great day!")
            break
        else:
            print_error("Invalid choice! Please choose a valid option.\n")

# Run the main function
main()