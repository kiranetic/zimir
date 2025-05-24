import streamlit as st
import requests
from config import API_URL

def dashboard():
    st.subheader("📊 Dashboard")

    headers = {"Authorization": f"Bearer {st.session_state['access_token']}"}
    response = requests.get(f"{API_URL}/transactions/", headers=headers)

    if response.status_code == 200:
        transactions = response.json()

        income = 0.0
        expense = 0.0

        for txn in transactions:
            try:
                amount = float(txn.get('amount', 0))
            except (ValueError, TypeError):
                continue  # Skip invalid amounts

            if txn.get('type') == 'income':
                income += amount
            elif txn.get('type') == 'expense':
                expense += amount

        balance = income - expense

        st.metric("💰 Total Income", f"₹{income}")
        st.metric("💸 Total Expense", f"₹{expense}")
        st.metric("📦 Balance", f"₹{balance}")
    else:
        st.error("Failed to fetch transactions.")
