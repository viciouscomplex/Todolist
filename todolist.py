# define a list to store items
todo_list = []

# define a function to add items to the list
def add_item():
    item = input("Enter a to-do item: ")
    todo_list.append(item)
    print("Item added to list.")

# define a function to remove items from the list
def remove_item():
    item = input("Enter an item to remove: ")
    try:
        todo_list.remove(item)
        print("Item removed from list.")
    except ValueError:
        print("Item not found in list.")

# define a function to print the current list
def print_list():
    print("To-Do List:")
    for item in todo_list:
        print("- " + item)

# main program loop
while True:
    print("\nWhat would you like to do?")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Print the list")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        print_list()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
