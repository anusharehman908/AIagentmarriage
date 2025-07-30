
        import streamlit as st
import random

# Fake WhatsApp message sender (simulate sending)
def send_whatsapp_message(phone: str, message: str):
    # Simulate sending message
    return f"📨 Paighaam '{message}' bhej diya gaya number: {phone}"

# AI-style match response (Roman Urdu)
def generate_match_response(user_name, match_name, match_age, match_profession, match_city):
    responses = [
        f"Salam {user_name}! Humne aap ke liye ek acha rishta dhoond lia hai: {match_name}, {match_age} saal ka, {match_profession}, {match_city} se.",
        f"Assalamualaikum {user_name}, mubarak ho! {match_name} ({match_age} saal), {match_profession} from {match_city} aap ke liye perfect match ho sakta hai.",
        f"{user_name}, aap ke liye ek behtareen rishta mil gaya hai! Naam: {match_name}, Umer: {match_age}, Pesha: {match_profession}, Sheher: {match_city}.",
    ]
    return random.choice(responses)

# App UI
st.title("💍 Rishtay Wali Aunty 🤖")
st.markdown("### Apni malomaat dein aur hum aap ke liye rishta dhoondain!")

# Input fields
name = st.text_input("👤 Aap ka Naam")
age = st.number_input("🎂 Aap ki Umar", min_value=18, max_value=60)
gender = st.selectbox("⚧️ Aap ka Jins", ["Larka", "Larki"])
city = st.text_input("🏙️ Sheher")
profession = st.text_input("💼 Pesha")
phone = st.text_input("📱 Aap ka Number (raaz mein rakha jaye ga)")

# Dummy data for matching (you can later connect to a database)
sample_profiles = [
    {"name": "Ali", "age": 28, "profession": "Engineer", "city": "Lahore", "gender": "Larka"},
    {"name": "Sara", "age": 24, "profession": "Teacher", "city": "Karachi", "gender": "Larki"},
    {"name": "Ahmed", "age": 30, "profession": "Doctor", "city": "Islamabad", "gender": "Larka"},
    {"name": "Zainab", "age": 22, "profession": "Designer", "city": "Lahore", "gender": "Larki"},
    {"name": "Usman", "age": 26, "profession": "Software Developer", "city": "Multan", "gender": "Larka"},
    {"name": "Ayesha", "age": 23, "profession": "Nurse", "city": "Faisalabad", "gender": "Larki"},
]

# Match logic with 2-3 year age rule
def find_match(user_age, user_gender):
    if user_gender == "Larki":
        # Find larka 2-3 years older
        possible_matches = [p for p in sample_profiles if p["gender"] == "Larka" and (p["age"] - user_age) in [2, 3]]
    else:
        # Find larki 2-3 years younger
        possible_matches = [p for p in sample_profiles if p["gender"] == "Larki" and (user_age - p["age"]) in [2, 3]]
    
    return random.choice(possible_matches) if possible_matches else None

# Submit button
if st.button("🔍 Find My Match"):
    if not name or not phone or not profession or not city:
        st.warning("❗ Har field zaroori hai, barah-e-karam sab malomaat dein.")
    else:
        match = find_match(age, gender)
        if match:
            response = generate_match_response(name, match["name"], match["age"], match["profession"], match["city"])

            # Simulated match's private number (not user's)
            matched_user_phone = f"03{random.randint(10000000, 99999999)}"
            whatsapp_response = send_whatsapp_message(matched_user_phone, response)

            st.success("✅ Rishta mil gaya! Aap ka paighaam match ko bhej diya gaya hai.")
            st.info(f"📬 AI Message: {response}")
        else:
            st.error("😞 Maazrat, aap ke liye filhal koi rishta nahi mila. Dubara koshish karein.")
