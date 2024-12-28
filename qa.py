import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()
import google.generativeai as genai

# Configure the Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

# Function to get a response from Gemini
def get_gemini_response(question):
    response = chat.send_message(question)
    return "".join(chunk.text for chunk in response)

# Streamlit page configuration
st.set_page_config(page_title="Q&A Bot")
st.header("Gemini LLM Application")

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input field and button
input_question = st.text_input("Input: ", key="input")
submit = st.button("Ask the Question")

# Handle submission
if submit and input_question:
    response = get_gemini_response(input_question)
    # Append the question and response to chat history
    st.session_state['chat_history'].append(("You", input_question))
    st.session_state['chat_history'].append(("Bot", response))
    # Display the response
    st.subheader("The Response is")
    st.write(response)

# Display chat history
st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
