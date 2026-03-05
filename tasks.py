
# tasks.py — starter scaffold (Team Lead creates this)

tasks = []   # Each task: {"id": int, "title": str, "priority": str, "done": bool}
_next_id = 1

def display_tasks():
    if not tasks:
        print("📋 No tasks yet.")
        return

    for t in tasks:
        print(f"[{t['id']}] {t['title']} ({t['priority']})") 
#added the code
def add_task(title, priority="medium"): global _next_id if priority not in ["high", "medium", "low"]: print("❌ Priority must be: high, medium, or low") return task = {"id": _next_id, "title": title, "priority": priority, "done": False} tasks.append(task) _next_id += 1 print(f"✅ Task added: [{task['id']}] {title} ({priority})")