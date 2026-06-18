import ast
import json
import pandas as pd

from src.pdf_loader import load_pdf
from src.claim_extractor import extract_claims
from src.web_search import search_web
from src.verifier import verify_claim


def clean_claims(claims):

    claims = claims.replace("```python", "")

    claims = claims.replace("```", "")

    claims = claims.strip()

    return ast.literal_eval(claims)


def clean_verification(response):

    response = response.replace("```json", "")

    response = response.replace("```", "")

    response = response.strip()

    return json.loads(response)


def fact_check_pdf(pdf_path, client, tavily_client):

    text = load_pdf(pdf_path)

    claims = extract_claims(
        text,
        client
    )

    claims_list = clean_claims(
        claims
    )

    all_results = []

    for claim in claims_list:

        web_results = search_web(
            claim,
            tavily_client
        )

        verification = verify_claim(
            claim,
            web_results,
            client
        )

        verification = clean_verification(
            verification
        )

        all_results.append({

            "claim": claim,

            "status": verification["status"],

            "reason": verification["reason"],

            "corrected_fact": verification["corrected_fact"],

            "source_url": web_results[0]["url"]

        })

    return pd.DataFrame(all_results)