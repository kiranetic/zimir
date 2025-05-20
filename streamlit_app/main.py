import streamlit as st
from auth import login, register

def main():
    st.set_page_config(page_title="Zimir", layout="centered")

    # First-time state initialization
    if "access_token" not in st.session_state:
        st.session_state["access_token"] = None
    if "show_register" not in st.session_state:
        st.session_state["show_register"] = False

    st.title("Zimir - Personal Finance")

    # Auth check
    if not st.session_state["access_token"]:
        if st.session_state["show_register"]:
            register()
            if st.button("← Back to Login"):
                st.session_state["show_register"] = False
                st.rerun()
        else:
            login()
            if st.button("Create new account"):
                st.session_state["show_register"] = True
                st.rerun()
    else:
        st.success(f"Welcome, {st.session_state['user_email']}!")
        st.write("You are logged in.")
        if st.button("Logout"):
            st.session_state.clear()
            st.rerun()

if __name__ == "__main__":
    main()
