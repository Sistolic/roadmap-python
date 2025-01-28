import json
from os import system as sys
from datetime import datetime

tasks = []

def print_help():
  print("""
  add - add a task
  update - update a task
  delete - delete a task
  mark-in-progress - mark the task in progress
  mark-done - mark the task done

  list - list all tasks
    use 'list' follow by:
      done - to list all done tasks
      todo - to list tasks to do
      in-progress - to list tasks in progress
""")

def search_id(task_id: int) -> bool:
  for idx, task in enumerate(tasks):
    for value in task.values():
      if value == task_id: return search_id(task_id + 1)
      else: return task_id

def create_task(task: str) -> str:
  id = len(tasks) + 1 if len(tasks) == 0 else search_id(len(tasks) + 1)
  
  tasks.append({
    "id": id,
    "description": task,
    "status": "todo",
    "createdAt": datetime.now().strftime("%H:%M - %d %B %Y"),
    "updateAt": ""
  })
  
  return id
    
def update_task(task_id: int, new_task: str):
  update_time = f'{datetime.now().strftime("%H:%M - %d %B %Y")}'
  
  for task in tasks:
    for value in task.values():
      if value == task_id:
        task.update({"updateAt": update_time})
        task.update({"description": new_task})
        
        break

def delete_task(task_id: int):
  for idx, task in enumerate(tasks):
    for value in task.values():
      if value == task_id:
        tasks.pop(idx)
        
        break

def mark_tasks(task_id: int, command: str):
  for task in tasks:
    for value in task.values():
      if value == task_id:
        task.update({"status": command})
        
        break
      
def list_tasks(command: str):
  sys('cls')
  for task in tasks:
    if task["status"] == command or command == "list":
      print("-"*30)
      for key, value in task.items():
        print(f'{key}: {value}')
        
def save_archive():
  with open(path, "w") as file:
    json.dump(tasks, file, indent=2)
    
path = "tasks.json"

try:
  with open(path, "r") as file:
    tasks = json.load(file)
except FileNotFoundError:
  save_archive()
except json.decoder.JSONDecodeError:
  pass

while True:
  sys('cls')
  user_input = input("> task-cli ")
  
  cmd_split = user_input.split()
  command = "".join(cmd_split[:1])

  params = cmd_split[1:]
  task = " ".join(params[:]).replace("\"", "")
  
  if params and params[0].isdigit():
    task = " ".join(params[1:]).replace("\"", "")
    task_id = int("".join(params[:1]))
    if len(tasks) < task_id or task_id <= 0:
      input("You must add a valid ID.")
      continue
  
  if command != "delete" and (params and not task):
    input("You must add a task to do.")
    continue
  
  try:
    match command:
      case "help": print_help()
      case "quit": 
        save_archive()
        break
      case "add": print(f'Task added successfully (ID: {create_task(task)})')
      case "update": update_task(task_id, task)
      case "delete": delete_task(task_id)
      case "mark-in-progress": mark_tasks(task_id, "in-progress")
      case "mark-done": mark_tasks(task_id, "done")
      case "list": 
        if len(tasks) < 0: print("There are not task yet")
        else: list_tasks(params[-1] if params else "list")
      case other: print("Command not allow")
  
  except NameError:
    print("You must add the ID in the command.")
    
  input("...")