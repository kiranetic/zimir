import streamlit as st
from auth import login, register
from dashboard import dashboard
from categories import categories
from transactions import transactions

def main():
    st.set_page_config(page_title="Zimir", layout="centered")

    if "access_token" not in st.session_state:
        st.session_state["access_token"] = None
    if "show_register" not in st.session_state:
        st.session_state["show_register"] = False

    st.title("Zimir - Personal Finance")

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
        tabs = st.tabs(["📊 Dashboard", "📑 Transactions", "📁 Categories"])

        with tabs[0]:
            dashboard()
        with tabs[1]:
            transactions()
        with tabs[2]:
            categories()

        st.sidebar.success(f"Logged in as: {st.session_state['user_email']}")
        if st.sidebar.button("Logout"):
            st.session_state.clear()
            st.rerun()

if __name__ == "__main__":
    main()
