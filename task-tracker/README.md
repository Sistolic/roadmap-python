# [Task Tracker CLI](https://roadmap.sh/projects/task-tracker)

Task Tracker CLI is a simple command-line application that allows you to manage tasks easily. The application is build in Python. 

## Installation

To use this application, clone the repository to your machine:

```
git clone https://github.com/Sistolic/roadmap-python.git
cd task-tracker
```

## Usage
Run the application
```
python task-tracker.py
```

- Add a task
```
add "Buy groceries"
```

- Update a task
```
update <task-id> "New task"
```

- Mark the task
```
# Mark the task in progress
mark-in-progress <task-id>

# Mark the task done
mark-done <task-id>
```

- List tasks
```
# To list all the tasks
list

# Filter the tasks
list done
list todo
list in-progress
```

- Delete a  task
```
delete <task-id>
```
