import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Retail Analytics Dashboard", layout="wide")

st.title("📊 Retail Analytics Dashboard")

powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=bd2825e8-f17d-4bba-98c3-c9d8f9eb2d82&autoAuth=true&ctid=d4963ce2-af94-4122-95a9-644e8b01624d"
components.iframe(
    powerbi_url,
    width=1200,
    height=700,
    scrolling=True
)
