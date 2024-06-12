class ToDoList:
    def __init__(self):
      self.tasks = []
      
    def add_tasks(self,tasks): 
        for task in tasks:
         self.tasks.append({'task': task,'completed':False })
        task_list = ",".join([f"'{task}'" for task in tasks])
        print(f"Added tasks : '{task_list}'")
        
    def view_tasks(self):
        if not self.tasks:
            print("NO tasks in TO-DO list")  
        else:
            print("To-Do-List:")  
            for idx,task in enumerate(self.tasks,start = 1): 
               status = "Done" if task ['completed'] else "pending"
               print(f"{idx}.{task['task']} - {status}")
               
    def complete_tasks(self,task_number):
        if 0<task_number <= len(self.tasks) :
            self.tasks[task_number - 1]['completed'] = True 
            print(f"Marked task {task_number} as completed") 
        else:
            print("invalid task number")        
def main():
    to_do_list = ToDoList()  
    
    while True:
        print("\n**** Welcome to the TO-Do List Manager ****") 
        print("1.Add Task") 
        print("2.View tasks")
        print("3.complete task")
        print("4.Exit")
        
        choice = input("Enter the choice:")
        
        
        if choice == "1":
            tasks_input =input("Enter tasks separted by commas:")
            tasks = [task.strip() for task in tasks_input.split(',')]
            to_do_list.add_tasks(tasks)
        elif choice == "2" :
            to_do_list.view_tasks()   
        elif choice == "3":
            task_number = int(input("Enter the task no.to complete:"))
            to_do_list.complete_tasks(task_number)
        elif choice == "4":
            print("Exiting the TO-Do list manager") 
            break 
        else:
            print("invalid choice.Please try again")            
        
if __name__ == "__main__" : 
  main()    