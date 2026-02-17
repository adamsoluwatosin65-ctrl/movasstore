import streamlit as st
import urllib.parse

# --- CONFIGURATION ---
WHATSAPP_NUMBER = "2348026294248" 

st.set_page_config(page_title="Movas Water Shop", page_icon="💧", layout="wide")

# --- DARK MODE ANIMATED BACKGROUND ---
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
    
    /* DARK CARDS */
    .product-card {
        background: rgba(0, 0, 0, 0.6); /* Black transparent background */
        backdrop-filter: blur(15px);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        color: white;
        margin-bottom: 20px;
    }
    
    /* Make text readable */
    h1, h2, h3, h4, p, label, .stMarkdown {
        color: #e0e0e0 !important;
        font-family: 'Inter', sans-serif;
    }

    /* Input Box Styling */
    input {
        background-color: #1a1a1a !important;
        color: white !important;
        border: 1px solid #333 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP START ---
st.title("💧 Movas Table Water")
st.write("### Quality Hydration | Direct WhatsApp Ordering")

# We removed the "Verification Code" section to prevent errors. 
# The shop is now open immediately.

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    try:
        st.image("photo_3_2026-02-17_10-12-40.jpg")
    except:
        st.write("📦 Image Missing")
    st.write("#### 75ml (Big)")
    st.write("₦1,300 per pack")
    q75 = st.number_input("Packs", min_value=0, key="q75", step=1)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    try:
        st.image("photo_1_2026-02-17_10-12-40.jpg")
    except:
        st.write("📦 Image Missing")
    st.write("#### 50ml (Medium)")
    st.write("₦1,300 per pack")
    q50 = st.number_input("Packs", min_value=0, key="q50", step=1)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    try:
        st.image("photo_2_2026-02-17_10-12-40.jpg")
    except:
        st.write("📦 Image Missing")
    st.write("#### 30ml (Small)")
    st.write("₦1,900 per pack")
    q30 = st.number_input("Packs", min_value=0, key="q30", step=1)
    st.markdown('</div>', unsafe_allow_html=True)

total = (q75 * 1300) + (q50 * 1300) + (q30 * 1900)

if total > 0:
    st.divider()
    st.write(f"## Total: ₦{total:,}")
    
    # Dark Payment Box
    st.markdown(f"""
    <div style="background-color:rgba(0,0,0,0.8); padding:20px; border-radius:15px; border: 1px solid #0074D9;">
        <h3 style="color:#7FDBFF !important;">💳 Payment Information</h3>
        <p>Transfer ₦{total:,} to:</p>
        <p><b>OPAY: 8026294248</b></p>
        <p>Name: Movas Water</p>
    </div>
    """, unsafe_allow_html=True)
    
    method = st.radio("Delivery Option", ["Self Pick-Up", "Home Delivery"])
    addr = ""
    if method == "Home Delivery":
        addr = st.text_input("Delivery Address")

    # Generate Message
    msg = f"Hello Movas! 💧\nI want to order:\n- 75ml: {q75} packs\n- 50ml: {q50} packs\n- 30ml: {q30} packs\n\nTotal: ₦{total:,}\nMethod: {method}\nAddress: {addr}\n\nI am sending my proof of payment now."
    wa_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(msg)}"

    if st.button("SEND ORDER VIA WHATSAPP ✅"):
        st.write(f'<meta http-equiv="refresh" content="0;url={wa_url}">', unsafe_allow_html=True)
        st.link_button("Click here if not redirected", wa_url)

st.divider()
st.write("📍 44 Lamina Liasu Road, Ikotun Egbe")
