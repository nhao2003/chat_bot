from flask import Flask, jsonify, request
from database import get_search_result
from ai import promt_chain

# Initialize Flask app
app = Flask(__name__)


@app.route('/generate', methods=['POST'])
def chatbot():
    data = request.get_json()
    query = data.get('query', '')
    # If trimmed query is empty, return an error response
    if not query.strip():
        return jsonify({"response": "Invalid query. Please provide a valid query."})

    # Generate search results based on the user query
    search_result, ids = get_search_result("Python programming")

    # Execute the LLMChain to generate response
    result = promt_chain.run(query=query, source_information=search_result)
    return jsonify({"response": result,
                    "ids": ids,})


if __name__ == '__main__':
    app.run(debug=True)
