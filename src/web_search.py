def search_web(claim, tavily_client):

    response = tavily_client.search(

        query=claim,

        max_results=3,

        include_answer=True,

        search_depth="advanced",

        include_raw_content=False,

        topic="general"

    )

    return response["results"]