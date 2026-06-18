# 🔎 AI Fact Check Agent

An AI-powered Fact-Checking Web Application that automatically verifies factual claims from PDF documents against live web data.

This application extracts factual statements from uploaded PDFs, searches reliable web sources, verifies their accuracy using Large Language Models (LLMs), and generates a downloadable fact-check report.

---

## 🚀 Objective

Marketing reports, research documents, and business presentations often contain outdated or inaccurate information.

This application acts as a **Truth Layer** by:

* Extracting factual claims from PDFs
* Searching live web sources
* Verifying claim accuracy
* Flagging misinformation
* Generating a downloadable report

---

## ✨ Features

* 📄 Upload any PDF document
* 🧠 Automatically extract factual claims
* 🌐 Search live web sources using Tavily
* 🤖 Verify claims using OpenAI GPT
* ✅ Label claims as Verified
* ⚠️ Label outdated information as Inaccurate
* ❌ Label unsupported claims as False
* 📥 Download the final report as CSV

---

## 🏗️ System Architecture

```text
User
 ↓
Upload PDF
 ↓
PDF Text Extraction
 ↓
Claim Extraction
 ↓
Live Web Search
 ↓
Fact Verification
 ↓
Report Generation
 ↓
Download Results
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### AI Model

* OpenAI GPT-4o-mini

### Web Search

* Tavily Search API

### PDF Processing

* PyPDF

### Data Handling

* Pandas

### Language

* Python

---

## 📂 Project Structure

```text
fact_check_agent/

│

app.py

requirements.txt

README.md

.gitignore

src/

│

pdf_loader.py

claim_extractor.py

web_search.py

verifier.py

utils.py

.streamlit/

secrets.toml
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository_url>

cd fact_check_agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
.\venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Keys

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
OPENAI_API_KEY="your_openai_api_key"

TAVILY_API_KEY="your_tavily_api_key"
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 📊 Output

The application generates a report containing:

* Claim
* Verification Status
* Reason
* Corrected Fact
* Source URL

Verification Categories:

* ✅ Verified
* ⚠️ Inaccurate
* ❌ False

---

## 🔮 Future Improvements

* Multi-language support
* Confidence score for each claim
* Source ranking system
* Support for DOCX and TXT files
* Enhanced trusted-source filtering

---

## 👨‍💻 Author

Roshan Kumar
