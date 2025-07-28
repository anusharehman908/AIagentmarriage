
import streamlit as st
import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai
# from streamlit_extras.let_it_rain import rain

# ========== CONFIG ========== #
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ULTRAMSG_INSTANCE_ID = os.getenv("ULTRAMSG_INSTANCE_ID")
ULTRAMSG_TOKEN = os.getenv("ULTRAMSG_TOKEN")

genai.configure(api_key=GEMINI_API_KEY)

# ========== FUNCTIONS ========== #
def ask_gemini(prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    return response.text

def send_whatsapp_message(phone_number, message):
    url = f"https://api.ultramsg.com/{ULTRAMSG_INSTANCE_ID}/messages/chat"
    payload = {
        "token": ULTRAMSG_TOKEN,
        "to": phone_number,
        "body": message
    }
    response = requests.post(url, data=payload)
    return response.json()

# ========== USER DATA ========== #
users = [
    {"name": "Ali", "age": 22, "gender": "male"},
    {"name": "Zavian", "age": 25, "gender": "male"},
    {"name": "Maaz", "age": 24, "gender": "male"},
    {"name": "Shaheer", "age": 28, "gender": "male"},
    {"name": "Taha", "age": 23, "gender": "male"},
    {"name": "Aahil", "age": 21, "gender": "male"},
    {"name": "Arham", "age": 26, "gender": "male"},
    {"name": "Uzair", "age": 24, "gender": "male"},
    {"name": "Zohair", "age": 29, "gender": "male"},
    {"name": "Ali", "age": 25, "gender": "male"},
    {"name": "Alveena", "age": 23, "gender": "female"},
    {"name": "Ishal", "age": 20, "gender": "female"},
    {"name": "Areeba", "age": 29, "gender": "female"},
    {"name": "Yumna", "age": 26, "gender": "female"},
    {"name": "Rania", "age": 25, "gender": "female"},
    {"name": "Eshal", "age": 22, "gender": "female"},
    {"name": "Aleha", "age": 27, "gender": "female"},
    {"name": "Faryal", "age": 24, "gender": "female"},
    {"name": "Sehrish", "age": 28, "gender": "female"},
    {"name": "Mahira", "age": 23, "gender": "female"},
]

# ========== STREAMLIT UI ========== #
st.set_page_config(page_title="💍 Marriage Bureau", layout="centered")

# ========== Custom CSS & Banner ========== #
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to right, #fff5f8, #fbe7ff, #fffbdc);
        padding: 2rem;
    }

    .banner {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 1.5rem;
    }

    .banner img {
        max-width: 25%;
        height: auto;
        border-radius: 18px;
        box-shadow: 0px 6px 15px rgba(0,0,0,0.15);
    }

    .center-title {
        text-align: center;
        font-size: 5vw;
        font-weight: bold;
        color: #c2185b;
        font-family: 'Segoe UI', sans-serif;
        margin-top: 0.75rem;
        text-shadow: 1px 1px 2px #fff;
    }

    h3 {
        color: #6a1b9a;
    }

    label, .stSlider, .stTextInput {
        color: #4a148c !important;
        font-weight: 600;
    }

    @media (max-width: 768px) {
        .center-title {
            font-size: 6.5vw;
        }
    }
    </style>

    <div class="banner">
        <img src='https://tse1.mm.bing.net/th/id/OIP.XSegwM_A-Vy6pAGa6GMP8gHaK_?r=0&rs=1&pid=ImgDetMain&o=7&rm=3' alt="Marriage Bureau Banner" />
    </div>
    <div class="center-title">💍Marriage Bureau💍 </div>
""", unsafe_allow_html=True)

# Rain Effect
rain(emoji="❤️", font_size=20, falling_speed=5, animation_length="infinite")

# ========== Form ========== #
st.markdown("### 🗘️ Fill your details to find a perfect match:")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Your Name 👤")
    age = st.number_input("Your Age 🎂", min_value=18, max_value=100, step=1)
with col2:
    gender = st.selectbox("Your Gender 🛋", ["male", "female"])
    phone = st.text_input("WhatsApp Number 📱 (e.g. +92...)")

min_age = st.slider("Minimum age for your match 🎯", 18, 40, 24)

if st.button("🔍 Find My Match"):
    if name and phone:
        matches = [u for u in users if u["age"] >= min_age and u["gender"] != gender]

        if matches:
            match = matches[0]
            prompt = f"{name} ({age}) ko {min_age}+ ki {'ladki' if gender == 'male' else 'ladka'} ka rishta chahiye. Mil gaya match: {match['name']} ({match['age']}). Thoda romantic aur narm lehja likho."
            ai_response = ask_gemini(prompt)

            final_message = f"💘 Rishta Mil Gaya!\n{name} ({age}) ne dil se dhoonda aur mila: {match['name']} ({match['age']})\n\n📩 Paighaam-e-Mohabbat: {ai_response}\n\n✨ Mirage Bureau – Jahan dil milte hain."

            st.success("🎯 Match Found!")
            st.markdown(f"**✨ AI Suggestion:** {ai_response}")

            whatsapp_response = send_whatsapp_message(phone, final_message)
            st.info(f"📩 WhatsApp Sent: {whatsapp_response}")
        else:
            st.warning("😢 Sorry, koi suitable match nahi mila.")
    else:
        st.error("⚠️ Please fill in all the fields!")





