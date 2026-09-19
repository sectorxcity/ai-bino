import json
from pathlib import Path

class Memory:
    file_path = Path('data/memory.json')

    def save(self, message: str):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        memories = self.load()
        memories.append(message)
        self.file_path.write_text(json.dumps(memories, indent=2), encoding='utf-8')

    def load(self):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self.file_path.write_text('[]', encoding='utf-8')
        return json.loads(self.file_path.read_text(encoding='utf-8'))
