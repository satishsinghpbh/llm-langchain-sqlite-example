import streamlit as st

st.title("GenAI Trade Query Assistant")

user_input = st.text_input("Ask a trade-related question")

if user_input:
    response = agent_executor.run(user_input)
    st.write(response)
