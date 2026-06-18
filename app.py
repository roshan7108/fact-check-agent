import streamlit as st

from openai import OpenAI
from tavily import TavilyClient

from src.utils import fact_check_pdf


st.set_page_config(

    page_title="Fact Check Agent",

    page_icon="✅",

    layout="wide"

)

st.title("🔎 AI Fact Check Agent")

st.markdown(
    """
    Upload a PDF and automatically verify factual claims
    against live web sources.

    The system will classify each claim as:

    ✅ Verified

    ⚠️ Inaccurate

    ❌ False
    """
)


OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]


client = OpenAI(

    api_key=OPENAI_API_KEY

)

tavily_client = TavilyClient(

    api_key=TAVILY_API_KEY

)


uploaded_file = st.file_uploader(

    "Upload PDF",

    type=["pdf"]

)


if uploaded_file:

    with open(

        uploaded_file.name,

        "wb"

    ) as file:

        file.write(

            uploaded_file.getbuffer()

        )

    if st.button("Verify Facts"):

        with st.spinner(

            "Fact checking..."

        ):

            df = fact_check_pdf(

                uploaded_file.name,

                client,

                tavily_client

            )

        st.dataframe(

            df,

            use_container_width=True

        )
        
        st.download_button(
            label="📥 Download Report",
            data=df.to_csv(index=False),
            file_name="fact_check_report.csv",
            mime="text/csv"
        )