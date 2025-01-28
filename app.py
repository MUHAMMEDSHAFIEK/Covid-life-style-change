import streamlit as st
#Title of the web app
st.title("my first stramlit App")
# Text input for the user
name=st.text_input("enter you namee:")
# Butten no triger an action
if st.button("say hello"):
    st.write(f"hello,{name}!")
