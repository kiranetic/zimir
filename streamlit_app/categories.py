import streamlit as st
import requests
from config import API_URL

def categories():
    st.subheader("📁 Categories")
    headers = {"Authorization": f"Bearer {st.session_state['access_token']}"}

    # List existing categories
    resp = requests.get(f"{API_URL}/categories/", headers=headers)
    if resp.status_code == 200:
        cats = resp.json()
        for cat in cats:
            st.write(f"- **{cat['name']}** ({cat['type']}) - {cat.get('description', '')}")
    else:
        st.error("Could not fetch categories.")

    st.divider()

    # Add new category
    st.subheader("➕ Add Category")
    name = st.text_input("Category Name")
    type_ = st.selectbox("Type", ["income", "expense"], key="category_type_selectbox")
    desc = st.text_input("Description (optional)")

    if st.button("Add Category"):
        data = {"name": name, "type": type_, "description": desc}
        r = requests.post(f"{API_URL}/categories/", json=data, headers=headers)
        if r.status_code == 200:
            st.success("Category added successfully!")
            st.rerun()
        else:
            st.error(f"Failed to add category: {r.text}")
