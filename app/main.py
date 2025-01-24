# app/main.py
from flask import Flask, request, jsonify
from app.agent import Agent
from app.db_connection import get_results
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
agent = Agent()

@app.route("/api/search", methods=["POST"])
def search_endpoint():
    """
    Expects JSON: { "query": "some topic" }
    Returns JSON with summary, references, and query_id
    """
    data = request.get_json()
    query_text = data.get("query")
    if not query_text:
        return jsonify({"error": "No query provided"}), 400
    
    result = agent.handle_query(query_text)
    return jsonify(result), 200

@app.route("/api/results/<int:query_id>", methods=["GET"])
def get_results_endpoint(query_id):
    """
    Retrieve results from the database for a given query_id
    """
    rows = get_results(query_id)
    if not rows:
        return jsonify({"message": "No results found for this query_id"}), 404
    
    # Return an array of results (though we typically store only one summary)
    response = []
    for row in rows:
        summary, references, timestamp = row
        response.append({
            "summary": summary,
            "references": references,
            "timestamp": str(timestamp)
        })
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
