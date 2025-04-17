import streamlit as st
import re
import random

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ At least 8 characters.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include uppercase & lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one digit.")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (!@#$%^&*).")

    return score, feedback

def generate_strong_password(length=12):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Strength Checker")
password = st.text_input("Enter your password", type="password")

if st.button("Check Strength"):
    if not password:
        st.warning("Please enter a password.")
    else:
        score, tips = check_password_strength(password)

        st.markdown(f"### 🔍 Score: `{score}/4`")

        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.warning("⚠️ Moderate Password - You can improve it.")
            for tip in tips:
                st.write("•", tip)
        else:
            st.error("❌ Weak Password - Needs improvement!")
            for tip in tips:
                st.write("•", tip)

        if score < 4:
            st.markdown("### 💡 Suggested Strong Password:")
            st.code(generate_strong_password(), language="text")

# Footer
st.markdown(
    """
    <hr style="margin-top: 50px;"/>
    <div style="text-align: center; font-size: 14px; color: gray;">
        &copy; 2025 <strong>Owais Khan</strong>. All Rights Reserved.
    </div>
    """,
    unsafe_allow_html=True
)
