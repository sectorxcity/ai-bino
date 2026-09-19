from app.memory.memory import Memory


class AIBinoAgent:
    name = "AI-Bino"

    def respond(self, message: str, memory_type: str = "general") -> str:
        memory = Memory()

        previous_memories = memory.load()

        memory.save(message, memory_type)

        if previous_memories:
            previous = previous_memories[-1]

            return (
                f"{self.name} remembers: {previous['content']} "
                f"(type: {previous['type']}). "
                f"You said: {message}"
            )

        return f"{self.name} received: {message}"