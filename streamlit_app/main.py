import streamlit as st
from auth import login

def main():
    st.set_page_config(page_title="Zimir", layout="wide")

    if "access_token" not in st.session_state:
        login()
    else:
        st.success("You are logged in!")
        # Placeholder for tabs, to be implemented next

if __name__ == "__main__":
    main()
