#Todo List Manager (Menu-Driven List)
todo_list = []

while True:
    print("\n--- To-Do List Manager ---")
    print("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the new task: ")
        todo_list.append(task)
        print("Task added successfully.")
        
    elif choice == '2':
        print("\nYour Tasks:")
        if not todo_list:
            print("The list is empty.")
        else:
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
                
    elif choice == '3':
        if not todo_list:
            print("Nothing to remove. The list is empty.")
            continue
            
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(todo_list):
                # Subtract 1 because list indices start at 0
                removed_task = todo_list.pop(task_num - 1)
                print(f"Successfully removed: '{removed_task}'")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
            
    elif choice == '4':
        print("Exiting To-Do List Manager.")
        break
        
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")