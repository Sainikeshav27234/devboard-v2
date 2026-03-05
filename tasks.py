
# tasks.py — starter scaffold (Team Lead creates this)

tasks = []   # Each task: {"id": int, "title": str, "priority": str, "done": bool}
_next_id = 1

def display_tasks():
    if not tasks:
        print("📋 No tasks yet.")
        return

    for t in tasks:
        print(f"[{t['id']}] {t['title']} ({t['priority']})") 

def delete_task(task_id): 
global tasks original_len = len(tasks) 
tasks = [t for t in tasks if t["id"] != task_id] 
	if len(tasks) < original_len: print(f"🗑️ Task {task_id} deleted.") 
	else: print(f"❌ No task found with ID {task_id}")
