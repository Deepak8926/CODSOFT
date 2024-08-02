asks= []

def add_task(task):
    tasks.append(task)
    print(f"task '{task}' added.")

def remove_task(task):
        if task in task:
              tasks.remove(task)
              print(f"task '{task}'removed.")
        else:
              print(f"task '{task}'not found.")

def list_task():
      if not tasks:
            print("No task in the list.")
      else:
            print("To-Do list:")
            for idx, task in enumerate(tasks, 1):
                  print(f"{idx} . {task}")

def main():
      while True:
            print("\nOptions:")
            print("1. Add task")
            print("2. remove task")
            print("3. list tasks")
            print("4. Exit")

            choice = input("choose an optio:")

            if choice == '1':
                  task = input("Enter the task:")
                  add_task(task)
            elif choice =='2':
                  task= input("Enter the task to remove:")
                  remove_task(task)
            elif choice == '3':
                  list_task()
            elif choice == '4':
                  break
            else:
                  print("Invalid choice, please try again.")
if __name__=="__main__":    
      main() 
