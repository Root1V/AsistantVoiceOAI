from streamlit_mic_recorder import speech_to_text
from langchain_openai import ChatOpenAI
import streamlit as st

from dotenv import load_dotenv
from app.config import Config

class App:

    def __init__(self) -> None:
        self.config = Config.get_all()
        self.client = ChatOpenAI(model=self.config["model"])

    def show(self):
        st.title("Tu asistente de voz Elysia")
        st.write("App chat habilitada por voz")
        text = speech_to_text(language="es", use_container_width=True, just_once=False, key="STT")

        if text:
            st.write("Tu:", text)
            response = self.client.invoke(text)
            st.write("Respuesta del modelo:", response.content)


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