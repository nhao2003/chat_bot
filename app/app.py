from flask import Flask, jsonify, request
from flask_cors import CORS
from database import get_search_result
from ai import generate_response

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/generate', methods=['POST'])
def chatbot():
    data = request.get_json()
    query = data.get('query', '')
    # If trimmed query is empty, return an error response
    if not query.strip():
        return jsonify({"response": "Invalid query. Please provide a valid query."})

    # Generate search results based on the user query
    search_result = get_search_result(query)
    
    for result in search_result:
        result['id'] = str(result.pop('_id'))

    # Execute the LLMChain to generate response
    print(search_result)
    try:
        result = generate_response(query, search_result)
        return jsonify({
            "response": result,
            "result": search_result
        })
    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Error: {e}")
        return jsonify({
            "response": "An error occurred while generating response. Please try again.",
            "result": search_result  # Use a proper key here
        })

@app.route('/')
def index():
    return "Welcome to the AI Chatbot API!"

if __name__ == '__main__':
    app.run(port=8683, host="0.0.0.0", debug=True)
