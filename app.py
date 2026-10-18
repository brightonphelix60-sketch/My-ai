
import streamlit as st

st.set_page_config(page_title="My AI", page_icon="🤖")
st.title("🤖 My AI - Ask Me Anything!")

st.write("Hello! I am your AI created in Eldoret. Ask me anything!")

user_question = st.text_input("Your question:")

if user_question:
    st.write("### 🤖 My Answer:")
    if "hello" in user_question.lower():
        st.write("Hello bro! How can I help you?")
    elif "who are you" in user_question.lower():
        st.write("I am an AI created by you! I can answer questions.")
    elif "name" in user_question.lower():
        st.write("You can give me a name! What should we call me?")
    else:
        st.write(f"You asked: '{user_question}'")
        st.write("That's a great question! I am still learning, but I will try my best to help you with that.")
        
st.write("---")
st.write("Created with ❤️ in Kenya")
```
