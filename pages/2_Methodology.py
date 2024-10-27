import streamlit as st
from pathlib import Path

st.set_page_config(page_title = "Methodology 📖")
st.title("Methodology 📖")
st.sidebar.success("Current Page: Methodology 📖")

with st.expander("Chatbot"):
    st.write("The following is the methodology for Chatbot")
    st.image(str(Path.cwd() / 'Chat.jpg'))

with st.expander("Are you Ready For A Pet"):
    st.write("The following is the methodology for the page 'Are you Ready For A Pet'")
    st.image(str(Path.cwd() / 'Quiz.jpg'))
    
with st.expander("Getting A Pet"):
    st.write("The following is the methodology for the page 'Getting A Pet'")
    st.image(str(Path.cwd() / 'maps.jpg'))