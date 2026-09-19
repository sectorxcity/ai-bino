import json
from pathlib import Path
from datetime import datetime


class Memory:
    file_path = Path("data/memory.json")

    def save(self, content: str, memory_type: str = "general"):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        memories = self.load()

        memory = {
            "content": content,
            "type": memory_type,
            "timestamp": datetime.now().isoformat()
        }

        memories.append(memory)

        self.file_path.write_text(
            json.dumps(memories, indent=2),
            encoding="utf-8"
        )

    def load(self):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.file_path.exists():
            self.file_path.write_text("[]", encoding="utf-8")

        return json.loads(
            self.file_path.read_text(encoding="utf-8")
        )