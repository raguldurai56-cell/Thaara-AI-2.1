from datetime import datetime


class CommandHistory:
    def __init__(self):
        self.items = []

    def add_command(self, command, input_type="text", success=True):
        self.items.append({"command": command, "input_type": input_type, "success": success, "timestamp": datetime.now().isoformat()})

    def get_recent_commands(self, limit=20):
        return list(reversed(self.items[-limit:]))

    def clear_history(self):
        self.items.clear()

    def search_commands(self, query="", date_filter="", input_type=""):
        query = (query or "").lower()
        return [i for i in self.items if query in i["command"].lower() and (not input_type or i["input_type"] == input_type)]

    def get_statistics(self):
        total = len(self.items)
        return {"total": total, "voice": sum(i["input_type"] == "voice" for i in self.items), "text": sum(i["input_type"] == "text" for i in self.items), "most_used": [], "success_rate": sum(i["success"] for i in self.items) / total * 100 if total else 0}


command_history = CommandHistory()
