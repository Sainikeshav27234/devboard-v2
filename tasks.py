
# tasks.py — starter scaffold (Team Lead creates this)

tasks = []   # Each task: {"id": int, "title": str, "priority": str, "done": bool}
_next_id = 1
print(f"--- {len(tasks)} Task(s) ---")
def display_tasks():
    if not tasks:
        print("📋 No tasks yet.")
        return

    for t in tasks:
        print(f"[{t['id']}] {t['title']} ({t['priority']})") 
def search_task(keyword): results = [t for t in tasks if keyword.lower() in t["title"].lower()] if not results: print(f"🔍 No tasks found matching '{keyword}'") else: print(f"🔍 Found {len(results)} match(es):") for t in results: print(f" [{t['id']}] {t['title']}")