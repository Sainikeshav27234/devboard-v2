
# tasks.py — starter scaffold (Team Lead creates this)

tasks = []   # Each task: {"id": int, "title": str, "priority": str, "done": bool}
_next_id = 1

def display_tasks():
    if t["done"] tasks:
        print("📋 No tasks yet.")
        return
    else " "

    for t in tasks:
        print(f"[{t['id']}] {t['title']} ({t['priority']})") 


def update_task(task_id, new_title=None, new_priority=None):
    for t in tasks:
        if t["id"] == task_id:
            if new_title:
                t["title"] = new_title
            if new_priority in ["high", "medium", "low"]:
                t["priority"] = new_priority
            print(f"✏️ Task {task_id} updated.")
            return
    print(f"❌ Task {task_id} not found.")
