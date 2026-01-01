import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_API_KEY=os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing in .env file")
client=Groq(api_key=GROQ_API_KEY)

def generate_llm_response(prompt: str)-> str:
    """
    Simple Groq call - we will improve formatting later.
    """
    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role":"system",
                "content":"You are an academic medical study assistant."
                "Explain topics in exam-oriented structure format."
                "Do NOT give real-world treatment instructions."
            },
            {"role":"user","content":prompt}

        ],
        temperature=0.4,

    )
    return response.choices[0].message.content
    
