from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from prompt import prompt_template

# Initialize Google Generative AI model
llm = ChatGoogleGenerativeAI(model='gemini-pro')
promt_chain = LLMChain(llm=llm, prompt=prompt_template, verbose=True)