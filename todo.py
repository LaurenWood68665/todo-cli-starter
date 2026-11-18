import argparse
import json
from pathlib import Path

DB = Path("tasks.json")

def load_tasks():
    return json.loads(DB.read_text()) if DB.exists() else []

def save_tasks(tasks):
    DB.write_text(json.dumps(tasks, indent=2))

def main():
    parser = argparse.ArgumentParser(description="Simple CLI Todo Manager")
    sub = parser.add_subparsers(dest="cmd", required=True)
    add_p = sub.add_parser("add")
    add_p.add_argument("title")
    sub.add_parser("list")
    args = parser.parse_args()
    tasks = load_tasks()
    if args.cmd == "add":
        tasks.append({"title": args.title, "done": False})
        save_tasks(tasks)
        print(f"Added: {args.title}")
    elif args.cmd == "list":
        for i, t in enumerate(tasks, 1):
            mark = "x" if t["done"] else " "
            print(f"{i}. [{mark}] {t['title']}")

if __name__ == "__main__":
    main()
