from app.memory.memory import Memory


class AIBinoAgent:
    name = "AI-Bino"

    def respond(self, message: str) -> str:
        memory = Memory()

        memories = memory.load()
        memory.save(message)

        if memories:
            previous = memories[-1]
            return f"{self.name} remembers: {previous}. You said: {message}"

        return f"{self.name} received: {message}"