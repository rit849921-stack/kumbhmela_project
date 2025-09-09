
import streamlit as st

st.set_page_config(page_title="Kumbh Mela Prayagraj 2025", layout="wide")

st.markdown("<h1 style='text-align: center; color: orange;'>🕉️ Kumbh Mela Prayagraj 2025</h1>", unsafe_allow_html=True)

st.sidebar.title("Navigation")
pages = ["Home", "Lost & Found", "Devotee Tracker", "Crowd Prediction", "Map", "Help Desk", "Weather", "Chat", "Admin"]
choice = st.sidebar.radio("Go to", pages)

st.success("This is a demo placeholder. Full advanced code will handle Lost & Found, Devotee Tracker, Map, etc.")
