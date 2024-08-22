import streamlit as st
import google.generativeai as genai


st.title("chat bot")

genai.configure(api_key="AIzaSyDCz4iaS2xRP5vEKW0lqQphjbW8G670LCo")  #to get api-key https://aistudio.google.com/app/apikey

text = st.text_input("enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)

if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button('Increment'):
    st.session_state.counter += 1


if st.button('Clean'):
    st.session_state.counter = 0


st.write('Counter:', st.session_state.counter)