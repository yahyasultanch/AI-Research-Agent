import requests
import os

BING_API_KEY = os.getenv("BING_API_KEY")
BING_URL = "https://api.bing.microsoft.com/v7.0/search"

def bing_web_search(query, count=5):
    headers = {
        "Ocp-Apim-Subscription-Key": BING_API_KEY,
        "Ocp-Apim-Subscription-Region": "global"
    }

    params = {
        "q": query,
        "count": count
    }
    response = requests.get(BING_URL, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        web_pages = data.get("webPages", {}).get("value", [])
        return web_pages
    else:
        print(f"Error: Bing API returned {response.status_code}")
        return []
