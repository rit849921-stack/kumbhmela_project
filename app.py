import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import random
import requests

# Load demo data
locations = pd.read_csv("data/locations.csv")
faqs = pd.read_csv("data/faqs.csv")

st.set_page_config(page_title="KumbhMela AI Assistant", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Crowd Prediction", "Map & Geo-tags", "Help Desk", "Weather"])

if page == "Home":
    st.title("🕉️ Kumbh Mela AI Assistant")
    st.write("Welcome to the AI-powered Kumbh Mela Assistant. This app helps manage crowd, safety, and guidance.")
    st.metric("Total Locations", len(locations))
    st.metric("FAQs Available", len(faqs))

elif page == "Crowd Prediction":
    st.title("📊 Crowd Prediction")
    ghat = st.selectbox("Select Ghat", locations[locations['type']=="ghat"]["name"].tolist())
    if st.button("Predict Crowd"):
        crowd = random.randint(1000, 10000)
        st.success(f"Predicted crowd at {ghat}: {crowd} people")

elif page == "Map & Geo-tags":
    st.title("🗺️ Map of Kumbh Mela")
    m = folium.Map(location=[25.4358, 81.8463], zoom_start=13)
    for _, row in locations.iterrows():
        folium.Marker([row['lat'], row['lon']], popup=f"{row['type'].capitalize()}: {row['name']}").add_to(m)
    st_folium(m, width=700, height=500)

elif page == "Help Desk":
    st.title("❓ Help Desk")
    query = st.text_input("Enter your question")
    if st.button("Search"):
        matches = faqs[faqs['question'].str.contains(query, case=False, na=False)]
        if not matches.empty:
            for _, row in matches.iterrows():
                st.write(f"**Q:** {row['question']}")
                st.write(f"**A:** {row['answer']}")
        else:
            st.error("No matching FAQ found.")

elif page == "Weather":
    st.title("⛅ Weather Updates")
    city = st.text_input("Enter City", "Prayagraj")
    if st.button("Get Weather"):
        try:
            url = f"https://wttr.in/{city}?format=j1"
            res = requests.get(url).json()
            temp = res['current_condition'][0]['temp_C']
            desc = res['current_condition'][0]['weatherDesc'][0]['value']
            st.success(f"Weather in {city}: {temp}°C, {desc}")
        except:
            st.error("Weather API not available. Try again.")
