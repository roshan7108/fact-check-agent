def verify_claim(claim, web_results, client):

    evidence = "\n".join(

        [item["content"] for item in web_results]

    )

    prompt = f"""
    Claim:
    {claim}

    Evidence:
    {evidence}

    Based on the evidence, classify the claim as ONLY one of:

    - Verified
    - Inaccurate
    - False

    Return ONLY a JSON dictionary in this format:

    {{
      "status":"",
      "reason":"",
      "corrected_fact":""
    }}
    """

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[

            {
                "role": "system",

                "content": "You are a fact-checking assistant."
            },

            {
                "role": "user",

                "content": prompt
            }

        ],

        temperature=0

    )

    return response.choices[0].message.content