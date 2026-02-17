import streamlit as st
import random
import smtplib
from email.message import EmailMessage

# --- 1. SETTINGS & AUTH (FIX THIS LINE!) ---
SENDER_EMAIL = "adamsoluwatosin65@gmail.com" 
SENDER_PASS = "xxxx xxxx xxxx xxxx" # Replace with your 16-digit App Password

st.set_page_config(page_title="Movas Water Shop", page_icon="💧", layout="wide")

# --- 2. THE ANIMATED NAVY/SKY BLUE BACKGROUND ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(-45deg, #001f3f, #0074D9, #7FDBFF, #001f3f);
        background-size: 400% 400%;
        animation: gradientBG 10s ease infinite;
        color: white;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .product-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
        margin-bottom: 15px;
    }
    h1, h2, h3, p, span, label {
        color: white !important;
    }
    /* Fixing input visibility */
    input {
        color: black !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE EMAIL ENGINE ---
def send_movas_email(subject, receiver, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASS)
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Login failed. Check your App Password! Error: {e}")
        return False

# --- 4. APP LOGIC ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# PAGE A: LOGIN
if not st.session_state.authenticated:
    st.title("💧 Movas Table Water")
    st.subheader("Register to Unlock Freshness")
    
    user_mail = st.text_input("Enter your Gmail")
    if st.button("Send Code"):
        otp = str(random.randint(100000, 999999))
        st.session_state.otp = otp
        if send_movas_email("💧 Movas Verification Code", user_mail, f"Your code: {otp}"):
            st.success("Verification code sent!")

    code_in = st.text_input("Enter 6-Digit Code")
    if st.button("Access Shop"):
        if code_in == st.session_state.get('otp'):
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Invalid Code")

# PAGE B: THE SHOP
else:
    st.title("🛒 Movas Order Center")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.write("### 75ml (Big)")
        st.write("₦1,300 per pack")
        q75 = st.number_input("Packs", min_value=0, key="q75")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.write("### 50ml (Medium)")
        st.write("₦1,300 per pack")
        q50 = st.number_input("Packs", min_value=0, key="q50")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.write("### 30ml (Small)")
        st.write("₦1,900 per pack")
        q30 = st.number_input("Packs", min_value=0, key="q30")
        st.markdown('</div>', unsafe_allow_html=True)

    total = (q75 * 1300) + (q50 * 1300) + (q30 * 1900)
    
    if total > 0:
        st.markdown(f"## Total: ₦{total:,}")
        if st.checkbox("Proceed to Payment"):
            st.info("Transfer to: **8026294248 | OPAY (Movas)**")
            st.file_uploader("Upload Receipt")
            if st.button("Confirm Order"):
                st.balloons()
                st.success("Order Placed!")
