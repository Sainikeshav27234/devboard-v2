
# tasks.py — starter scaffold (Team Lead creates this)

tasks = []   # Each task: {"id": int, "title": str, "priority": str, "done": bool}
_next_id = 1

def display_tasks():
    if not tasks:
        print("📋 No tasks yet.")
        return

    for t in tasks:
        print(f"[{t['id']}] {t['title']} ({t['priority']})") 