class AIBinoAgent:
    name = 'AI-Bino'

    def respond(self, message: str) -> str:
        return f'{self.name} received: {message}'
