# app/agent.py
from app.search_api import bing_web_search
from app.summarizer import summarize_text
from app.db_connection import save_query, save_result
import requests
from bs4 import BeautifulSoup

class Agent:
    def __init__(self):
        pass

    def handle_query(self, query_text):
        """
        1) Save the query in the DB
        2) Use Bing API to search
        3) For each result, fetch snippet or main text
        4) Summarize
        5) Combine the summarized results or pick top
        6) Save the final summary + references in the DB
        7) Return the summary
        """
        
        # Save the user query
        query_id = save_query(query_text)

        # Bing Web Search
        results = bing_web_search(query_text, count=5)

        combined_text = ""
        references = []

        for idx, res in enumerate(results):
            name = res.get('name')
            snippet = res.get('snippet')
            url = res.get('url')

            references.append(url) 
            page_text = self.scrape_webpage(url)

            if snippet:
                combined_text += f"\nSnippet: {snippet}\n"
            if page_text:
                combined_text += f"\nPage Extract: {page_text}\n"

        if not combined_text.strip():
            final_summary = "No substantial content found to summarize."
        else:
            # Summarize
            final_summary = summarize_text(combined_text, max_length=150, min_length=50)

        # Save final summary in the DB
        ref_str = "; ".join(references)
        save_result(query_id, final_summary, ref_str)

        response = {
            "query_id": query_id,
            "summary": final_summary,
            "references": references
        }
        return response
    
    def scrape_webpage(self, url):
        """
        Fetches the webpage content and extracts main text.
        We'll keep it simple by returning the title or a short chunk.
        """
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")

                paragraphs = soup.find_all('p')
                text_chunks = [p.get_text() for p in paragraphs]
                joined_text = " ".join(text_chunks[:3])
                return joined_text
            else:
                return ""
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return ""
