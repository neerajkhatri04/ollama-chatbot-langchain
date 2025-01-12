import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith monitoring
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "QnA Chatbot with OLLAMA"

##Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system","Act like a AI chatbot. Help with user question."),
    ("user","Question:{question}"),
])

def gen_response(question, engine, temperature,max_tokens):
    ## llm model
    llm = OllamaLLM(model=engine, temperature=temperature, max_tokens=max_tokens)
    ## output parser
    output_parser = StrOutputParser()
    ## LCEL chain
    chain = prompt | llm | output_parser
    ## Invoking the chain
    ans = chain.invoke({"question": question})
    return ans


st.title("QnA Chatbot with OLLAMA")

engine = st.sidebar.selectbox("Select Engine", ["llama2"])

temperature = st.sidebar.slider("Creativity", 0.0, 1.0, 0.5, 0.1)
max_tokens = st.sidebar.slider("Max output length", 10, 200, 50, 10)

st.write("Ask your question")
user_input = st.text_input("Question:")

if user_input:
    response = gen_response(user_input, engine, temperature, max_tokens)
    st.write(response)
else: 
    st.write("Please enter a question")
