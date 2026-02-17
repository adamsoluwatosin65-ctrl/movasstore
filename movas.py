import streamlit as st
import random
import smtplib
from email.message import EmailMessage

# --- CONFIGURATION ---
SENDER_EMAIL = "adamsoluwatosin65@gmail.com" 
# IMPORTANT: Put your 16-character Google App Password here!
SENDER_PASS = "xxxx xxxx xxxx xxxx" 

st.set_page_config(page_title="Movas Water", page_icon="💧", layout="wide")

# --- ANIMATED NAVY & SKY BLUE BACKGROUND ---
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(-45deg, #001f3f, #0074D9, #7FDBFF, #001f3f);
        background-size: 400% 400%;
        animation: gradientBG 10s ease infinite;
        color: white;
    }}

    @keyframes gradientBG {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    /* Card Styling */
    .product-card {{
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(15px);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
        transition: 0.3s;
    }}
    .product-card:hover {{
        transform: scale(1.03);
        background: rgba(255, 255, 255, 0.25);
    }}
    
    /* Input colors for visibility */
    .stNumberInput input, .stTextInput input {{
        color: #001f3f !important;
    }}
    h1, h2, h3, p {{
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- EMAIL ENGINE ---
def send_movas_email(subject, receiver, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(SENDER_EMAIL, SENDER_PASS)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        st.error(f"Email Error: {e}")
        return False

# --- APP LOGIC ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("💧 Movas Table Water")
    st.write("### Register to Unlock Freshness")
    
    target_email = st.text_input("Enter your Gmail")
    if st.button("Send Code"):
        otp = str(random.randint(100000, 999999))
        st.session_state.otp = otp
        if send_movas_email("Verification Code", target_email, f"Your code: {otp}"):
            st.success("Code sent to your inbox!")

    code_in = st.text_input("6-Digit Code")
    if st.button("Access Shop"):
        if code_in == st.session_state.get('otp'):
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Invalid Code")

else:
    # --- LOGO & SHOP ---
    st.image("photo_2026-02-17_10-14-26.jpg", width=150)
    st.title("🛒 Order Your Water")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image("photo_3_2026-02-17_10-12-40.jpg")
        st.write("#### 75ml (Big)")
        st.write("₦1,300 per pack")
        q75 = st.number_input("Qty", min_value=0, key="q75")
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image("photo_1_2026-02-17_10-12-40.jpg")
        st.write("#### 50ml (Medium)")
        st.write("₦1,300 per pack")
        q50 = st.number_input("Qty", min_value=0, key="q50")
        st.markdown('</div>', unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image("photo_2_2026-02-17_10-12-40.jpg")
        st.write("#### 30ml (Small)")
        st.write("₦1,900 per pack")
        q30 = st.number_input("Qty", min_value=0, key="q30")
        st.markdown('</div>', unsafe_allow_html=True)

    total_amt = (q75 * 1300) + (q50 * 1300) + (q30 * 1900)

    if total_amt > 0:
        st.write(f"## Total: ₦{total_amt:,}")
        if st.checkbox("Ready to Checkout?"):
            st.warning("Pay to: 8026294248 | OPAY")
            proof_file = st.file_uploader("Upload Receipt")
            mthd = st.radio("Delivery", ["Pick Up", "Delivery"])
            
            if st.button("Finalize Order"):
                if proof_file:
                    st.balloons()
                    st.success("Order Placed! Check your email.")
                else:
                    st.error("Please upload receipt first.")
