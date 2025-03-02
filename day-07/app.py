def main():
    tasks = []  # Task list
    
    while True:
        print("\n📌 To-Do List!")
        print("1️⃣  Add Task")
        print("2️⃣  Show Tasks ")
        print("3️⃣  Delete Task")
        print("4️⃣  Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            task = input("Enter new task: ")
            tasks.append(task)
            print("Task Added! ✅")
        
        elif choice == "2":
            if tasks:
                print("\n📝 Your To-Do List:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
            else:
                print("No tasks found! 📝")
        
        elif choice == "3":
            if tasks:
                print("\n📝 Your To-Do List:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                try:
                    task_index = int(input("Enter task number to delete: ")) - 1
                    if 0 <= task_index < len(tasks):
                        removed_task = tasks.pop(task_index)
                        print(f"Task '{removed_task}' deleted! ❌")
                    else:
                        print("Invalid task number! 🚫")
                except ValueError:
                    print("Please enter a valid number! 🔢")
            else:
                print("No tasks to delete! 📝")
        
        elif choice == "4":
            print("Exiting... Goodbye! 👋")
            break
        
        else:
            print("Invalid choice! Please choose between 1-4. 🚀")

if __name__ == "__main__":
    main()
