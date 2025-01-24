# AI-Research-Agent

### An Autonomous AI Research Assistant; A full-stack demonstration of an Agentic AI system capable of:

Searching the web for relevant articles (via Bing Search API).
Scraping page contents with BeautifulSoup.
Summarizing text using T5-Small (Hugging Face Transformers).
Storing query and summary data in a MySQL database.
Allowing both a REST API (for Postman or programmatic clients) and a web frontend with a simple HTML form and CSS styling.


### Agentic AI Workflow

- Save initial query in DB.
- Search with Bing.
- Scrape each result.
- Summarize the combined text.
- Store the final summary in DB.
- Return a result dictionary containing:
   - `query_id`: The unique identifier for the query.
   - `summary`: The generated summary.
   - `references`: A list of referenced URLs.


### Core Components:

- Bing API; Using **Bing Search v7** that searches and returns top results in JSON form.
- Web Scraper; Using **BeautifulSoup** to extract text. 
- Summarizer; Using **T5-Small model** from Hugging Face that summarizes combined text (snippet + page).
- Database; **MySQL** to store queries and results.


### Files Architecture:

- *app/search_api.py*: handles Bing search.
- *app/agent.py*: orchestrates search → scrape → summarize → store.
- *app/db_connection.py*: manages MySQL connection & CRUD.
- *app/summarizer.py*: sets up the T5-Small pipeline.
- *app/main.py*: defines the Flask routes (API + basic frontend).
- *db_setup.py*: Script to create MySQL tables.
- *requirements.txt*: Python dependencies.
- *templates/ + static/*: For Flask’s HTML and CSS files.

---

## Requirements & Installation

If you would like to try it out:
- Clone the Repo:
git clone https://github.com/yahyasultanch/AI-Research-Agent.git

- Create & Activate a Virtual Environment.

- Install Dependencies:
pip install -r requirements.txt

- Create a file named .env (excluded from Git via .gitignore) with:
BING_API_KEY=YOUR_BING_API_KEY
DB_HOST=localhost
DB_USER=root
DB_PASS=your_password
DB_NAME=db_name

- Run the db_setup.py script once to create tables:
python db_setup.py

- Run the application(Inside the project folder (with venv activated)):
python -m app.main

**Flask will start at http://127.0.0.1:5000**

## Acknowledgements:
Microsoft Azure Bing Search V7 for adding intelligent search and returning relevant results: [https://azuremarketplace.microsoft.com/en-us/marketplace/apps/microsoft.bingsearch?tab=overview]
BeautifulSoup for Web Scraping: [https://www.crummy.com/software/BeautifulSoup/bs4/doc/]
T5-Small model from Hugging Face for text summarizing: [https://huggingface.co/google-t5/t5-small]
