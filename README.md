# DevBoard v2

## Project Description
DevBoard v2 is a simple Python-based task management system that runs in the command line. It allows users to add, update, delete, search, and display tasks with different priority levels.

This project demonstrates collaborative software development using GitHub. The team practiced working with branches, pull requests, code reviews, merge conflict resolution, automated testing, and documentation.

---

## Features

### Add Task
Adds a new task with a title and priority.

Example:
add_task("Buy groceries", "high")
Example Output:
✅ Task added: [1] Buy groceries (high)

### Delete Task
Deletes a task using its task ID.

Example:
delete_task(1)
Example Output:
🗑️ Task 1 deleted.

### Update Task
Updates a task's title or priority using its task ID.

Example:
update_task(1, "Buy milk", "medium")
Example Output:
✏️ Task 1 updated: [1] Buy milk (medium)

### Search Task
Searches for tasks based on a keyword.

Example:
search_task("deploy")
Example Output:
🔍 Found 1 match(es):
[1] Deploy to staging

### Display Tasks
Displays all tasks with their IDs, titles, and priorities.

Example:
Example Output:

--- 2 Task(s) ---
[ ] [1] Buy groceries (high)
[✓] [2] Write tests (medium)

### Test Structure

devboard-v2
│
├── tasks.py
├── test_tasks.py
├── README.md
└── CONTRIBUTING.md

## Installation

1. Clone the repository
git clone https://github.com/Sainikeshav27234/devboard-v2.git

2. Navigate into the folder
cd devboard-v2

3. Install dependencies
pip install pytest

How to Run the Program

Example:

## Running the App

Run Python and import the task module:

python
>>> import tasks
>>> tasks.add_task("Finish assignment", "high")
>>> tasks.display_tasks()


### Team Members
Name	            Role	                GitHub Username
Keshav	            Team Lead	            @Sainikeshav27234
Chinni Krishna	    Backend Developer A	    @GrayViper
Sreejit 	        Backend Developer B	    @Sreejit
Murli	            QA Engineer             @Murli
Archishman          Technical Writer	    @Zlan9

