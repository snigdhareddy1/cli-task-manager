
import argparse
from datetime import date
from storage import load_tasks, save_tasks


def add_task(args):
    tasks = load_tasks()

    task = {
        "id": max([t["id"] for t in tasks], default=0) + 1,
        "title": args.title,
        "due": args.due,
        "status": "pending"
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully! ID: {task['id']}")


def list_tasks(args):
    tasks = load_tasks()

    if args.status:
        tasks = [t for t in tasks if t["status"] == args.status]

    if args.due:
        tasks = [t for t in tasks if t["due"] == args.due]

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(
            f"ID: {task['id']} | "
            f"Title: {task['title']} | "
            f"Due: {task['due'] or 'Not set'} | "
            f"Status: {task['status']}"
        )


def complete_task(args):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == args.id:
            task["status"] = "completed"
            save_tasks(tasks)
            print("Task marked as completed!")
            return

    print("Task not found.")


def delete_task(args):
    tasks = load_tasks()
    updated_tasks = [t for t in tasks if t["id"] != args.id]

    if len(tasks) == len(updated_tasks):
        print("Task not found.")
        return

    save_tasks(updated_tasks)
    print("Task deleted successfully!")


def main():
    parser = argparse.ArgumentParser(
        description="A simple command-line task manager"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")
    add_parser.add_argument("--due")
    add_parser.set_defaults(func=add_task)

    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--status", choices=["pending", "completed"])
    list_parser.add_argument("--due")
    list_parser.set_defaults(func=list_tasks)

    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("id", type=int)
    complete_parser.set_defaults(func=complete_task)

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int)
    delete_parser.set_defaults(func=delete_task)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
