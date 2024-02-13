import streamlit as st 
from medium import get_medium
from emails import get_mail_content,logout
from GeminiAPI import Gemini_login, gemini_medium_prompt,model_msg,gemini_email_prompt,clear_history

st.set_page_config(page_title="Project Aida",
                   page_icon=":bridge_at_night:",
                   layout="wide")

st.markdown("# :rainbow[Aida: Personal AI Assistant]")

if st.button(label="clear chat"):
    st.session_state["messages"] = []
    clear_history()

# Initialize chat history 
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display message in chat history on rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        clear_history()

def chat_completion(input,reply):    
    # Add user message to chat history
    st.session_state.messages.append({"role":"user", "content": input})
    # Display user message in chat message container
    with st.chat_message("user"):
         st.markdown(input)

    # display assistant response in chat container 
    st.session_state.messages.append({"role":"assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)

# react to user input 
# := is actually a valid operator that allows for assignment of variables  within expressions:
if input :=st.chat_input("Enter your question"): 
    reply = model_msg(input)
    chat_completion(input,reply)

st.sidebar.write("# About")
if st.sidebar.button("Login"):
    Gemini_login()
    
if st.sidebar.button(label="Medium"):
        st.chat_message("user").markdown("Today's top medium articles")
        st.session_state.messages.append({"role":"user", "content": "Today's top medium articles"})

        body = get_medium()
        reply = gemini_medium_prompt(body)
        chat_completion(input,reply)

if st.sidebar.button(label="Email"):
        st.chat_message("user").markdown("Today's top emails in inbox")
        st.session_state.messages.append({"role":"user", "content": "Today's top emails in inbox"})
        body = get_mail_content()
        reply = gemini_email_prompt(body)
        chat_completion(input,reply)

if st.sidebar.button(label="logout"):
     logout()
