from openai import OpenAI
from dotenv import load_dotenv
from app.config import Config


class App:

    def __init__(self) -> None:
        self.config = Config.get_all()
        self.client = OpenAI()

    def generate_text(self, prompt):
        """Generar texto con el modelo LLM GTP-4o-mini"""

        message = self.client.chat.completions.create(
            model=self.config["model"],
            max_tokens=self.config["max_tokens"],
            temperature=self.config["temperature"],
            messages=[
                {"role": "system", "content": "You are a smart AI assitant"},
                {"role": "user", "content": prompt},
            ],
        )
        return message.choices[0].message.content


if __name__ == "__main__":
    load_dotenv()
    prompt = "Escribe una historia sobre inteligencia artificial."
