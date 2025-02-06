import json
from random import choice, shuffle
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

def create_task(task: str) -> str:
  letters = 'abcdefghijklmnopqrstuvwxyz'
  nums = '1234567890'
  
  id = f'{choice(letters)}{choice(nums)}'
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

def validate_task(cmd, params):
  task = ""
  match cmd:
    case "add": task = " ".join(params[0:])
    case "update": task = " ".join(params[1:])
  
  task = task.replace("\"", "")
  if len(task) > 0:
    return task
  else:
    input("You must add the ID or the task.")
    return False

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
  
  task = ""
  if params:
    task_id = params[0]
    
  try:
    match command:
      case "help": print_help()
      case "quit": 
        save_archive()
        break
      case "add":
        task = validate_task(command, params)
        if isinstance(task, str):
          print(f'Task added successfully (ID: {create_task(task)})')
        else:
          continue
      case "update":
        task = validate_task(command, params)
        if isinstance(task, str):
          update_task(task_id, task)
        else:
          continue
      case "delete": delete_task(task_id)
      case "mark-in-progress": mark_tasks(task_id, "in-progress")
      case "mark-done": mark_tasks(task_id, "done")
      case "list": 
        if len(tasks) < 0: print("There are not task yet")
        else: list_tasks(params[-1] if params else "list")
      case other: print("Command not allow")
  
  except NameError as e:
    print("You made something wrong: ", e)
    
  input("Press enter...")
