import streamlit as st
import requests
from config import API_URL

def login():
    st.subheader("Login")

    email = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login"):
        if not email or not password:
            st.warning("Please enter email and password")
            return

        response = requests.post(f"{API_URL}/login/", json={"email": email, "password": password})

        if response.status_code == 200:
            data = response.json()
            st.session_state["access_token"] = data["access_token"]
            st.session_state["user_email"] = email
            st.rerun()
        else:
            st.error("Login failed. Please check your credentials.")

def register():
    st.subheader("Register")

    email = st.text_input("Email", key="register_email")
    password = st.text_input("Password", type="password", key="register_password")

    if st.button("Register"):
        if not email or not password:
            st.warning("Please enter email and password")
            return

        response = requests.post(f"{API_URL}/users/", json={"email": email, "password": password})

        if response.status_code == 200:
            st.success("Registration successful. You can now log in.")
            st.session_state["show_register"] = False
            st.rerun()
        else:
            st.error(f"Registration failed: {response.text}")
