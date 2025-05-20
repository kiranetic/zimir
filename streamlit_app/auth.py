import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"

def login():
    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        response = requests.post(f"{API_BASE_URL}/login/", json={"email": email, "password": password})

        if response.status_code == 200:
            data = response.json()
            st.session_state["access_token"] = data["access_token"]
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Login failed. Please check your credentials.")
