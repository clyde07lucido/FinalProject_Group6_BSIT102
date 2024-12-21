menu = ["Big Mac", "Coke Float", "French Fries", "Cheeseburger", "Chicken Nuggets", "Apple Pie", "Iced Tea", "Combo Meal"]
price = [120, 70, 100, 150, 180, 50, 60, 250]

total_price = [0]  

def apply_discount():
    if total_price[0] > 300:
        discount = total_price[0] * 0.1 
        total_price[0] -= discount
        print(f"\nYou get a 10% discount of ₱{discount}. New total: ₱{total_price[0]}")

def display_menu(menu, price):
        for i in range(len(menu)):
            print(f"{i+1}. {menu[i]}: ₱{price[i]}")

# Main Ordering Loop
while True:
    print("\nChoose the number of the item you want to order. Enter 0 to finish.")
    display_menu(menu, price)
    choice = int(input("\nEnter your choice: "))

    if choice == 0:
        break 
    elif 1 <= choice <= len(menu):
        total_price[0] += price[choice - 1]
        print(f"\nAdded {menu[choice - 1]} to your order. Total: ₱{total_price[0]}")
    else:
        print("Invalid choice. Please select a valid menu item.")


apply_discount()

print(f"\nYour total bill is: ₱{total_price[0]}")


while True:
    fee = int(input("\nEnter your fee: ₱ "))
    change = fee - total_price[0]

    if fee >= total_price[0]:
        print(f"\nChange: ₱{change}")
        break  
    else:
        print(f"\nYour fee is not enough. Please pay at least ₱{total_price[0]}")

print("\nThank you for your order. Come Again!")