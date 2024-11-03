# maria_noor, amna_arif, qudsia

menu = { 
    'pizza': 20,        
    'pasta': 30,
    'burger': 50,
    'sandwich': 40,
    'kabli pulao': 100 
}

print("Welcome to Algorithm Avengers Restaurant")    
print("pizza: Rs. 20\npasta: Rs. 30\nburger: Rs. 50\nsandwich: Rs. 40\nkabli pulao: Rs. 100")

order_total = 0   

item_1 = input("Enter the name of your order: ")   

if item_1 in menu:              
    order_total = menu[item_1]   
    print(f"Your item {item_1} has been added")
else:
    print("Invalid choice, please try again dear")

more_order = input("Do you want to order something else? (yes/no): ")

if more_order.lower() == "yes":    
    item_2 = input("Enter the second item: ")
    
    if item_2 in menu:
        order_total += menu[item_2]   
        print(f"Your item {item_2} has been added")   
    else:
        print(f"Item {item_2} is not available!")

print(f"The total amount to pay is Rs.{order_total}")