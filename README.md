 CLI Task Manager

A simple command-line task manager built using Python. It allows users to add, view, complete, delete, and filter tasks.

Features

- Add new tasks with optional due dates.
- View all tasks.
- Mark tasks as completed.
- Delete tasks.
- Filter tasks by status.
- Filter tasks by due date.
- Save tasks using JSON storage.
- Automated tests using pytest.

Requirements

- Python 3
- pytest

 Installation

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Install pytest:


python -m pip install pytest


Usage

 Add a task


python cli.py add "Learn Python" --due 2026-12-13


View all tasks


python cli.py list


 Complete a task


python cli.py complete 1


 Delete a task


python cli.py delete 1


Filter by status


python cli.py list --status pending


 Filter by due date


python cli.py list --due 2026-12-13


Run Tests


python -m pytest -v


Project Structure

cli-task-manager
 cli.py
storage.py
test_task_manager.py
README.md
tasks.json


Technologies Used

- Python
- argparse
- JSON
- pytest