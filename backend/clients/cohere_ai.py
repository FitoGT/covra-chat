import os
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain.schema import HumanMessage

load_dotenv()


class CohereAI:
    def __init__(self):
        self.llm = ChatCohere(
            cohere_api_key=os.getenv("COHERE_API_KEY"),
            model="command"
        )

    def generate_text(self, prompt: str) -> str:
        response = self.llm([HumanMessage(content=prompt)])
        return response.content

    def generate_cover_letter(self, cv: str, job_description: str) -> str:
        prompt = f"""
        You are an expert cover letter writer.

        Write a concise, authentic **cover letter** that sounds like it was written by a **senior software developer with 10+ years of experience**.

        Use the following details:

        - **CV**:  
        {cv}

        - **Job Description**:  
        {job_description}

        ### Requirements:
        - Max **150 words**
        - Clear structure: *short intro, focused body, strong closing*
        - Professional tone with confidence and warmth — no fluff
        - Highlight alignment between experience and job needs
        - Avoid clichés and vague statements. Prioritize substance
        - It must sound like a real person wrote it — experienced, sharp, and to the point
        """
        return self.generate_text(prompt)
