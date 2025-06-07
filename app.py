import streamlit as st
from PIL import Image
import random

# App configuratie
st.set_page_config(
    page_title="Bijbel Quiz voor Kinderen",
    page_icon="⛪",
    layout="wide"
)

# Initialiseer score en voortgang
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0

# Bijbelquizvragen
vragen = [
    {
        "vraag": "Wie bouwde een ark omdat God het vroeg?",
        "opties": ["Mozes", "Noach", "Jona", "David"],
        "antwoord": "Noach",
        "image": "https://cdn.pixabay.com/photo/2023/02/23/22/40/ark-7809897_640.jpg"
    },
    {
        "vraag": "Wie zat in de buik van een grote vis?",
        "opties": ["Jezus", "Jona", "Paulus", "Petrus"],
        "antwoord": "Jona",
        "image": "https://cdn.pixabay.com/photo/2020/01/28/01/08/whale-4796907_640.jpg"
    },
    {
        "vraag": "Wat gaf Jezus aan 5000 mensen om te eten?",
        "opties": ["Brood en vis", "Melk en honing", "Appels", "Water"],
        "antwoord": "Brood en vis",
        "image": "https://cdn.pixabay.com/photo/2017/08/01/08/29/fish-2561904_640.jpg"
    }
