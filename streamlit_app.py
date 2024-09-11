import streamlit as st

from streamlit_option_menu import option_menu

st.title("🎈 WQ's Interest Calculator")

st.write(
    "Calculates the interest and final amount owed based on start and end dates, interest and starting amount owed."
)
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["All Interest", "Norgan", "Date Changes"],
    )

if selected == "All Interest":
    st.title(f"Interest Calculator")

if selected == "Norgan":
    st.title(f"Norgan Calculator")

if selected == "Date Changes":
    st.title(f"Date Change Calculator")

