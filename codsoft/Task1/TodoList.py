class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks added yet.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f'{i}. {task["task"]} - {status}')

    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    def save_tasks(self, filename):
        with open(filename, 'w') as f:
            for task in self.tasks:
                f.write(f'{task["task"]},{task["completed"]}\n')

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    task_info = line.strip().split(',')
                    self.tasks.append({"task": task_info[0], "completed": bool(task_info[1])})
        except FileNotFoundError:
            print("File not found. Starting with an empty list.")

def main():
    todo_list = TodoList()
    todo_list.load_tasks('tasks.txt')

    while True:
        print("\n======= TO-DO LIST =======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Save Tasks")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
            print("Task added successfully!")
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to mark as completed: "))
            todo_list.complete_task(task_number)
        elif choice == '4':
            todo_list.save_tasks('tasks.txt')
            print("Tasks saved successfully!")
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

    todo_list.save_tasks('tasks.txt')

if __name__ == "__main__":
    main()
