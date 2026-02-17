import streamlit as st
import random
import smtplib
from email.message import EmailMessage

# --- CONFIGURATION (IMPORTANT: Use your 16-digit App Password) ---
SENDER_EMAIL = "adamsoluwatosin65@gmail.com" 
SENDER_PASS = "xxxx xxxx xxxx xxxx" 

st.set_page_config(page_title="Movas Water", page_icon="💧", layout="wide")

# --- ANIMATED BACKGROUND & STYLING ---
st.markdown(f"""
    <style>
    /* Animated Gradient Background */
    .stApp {{
        background: linear-gradient(-45deg, #ffffff, #e3f2fd, #bbdefb, #e3f2fd);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }}

    @keyframes gradient {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    /* Card Styling */
    .product-card {{
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        text-align: center;
        transition: transform 0.3s;
    }}
    .product-card:hover {{
        transform: translateY(-10px);
    }}
    h1, h2, h3 {{
        color: #01579b;
        font-family: 'Helvetica', sans-serif;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'otp' not in st.session_state:
    st.session_state.otp = None

# --- EMAIL LOGIC ---
def send_email(subject, receiver, body):
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
        return False

# --- UI: AUTHENTICATION ---
if not st.session_state.authenticated:
    st.title("💧 Movas Table Water")
    st.write("Verify your Gmail to start shopping.")
    
    email_user = st.text_input("Enter Gmail Address")
    if st.button("Get Verification Code"):
        otp = str(random.randint(100000, 999999))
        st.session_state.otp = otp
        if send_email("💧 Movas Verification Code", email_user, f"Your code is: {otp}"):
            st.success("Code sent!")
            
    code = st.text_input("Enter 6-Digit Code")
    if st.button("Verify & Enter Shop"):
        if code == st.session_state.otp:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Invalid code.")

# --- UI: MAIN SHOP ---
else:
    st.image("photo_2026-02-17_10-14-26.jpg", width=120) # Your Logo
    st.title("🛒 Movas Order Center")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image("photo_3_2026-02-17_10-12-40.jpg", caption="75ml (Big)")
        st.write("### ₦1,300")
        qty_75 = st.number_input("Packs (75ml)", min_value=0, key="q75")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image("photo_1_2026-02-17_10-12-40.jpg", caption="50ml (Medium)")
        st.write("### ₦1,300")
        qty_50 = st.number_input("Packs (50ml)", min_value=0, key="q50")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image("photo_2_2026-02-17_10-12-40.jpg", caption="30ml (Small)")
        st.write("### ₦1,900")
        qty_30 = st.number_input("Packs (30ml)", min_value=0, key="q30")
        st.markdown('</div>', unsafe_allow_html=True)

    total = (qty_75 * 1300) + (qty_50 * 1300) + (qty_30 * 1900)

    if total > 0:
        st.markdown(f"## Total: ₦{total:,}")
        
        with st.expander("Finalize Order"):
            st.info("Transfer to: **8026294248 | OPAY (Movas)**")
            proof = st.file_uploader("Upload Receipt")
            method = st.radio("Delivery Type", ["Pick Up", "Home Delivery"])
            addr = st.text_input("Address (if delivery)") if method == "Home Delivery" else "44 Lamina Liasu Road"

            if st.button("Complete My Order"):
                if proof:
                    order_details = f"Order Total: N{total}\n75ml: {qty_75}\n50ml: {qty_50}\n30ml: {qty_30}\nMethod: {method}\nAddress: {addr}"
                    
                    # Send to you
                    send_email("NEW ORDER RECEIVED!", SENDER_EMAIL, order_details)
                    # Send to customer
                    send_email("Movas Order Confirmation", email_user, f"Thanks for your order!\n\n{order_details}")
                    
                    st.balloons()
                    st.success("Order Successful! Receipt sent to your email.")
                else:
                    st.error("Please upload payment proof.")
