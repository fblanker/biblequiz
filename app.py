import streamlit as st
from PIL import Image
import random

# App configuratie
st.set_page_config(
    page_title="Leuke Bijbel Quiz",
    page_icon="⛪",
    layout="wide"
)

# Initialiseer de score en vragen
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0

# Kindvriendelijke Bijbelvragen
vragen = [
    {
        "vraag": "Wie maakte de dieren en de mensen?",
        "opties": ["Mozes", "Jezus", "God", "Abraham"],
        "antwoord": "God",
        "image": "https://cdn.pixabay.com/photo/2020/05/18/14/55/child-5187243_640.jpg"
    },
    {
        "vraag": "In welk dier zat Noach in de ark?",
        "opties": ["Een olifant", "Een giraf", "Een leeuw", "Alle dieren"],
        "antwoord": "Alle dieren",
        "image": "https://cdn.pixabay.com/photo/2017/09/25/13/14/dog-2785077_640.jpg"
    },
    {
        "vraag": "Wie werd in een mandje in de rivier gelegd?",
        "opties": ["Jezus", "Mozes", "David", "Maria"],
        "antwoord": "Mozes",
        "image": "https://cdn.pixabay.com/photo/2016/11/21/12/59/baby-1845614_640.jpg"
    },
    {
        "vraag": "Wie versloeg de reus Goliath?",
        "opties": ["Samson", "David", "Saul", "Jozua"],
        "antwoord": "David",
        "image": "https://cdn.pixabay.com/photo/2012/04/24/13/49/david-40742_640.png"
    },
    {
        "vraag": "Waar werd Jezus geboren?",
        "opties": ["In een paleis", "In een stal", "In een boot", "In een huis"],
        "antwoord": "In een stal",
        "image": "https://cdn.pixabay.com/photo/2017/12/24/18/48/nativity-scene-3037528_640.jpg"
    },
    {
        "vraag": "Wat gaf de goede herder aan zijn schaapjes?",
        "opties": ["Snoep", "Liefde en zorg", "Goud", "Een huis"],
        "antwoord": "Liefde en zorg",
        "image": "https://cdn.pixabay.com/photo/2017/10/20/11/22/sheep-2871915_640.jpg"
    }
]

# Schud de vragen als het een nieuw spel is
if 'shuffled_vragen' not in st.session_state:
    st.session_state.shuffled_vragen = random.sample(vragen, len(vragen))

# Header met score
st.title("⛪ Leuke Bijbel Quiz voor Jou!")
st.subheader(f"Score: {st.session_state.score} / {len(vragen)}")
st.write("Kies het goede antwoord!")

# Toon de huidige vraag
if st.session_state.current_question < len(st.session_state.shuffled_vragen):
    vraag_data = st.session_state.shuffled_vragen[st.session_state.current_question]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(vraag_data["image"], width=300)
    
    with col2:
        st.markdown(f"## {vraag_data['vraag']}")
        
        # Maak knoppen voor elke optie
        gekozen_antwoord = st.radio(
            "Kies je antwoord:",
            vraag_data["opties"],
            key=f"vraag_{st.session_state.current_question}"
        )
        
        if st.button("Antwoord controleren"):
            if gekozen_antwoord == vraag_data["antwoord"]:
                st.session_state.score += 1
                st.balloons()
                st.success(f"Goed zo! 🎉 Het antwoord is inderdaad: {vraag_data['antwoord']}")
            else:
                st.error(f"Bijna! Het goede antwoord is: {vraag_data['antwoord']}")
            
            st.session_state.current_question += 1
            if st.session_state.current_question < len(st.session_state.shuffled_vragen):
                st.experimental_rerun()
            else:
                st.balloons()
                st.success("🎉 Gefeliciteerd! Je hebt de quiz afgerond!")
                if st.button("Opnieuw spelen"):
                    st.session_state.score = 0
                    st.session_state.current_question = 0
                    st.session_state.shuffled_vragen = random.sample(vragen, len(vragen))
                    st.experimental_rerun()
else:
    st.balloons()
    st.success("🎉 Gefeliciteerd! Je hebt de quiz afgerond!")
    st.subheader(f"Eindscore: {st.session_state.score} van de {len(vragen)} goed!")
    
    if st.button("Opnieuw spelen"):
        st.session_state.score = 0
        st.session_state.current_question = 0
        st.session_state.shuffled_vragen = random.sample(vragen, len(vragen))
        st.experimental_rerun()

# Voeg wat leuke styling toe
st.markdown("""
<style>
    .stButton>button {
        background-color: #FFD700;
        color: black;
        font-weight: bold;
    }
    .stSuccess {
        font-size: 20px !important;
    }
</style>
""", unsafe_allow_html=True)
