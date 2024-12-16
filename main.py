import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyC2QatxVEu6O_J0vynLVgODEhPCGRI1mig")

result = genai.embed_content(
        model="models/text-embedding-004",
        content="What is the meaning of life?")

# print(str(result['embedding']))
print(len(result['embedding']))