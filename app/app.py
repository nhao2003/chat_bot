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
    source_information = get_search_result(query)

    # Execute the LLMChain to generate response
    result = promt_chain.run(query=query, source_information=source_information)
    return jsonify({"response": result})


if __name__ == '__main__':
    app.run(debug=True)
