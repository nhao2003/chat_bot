import pymongo
from embedding import get_embedding
from environment import MONGO_URI


def get_mongo_client(mongo_uri):
    """
    Establish connection to MongoDB using the provided URI.

    Args:
        mongo_uri (str): MongoDB connection URI.

    Returns:
        pymongo.MongoClient: MongoDB client instance.
    """
    try:
        # Connect to MongoDB
        print(mongo_uri)
        client = pymongo.MongoClient(mongo_uri, appname="devrel.content.python")
        print("Connection to MongoDB successful")
        return client
    except pymongo.errors.ConnectionFailure as e:
        print(f"Connection failed: {e}")
        return None


# Establish MongoDB connection
mongo_client = get_mongo_client(MONGO_URI)

# MongoDB database and collection
db = mongo_client["iconic"]
collection = db["products"]


def vector_search(user_query):
    """
    Perform vector search based on the user query using MongoDB aggregation pipeline.

    Args:
        user_query (str): User query for vector search.
        collection (pymongo.collection.Collection): MongoDB collection to search.

    Returns:
        list: Search results.
    """
    # Generate embedding for the user query
    query_embedding = get_embedding(user_query)

    if query_embedding is None:
        return "Invalid query or embedding generation failed."

    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",
                "queryVector": query_embedding,
                "path": "embedding",
                "exact": True,
                "limit": 5
            }
        },
        {
            "$addFields": {  # Thêm trường "score" vào kết quả hiện có
                "score": {
                    "$meta": "vectorSearchScore"
                }
            }
        },
        {
            "$project": {  # Loại bỏ trường "embedding" khỏi kết quả
                "embedding": 0
            }
        }
    ]



    # Execute the search
    results = collection.aggregate(pipeline)
    return list(results)


def get_search_result(query):
    """
    Get search results based on the user query.

    Args:
        query (str): User query for search.
        collection (pymongo.collection.Collection): MongoDB collection to search.

    Returns:
        str: Formatted search results.
    """
    # Perform vector search
    knowledge = vector_search(query)

    # Format search results
    
    if not knowledge:
        return "No relevant books were found."
    else:
        return knowledge

