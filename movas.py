import streamlit as st
import random
import smtplib
from email.message import EmailMessage

# --- CONFIGURATION (UPDATE THESE!) ---
SENDER_EMAIL = "adamsoluwatosin65@gmail.com" 
SENDER_PASS = "xxxx xxxx xxxx xxxx" # USE YOUR 16-DIGIT APP PASSWORD HERE

st.set_page_config(page_title="Movas Water", page_icon="💧", layout="centered")

# --- CUSTOM CSS (BACKGROUND & STYLING) ---
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(180deg, #ffffff 0%, #e3f2fd 100%);
    }}
    .product-card {{
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 20px;
    }}
    h1, h2, h3 {{
        color: #01579b;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'otp' not in st.session_state:
    st.session_state.otp = None

# --- EMAIL LOGIC ---
def send_otp(receiver_email):
    otp = str(random.randint(100000, 999999))
    st.session_state.otp = otp
    msg = EmailMessage()
    msg.set_content(f"Your Movas Water verification code is: {otp}")
    msg['Subject'] = "💧 Movas Verification Code"
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(SENDER_EMAIL, SENDER_PASS)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        st.error(f"Error: {e}")
        return False

# --- AUTHENTICATION PAGE ---
if not st.session_state.authenticated:
    st.image("https://raw.githubusercontent.com/re-movas-logo-here.png", width=150) # Use your logo here
    st.title("Welcome to Movas Water 💧")
    st.write("Please verify your Gmail to access the shop.")
    
    email_user = st.text_input("Enter Gmail Address")
    if st.button("Get Verification Code"):
        if send_otp(email_user):
            st.success("Code sent! Check your inbox.")
            
    code = st.text_input("Enter 6-Digit Code")
    if st.button("Verify & Enter Shop"):
        if code == st.session_state.otp:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Wrong code, try again.")

# --- MAIN SHOP PAGE ---
else:
    st.title("💧 Movas Table Water Shop")
    st.write("### Freshness Delivered to Your Doorstep")

    # Product Columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image("photo_3_2026-02-17_10-12-40.jpg", caption="75ml (Big)")
        st.write("**Bigger Bottle (75ml)**")
        st.write("15 per pack - ₦1,300")
        qty_75 = st.number_input("Packs (75ml)", min_value=0, step=1, key="q75")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image("photo_1_2026-02-17_10-12-40.jpg", caption="50ml (Medium)")
        st.write("**Medium Bottle (50ml)**")
        st.write("15 per pack - ₦1,300")
        qty_50 = st.number_input("Packs (50ml)", min_value=0, step=1, key="q50")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image("photo_2_2026-02-17_10-12-40.jpg", caption="30ml (Small)")
        st.write("**Smallest Bottle (30ml)**")
        st.write("20 per pack - ₦1,900")
        qty_30 = st.number_input("Packs (30ml)", min_value=0, step=1, key="q30")
        st.markdown('</div>', unsafe_allow_html=True)

    total = (qty_75 * 1300) + (qty_50 * 1300) + (qty_30 * 1900)

    if total > 0:
        st.divider()
        st.subheader(f"Total Amount: ₦{total:,}")
        
        if st.checkbox("Proceed to Checkout 💳"):
            st.info("Transfer to: **8026294248 | OPAY**")
            proof = st.file_uploader("Upload Proof of Payment", type=['jpg', 'png'])
            
            method = st.radio("Delivery Option", ["Pick Up", "Delivery"])
            if method == "Pick Up":
                st.write("📍 **44 Lamina Liasu Road, Ikotun Egbe**")
            else:
                address = st.text_area("Delivery Address")
            
            if st.button("Complete Order 🚀"):
                if proof:
                    st.success("Order Placed! Check your Gmail for confirmation.")
                    # Add logic here to send final email to you/customer
                else:
                    st.warning("Please upload payment proof.")
