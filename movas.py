import streamlit as st
import urllib.parse

# --- CONFIGURATION ---
WHATSAPP_NUMBER = "2348026294248" 

st.set_page_config(page_title="Movas Water Shop", page_icon="💧", layout="wide")

# --- ANIMATED NAVY/SKY BLUE BACKGROUND ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(-45deg, #001f3f, #0074D9, #7FDBFF, #001f3f);
        background-size: 400% 400%;
        animation: gradientBG 8s ease infinite;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .product-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
        color: white;
        transition: 0.3s;
    }
    .product-card:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-5px);
    }
    h1, h2, h3, p, label { color: white !important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.image("photo_2026-02-17_10-14-26.jpg", width=150)
st.title("💧 Movas Table Water")
st.write("### Quality Hydration, Delivered Fast.")
st.divider()

# --- PRODUCT SECTION ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image("photo_3_2026-02-17_10-12-40.jpg", caption="75ml Big Bottle")
    st.write("#### ₦1,300 / Pack")
    q75 = st.number_input("How many packs?", min_value=0, key="q75", step=1)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image("photo_1_2026-02-17_10-12-40.jpg", caption="50ml Medium Bottle")
    st.write("#### ₦1,300 / Pack")
    q50 = st.number_input("How many packs?", min_value=0, key="q50", step=1)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image("photo_2_2026-02-17_10-12-40.jpg", caption="30ml Small Bottle")
    st.write("#### ₦1,900 / Pack")
    q30 = st.number_input("How many packs?", min_value=0, key="q30", step=1)
    st.markdown('</div>', unsafe_allow_html=True)

# --- CHECKOUT CALCULATIONS ---
total = (q75 * 1300) + (q50 * 1300) + (q30 * 1900)

if total > 0:
    st.markdown(f"## 🛒 Order Total: ₦{total:,}")
    
    with st.container():
        st.markdown("""
        <div style="background-color:rgba(255,255,255,0.9); padding:20px; border-radius:15px; color:#001f3f;">
            <h3 style="color:#001f3f !important; margin-top:0;">💳 Payment Details</h3>
            <p style="color:#001f3f !important; font-size:18px;">Bank: <b>OPAY</b></p>
            <p style="color:#001f3f !important; font-size:18px;">Account Number: <b>8026294248</b></p>
            <p style="color:#001f3f !important; font-size:18px;">Account Name: <b>Movas Water</b></p>
        </div>
        """, unsafe_allow_html=True)
        
    st.write("")
    delivery = st.radio("Delivery Method", ["Self Pick-Up", "Home Delivery"])
    
    address = ""
    if delivery == "Home Delivery":
        address = st.text_input("Enter Delivery Address", placeholder="e.g. 123 Street Name, Ikotun")

    # Order Message Logic
    order_msg = f"*New Order from Website* 💧\n---\n📦 *Items:*\n- 75ml: {q75} packs\n- 50ml: {q50} packs\n- 30ml: {q30} packs\n\n💰 *Total:* ₦{total:,}\n🚚 *Method:* {delivery}\n📍 *Address:* {address if address else 'Pick up at Shop'}"
    wa_order_link = f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(order_msg)}"

    if st.button("Complete Order & Send Receipt ✅"):
        st.write(f'<meta http-equiv="refresh" content="0;url={wa_order_link}">', unsafe_allow_html=True)

# --- FOOTER / SUPPORT ---
st.divider()
support_msg = "Hello Movas Support, I have a question about my water order."
wa_support_link = f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(support_msg)}"

st.write("### Need Help?")
if st.button("Chat with Support on WhatsApp 💬"):
    st.write(f'<meta http-equiv="refresh" content="0;url={wa_support_link}">', unsafe_allow_html=True)

st.caption("📍 Visit us: 44 Lamina Liasu Road, Ikotun Egbe")
