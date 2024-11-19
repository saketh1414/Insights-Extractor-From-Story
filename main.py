import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()


GROQ_API_KEY=os.getenv("GROQ_API_KEY")

# Initialize the LLM
llm = ChatGroq(
    model_name="llama-3.1-70b-versatile",
    temperature=0,
    groq_api_key=GROQ_API_KEY
)

# Define Prompt Template
prompt_template = PromptTemplate.from_template(
    """
    You are an AI that specializes in extracting insights. A user has provided a long story containing diverse topics. 
    Focus only on extracting specific insights as per the user's instructions.

    Story:
    {story}

    User's Request:
    {query}

    Provide clear and concise insights based on the request.
    """
)

# Define Chain
chain = LLMChain(llm=llm, prompt=prompt_template)

# Streamlit App Interface
st.title("Key Insights Extractor")
st.subheader("Analyze a long story and extract specific insights.")

# Input Fields
story_input = st.text_area("Paste the long story here:", height=200)
query_input = st.text_input("Enter the type of insights you want (e.g., Productivity):")

# Generate Insights
if st.button("Extract Insights"):
    if story_input and query_input:
        response = chain.run({"story": story_input, "query": query_input})
        st.subheader("Extracted Insights:")
        st.write(response)
    else:
        st.error("Please provide both the story and the type of insights you want.")
