import streamlit as st
import requests
from config import API_URL
from datetime import datetime

def transactions():
    st.subheader("📑 Transactions")
    headers = {"Authorization": f"Bearer {st.session_state['access_token']}"}

    # View transactions
    r = requests.get(f"{API_URL}/transactions/", headers=headers)
    if r.status_code == 200:
        txns = r.json()

        # Sort by timestamp descending
        try:
            txns.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
        except Exception as e:
            st.warning(f"Failed to sort transactions: {e}")

        for t in txns:
            name = t.get("name", "")
            amount = t.get("amount", 0)
            type_ = t.get("type", "")
            notes = t.get("notes", "")
            timestamp = t.get("timestamp", "")[:10]

            st.write(f"- ₹{amount} | **{name}** ({type_}) on {timestamp} – {notes}")
    else:
        st.error("Could not fetch transactions.")

    st.divider()

    # Add transaction
    st.subheader("➕ Add Transaction")
    name = st.text_input("Name")
    amount = st.number_input("Amount", step=0.01)
    type_ = st.selectbox("Type", ["income", "expense"], key="transaction_type_selectbox")
    notes = st.text_area("Notes (optional)")
    timestamp_date = st.date_input("Date")
    timestamp_time = st.time_input("Time")

    if st.button("Add Transaction"):
        full_timestamp = datetime.combine(timestamp_date, timestamp_time).isoformat()
        data = {
            "name": name,
            "amount": amount,
            "type": type_,
            "notes": notes,
            "timestamp": full_timestamp
        }
        r = requests.post(f"{API_URL}/transactions/", json=data, headers=headers)
        if r.status_code == 200:
            st.success("Transaction added!")
            st.rerun()
        else:
            st.error(f"Failed to add transaction: {r.text}")
