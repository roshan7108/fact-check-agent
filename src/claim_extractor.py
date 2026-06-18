from openai import OpenAI


def extract_claims(text, client):

    prompt = f"""
    Extract complete factual statements from the text.

    Rules:
    1. Return complete sentences, not just numbers.
    2. Include statements containing:
       - dates
       - statistics
       - measurements
       - financial figures
       - technical facts

    Return ONLY a Python list.

    Example:

    [
      "India's population is 1.35 billion.",
      "ChatGPT was launched in 2021."
    ]

    Text:
    {text}
    """

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[

            {
                "role": "system",

                "content": "You extract factual claims."
            },

            {
                "role": "user",

                "content": prompt
            }

        ],

        temperature=0

    )

    return response.choices[0].message.content