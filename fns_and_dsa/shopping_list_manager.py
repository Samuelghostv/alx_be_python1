
def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Main function to manage shopping list
def main():
    shopping_list = []  

    while True:
        display_menu()  
        choice = input("Enter your choice (1-4): ")

        try:
            choice = int(choice)  
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  

        if choice == 1:
            # Add an item to the shopping list
            item = input("Enter the name of the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")

        elif choice == 2:
            # Remove an item from the shopping list
            item = input("Enter the name of the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
                
            else:
                print(f"'{item}' is not in the shopping list.")

        elif choice == 3:
            # Display the shopping list
            if shopping_list:
                print("Your shopping list:")
                for item in shopping_list:
                    print(f"- {item}")
                    
            else:
                print("Your shopping list is empty.")

        elif choice == 4:
            
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
