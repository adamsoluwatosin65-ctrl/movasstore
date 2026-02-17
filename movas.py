import streamlit as st
import urllib.parse

# --- CONFIG ---
WHATSAPP_NUMBER = "2348026294248" 
CALL_NUMBER = "08022233604"

st.set_page_config(page_title="Movas Water", page_icon="💧", layout="wide")

# --- DARK DESIGN ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(-45deg, #000814, #001d3d, #003566, #000814);
        background-size: 400% 400%;
        animation: gradientBG 10s ease infinite;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .product-card {
        background: rgba(0, 0, 0, 0.8); /* Solid Black Transparency */
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #0074D9;
        text-align: center;
        margin-bottom: 20px;
    }
    h1, h2, h3, h4, p, label { color: white !important; }
    
    /* WhatsApp Button Green */
    .wa-button a {
        background-color: #25D366 !important;
        color: white !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        font-size: 18px !important;
        text-align: center !important;
        display: block !important;
        padding: 10px;
        text-decoration: none;
    }
    /* Call Button Blue */
    .call-button a {
        background-color: #0074D9 !important;
        color: white !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        font-size: 18px !important;
        text-align: center !important;
        display: block !important;
        padding: 10px;
        text-decoration: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💧 Movas Table Water")
st.write("Freshness you can trust. Order below.")

# --- PRODUCT DISPLAY ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.write("#### 75ml (Big)")
    st.write("₦1,300 per pack")
    q75 = st.number_input("Packs", min_value=0, key="q75", step=1)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.write("#### 50ml (Medium)")
    st.write("₦1,300 per pack")
    q50 = st.number_input("Packs", min_value=0, key="q50", step=1)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.write("#### 30ml (Small)")
    st.write("₦1,900 per pack")
    q30 = st.number_input("Packs", min_value=0, key="q30", step=1)
    st.markdown('</div>', unsafe_allow_html=True)

total = (q75 * 1300) + (q50 * 1300) + (q30 * 1900)

if total > 0:
    st.divider()
    st.markdown(f"## Total Amount: ₦{total:,}")
    
    # Dark Payment Box
    st.markdown(f"""
    <div style="background-color:rgba(0, 0, 0, 0.6); padding:20px; border-radius:10px; border-left: 5px solid #0074D9;">
        <h4 style="margin-top:0;">💳 Payment Details</h4>
        <p>Transfer to: <b>OPAY - 8026294248</b></p>
        <p>Account Name: Movas Water</p>
    </div>
    """, unsafe_allow_html=True)
    
    method = st.radio("How do you want it?", ["Pick-Up", "Delivery"])
    addr = st.text_input("Enter Address (if delivery)") if method == "Delivery" else ""

    # WhatsApp Link
    msg = f"Order Request 💧\n---\nItems:\n- 75ml: {q75}\n- 50ml: {q50}\n- 30ml: {q30}\n\nTotal: ₦{total:,}\nMethod: {method}\nAddress: {addr}"
    wa_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(msg)}"

    # Buttons
    st.write("### Step 2: Complete Order")
    st.markdown(f'<div class="wa-button"><a href="{wa_url}" target="_blank">SEND ORDER TO WHATSAPP ✅</a></div>', unsafe_allow_html=True)

st.divider()

# --- FOOTER SUPPORT ---
st.write("### Need Assistance?")
fcol1, fcol2 = st.columns(2)

with fcol1:
    st.markdown(f'<div class="call-button"><a href="tel:{CALL_NUMBER}">📞 CALL US NOW</a></div>', unsafe_allow_html=True)

with fcol2:
    support_wa = f"https://wa.me/{WHATSAPP_NUMBER}?text=I%20need%20help%20with%20an%20order"
    st.markdown(f'<div class="wa-button"><a href="{support_wa}" target="_blank">💬 CHAT SUPPORT</a></div>', unsafe_allow_html=True)

st.caption("📍 Shop: 44 Lamina Liasu Road, Ikotun Egbe")
