# utils.py (create this if you don't already have it)

from openai import OpenAI


def call_gpt(user_message: str, model: str = "gpt-4o-mini") -> str:
    client = OpenAI()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ],
    )

    return response.choices[0].message.content