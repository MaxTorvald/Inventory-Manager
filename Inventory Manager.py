# Creating Inventory Manager for artists and freelancers

import json
import os

# File to store inventory data

Data_files = "Inventory.json"

# 1 - Load inventory from file
def load_inventory():
    if os.path.exists(Data_files):
        try:
            with open (Data_files, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            print("Error reading inventory file. Starting with empty inventory.")
            return{}
    return{}

# 2 - Save inventory to file
def save_inventory(inventury):
    try:
        with open(Data_files, "w") as file:
            json.dump(inventury, file, indent=4)
    except IOError:
        print("Cannot save your file.")

# 3 - Add a new Product
def add_product(product):
    product_ID = input("Enter product ID").strip()
    if product_ID in product:
        print("Product ID already exists")
        return
    name = input("Enter product name:")
    try:
        quantity = int(input("Enter quantity:"))
        price  = int(float("Enter the price: "))
    except ValueError:
        print("Invalid value inserted")
        return
    product[product_ID] = {"name" : name, "quantity" : quantity, "price": price}
    print("Product added successfully.")

# Update product details

def update_product(inventory):
    product_id = input("Enter product ID to update:").strip()
    if product_id not in inventory:
        print("Product ID not found.")
        return
    try:
        quantity = int(input("Enter new quantity:"))
        price = float(input("Enter new price:"))
    except:
        print("Invalid quantity or price>")
    inventory[product_id]["quantity"] = quantity
    inventory[product_id]["price"] = price
    print("Product updated successfully.")

# Delete a product

def del_product(inventory):
    product_id = input("Enter a product Id to delete: ").strip()
    if product_id in inventory:
        del inventory[product_id]
        print("product deleted successfully")
    else:
        print("Product not found")

# Search for a product

def search_product(inventory):
    keyword = input("Please insert the name of the product:").strip().lower()
    found = False
    for pid, details in inventory.items():
        if keyword in pid.lower() or keyword in details["name"].lower():
            print(f"ID = {pid}, name = {details['name']}, Qty = {details["quantity"]}, Price = {details['price']}")
            found = True
        if not found:
            print("No matching product found")

# Display all of the products

def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty")
        return
    print("\n ---Inventory List ---")
    for pid, details in inventory.items():
         print(f"ID = {pid}, name = {details['name']}, Qty = {details["quantity"]}, Price = {details['price']}")
    print("Done.")

# Main menu

def main():
    inventory = load_inventory()
    while True:
        print("\nInventory Manager")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. Search Product")
        print("5. Display Inventory")
        print("6. Save & Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_product(inventory)
        elif choice == "2":
            update_product(inventory)
        elif choice == "3":
            del_product(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            display_inventory(inventory)
        elif choice == "6":
            save_inventory(inventory)
            print("Inventory saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()