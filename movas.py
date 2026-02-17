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
        background: rgba(0, 0, 0, 0.85);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #0074D9;
        text-align: center;
        margin-bottom: 15px;
    }
    h1, h2, h3, h4, p, label { color: white !important; }
    
    /* WhatsApp Button - Large & Green */
    div.stLinkButton > a {
        background-color: #25D366 !important;
        color: white !important;
        border-radius: 15px !important;
        padding: 20px !important;
        font-size: 22px !important;
        font-weight: bold !important;
        border: none !important;
        display: block !important;
        text-align: center !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💧 Movas Table Water")

# --- PRODUCTS ---
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="product-card"><h4>75ml (Big)</h4><p>₦1,300/pack</p></div>', unsafe_allow_html=True)
    q75 = st.number_input("Packs", min_value=0, key="q75")
with col2:
    st.markdown('<div class="product-card"><h4>50ml (Medium)</h4><p>₦1,300/pack</p></div>', unsafe_allow_html=True)
    q50 = st.number_input("Packs", min_value=0, key="q50")
with col3:
    st.markdown('<div class="product-card"><h4>30ml (Small)</h4><p>₦1,900/pack</p></div>', unsafe_allow_html=True)
    q30 = st.number_input("Packs", min_value=0, key="q30")

total = (q75 * 1300) + (q50 * 1300) + (q30 * 1900)

if total > 0:
    st.divider()
    st.markdown(f"## Total: ₦{total:,}")
    
    # Payment Box
    st.success(f"🏦 Transfer ₦{total:,} to: **OPAY (8026294248)**")
    
    delivery = st.radio("Delivery Type", ["Pick-Up", "Home Delivery"])
    addr = st.text_input("Enter Address") if delivery == "Home Delivery" else ""

    # Message Setup
    msg = f"New Water Order 💧\n---\nItems:\n- 75ml: {q75}\n- 50ml: {q50}\n- 30ml: {q30}\n\nTotal: ₦{total:,}\nMethod: {delivery}\nAddress: {addr}"
    wa_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(msg)}"

    # --- THE FINAL BUTTON ---
    st.write("### Step 2: Confirm & Send")
    if st.button("I HAVE PAID - SHOW ORDER BUTTON"):
        st.balloons()
        st.markdown(f"""
        <div style="background-color:rgba(255,255,255,0.1); padding:20px; border-radius:15px; text-align:center;">
            <h3>Thank You for choosing Movas! 🫡</h3>
            <p>Click the green button below to finalize your order on WhatsApp.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("CLICK HERE TO SEND TO WHATSAPP ✅", wa_url)

st.divider()
# Footer Buttons
f1, f2 = st.columns(2)
with f1:
    st.link_button("📞 CALL FOR ENQUIRY", f"tel:{CALL_NUMBER}")
with f2:
    st.link_button("💬 CHAT WITH SUPPORT", f"https://wa.me/{WHATSAPP_NUMBER}")
