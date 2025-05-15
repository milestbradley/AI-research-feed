# src/summarize.py

import openai
from src.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def summarize_abstract(title, abstract):
    prompt = f"""Summarize the following research paper in 2–3 bullet points:
Title: {title}
Abstract: {abstract}

-"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert AI researcher."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )

        content = response.choices[0].message.content.strip()
        return content
    except Exception as e:
        print(f"Error during OpenAI summarization: {e}")
        return None
