import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

# ----------------------------
# Streamlit Page Configuration
# ----------------------------
st.set_page_config(
    page_title="NareshIT Bot using LangChain, Ollama & DeepSeek-R1",
    page_icon="🤖"
)

st.title("🤖 NareshIT Bot using Ollama")
st.write("Ask me anything!")

# ----------------------------
# Prompt Template
# ----------------------------
prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant.

Question:
{question}

Answer:
""")

# ----------------------------
# Load Ollama Model
# ----------------------------
llm = OllamaLLM(
    model="deepseek-r1"
)

# Create Chain
chain = prompt | llm

# ----------------------------
# User Input
# ----------------------------
question = st.text_input("Enter your question")

# ----------------------------
# Generate Response
# ----------------------------
if st.button("Ask"):

    if question.strip():

        with st.spinner("Thinking..."):

            try:
                response = chain.invoke(
                    {"question": question}
                )

                st.success("Answer")
                st.write(response)

            except Exception as e:
                st.error(f"Error: {e}")

    else:
        st.warning("Please enter a question.")