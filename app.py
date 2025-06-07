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
    },
    {
        "vraag": "Wie liep op het water naar Jezus toe?",
        "opties": ["Petrus", "Johannes", "Thomas", "Paulus"],
        "antwoord": "Petrus",
        "image": "https://cdn.pixabay.com/photo/2020/11/02/16/52/sea-5707326_640.jpg"
    },
    {
        "vraag": "Wat maakte God op de eerste dag?",
        "opties": ["Zon en maan", "Licht", "Dieren", "Planten"],
        "antwoord": "Licht",
        "image": "https://cdn.pixabay.com/photo/2018/02/07/10/25/background-3135151_640.jpg"
    },
    {
        "vraag": "Wie kreeg de tien geboden van God?",
        "opties": ["Mozes", "Abraham", "Noach", "Jozef"],
        "antwoord": "Mozes",
        "image": "https://cdn.pixabay.com/photo/2021/01/28/12/33/tablets-5957316_640.jpg"
    }
]

# Vragen schudden
if 'shuffled_vragen' not in st.session_state:
    st.session_state.shuffled_vragen = random.sample(vragen, len(vragen))

# Titel en score
st.title("📖 Leuke Bijbelquiz voor Kinderen")
st.subheader(f"Score: {st.session_state.score} / {len(vragen)}")
st.write("Lees de vraag en kies het juiste antwoord.")

# Toon de vraag
if st.session_state.current_question < len(st.session_state.shuffled_vragen):
    vraag_data = st.session_state.shuffled_vragen[st.session_state.current_question]

    col1, col2 = st.columns(2)
    with col1:
        st.image(vraag_data["image"], width=300)
    with col2:
        st.markdown(f"## {vraag_data['vraag']}")
        gekozen_antwoord = st.radio(
            "Kies je antwoord:",
            vraag_data["opties"],
            key=f"vraag_{st.session_state.current_question}"
        )

        if st.button("Controleer antwoord"):
            if gekozen_antwoord == vraag_data["antwoord"]:
                st.session_state.score += 1
                st.balloons()
                st.success(f"Goed gedaan! 🎉 Het juiste antwoord is: {vraag_data['antwoord']}")
            else:
                st.error(f"Oeps! Het goede antwoord is: {vraag_data['antwoord']}")

            st.session_state.current_question += 1
            st.rerun()

else:
    st.balloons()
    st.success("🎉 Je hebt de quiz helemaal afgerond!")
    st.subheader(f"Eindscore: {st.session_state.score} van de {len(vragen)} goed!")

    if st.button("Speel opnieuw"):
        st.session_state.clear()
        st.rerun()

# Styling
st.markdown("""
<style>
    .stButton>button {
        background-color: #90EE90;
        color: black;
        font-weight: bold;
    }
    .stSuccess {
        font-size: 20px !important;
    }
</style>
""", unsafe_allow_html=True)
