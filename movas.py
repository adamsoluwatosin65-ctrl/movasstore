import streamlit as st
import random
import smtplib
from email.message import EmailMessage

# --- CONFIGURATION ---
SENDER_EMAIL = "your-gmail@gmail.com"
SENDER_PASS = "your-app-password" # Not your login password, a Google App Password

st.set_page_config(page_title="Movas Water Shop", page_icon="💧")

# --- SESSION STATE ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'verification_code' not in st.session_state:
    st.session_state.verification_code = None

# --- EMAIL LOGIC ---
def send_otp(receiver_email):
    otp = str(random.randint(100000, 999999))
    st.session_state.verification_code = otp
    msg = EmailMessage()
    msg.set_content(f"Your Movas Water verification code is: {otp}")
    msg['Subject'] = "Verification Code - Movas Water"
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(SENDER_EMAIL, SENDER_PASS)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        st.error(f"Error sending email: {e}")
        return False

# --- UI: REGISTRATION ---
if not st.session_state.authenticated:
    st.title("💧 Movas Table Water")
    st.subheader("Please Register to Start Shopping")
    
    email = st.text_input("Enter your Gmail address")
    if st.button("Send Verification Code"):
        if email:
            if send_otp(email):
                st.success("Code sent! Check your inbox.")
        else:
            st.warning("Please enter an email.")

    code_input = st.text_input("Enter the 6-digit code")
    if st.button("Verify & Enter"):
        if code_input == st.session_state.verification_code:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Invalid code.")

# --- UI: THE SHOP ---
else:
    st.title("🛒 Movas Online Store")
    
    # Product Data
    products = {
        "Bigger Bottle (75ml) - 15 per pack": 1300,
        "Medium Bottle (50ml) - 15 per pack": 1300,
        "Smallest Bottle (30ml) - 20 per pack": 1900
    }

    st.write("### Choose Your Packs")
    order_summary = {}
    total_price = 0

    for item, price in products.items():
        qty = st.number_input(f"{item} (₦{price:,} per pack)", min_value=0, step=1)
        if qty > 0:
            order_summary[item] = qty
            total_price += qty * price

    if total_price > 0:
        st.divider()
        st.write(f"### Total: ₦{total_price:,}")
        
        if st.button("Proceed to Checkout"):
            st.session_state.checkout = True

    # --- CHECKOUT SECTION ---
    if st.session_state.get('checkout'):
        st.header("💳 Payment & Delivery")
        st.info("Transfer to: **8026294248 | OPAY**")
        
        proof = st.file_uploader("Upload Proof of Payment (Screenshot)", type=['png', 'jpg', 'jpeg'])
        
        delivery_type = st.radio("Delivery Method", ["Pick Up", "Home Delivery"])
        
        if delivery_type == "Pick Up":
            st.write("📍 **Pick up at:** 44 Lamina Liasu Road, Ikotun Egbe")
        else:
            address = st.text_area("Enter Delivery Address")

        if st.button("Confirm Order"):
            if proof:
                st.success("Order Received! A confirmation email is being sent. 🚀")
                # Add logic here to send the final order email to you and the customer
            else:
                st.error("Please upload your proof of payment first.")