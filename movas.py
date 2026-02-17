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
    h1, h2, h3, h4, p, label, .stMarkdown { color: white !important; }
    
    /* WhatsApp Button - Large & Green */
    div.stLinkButton > a {
        background-color: #25D366 !important;
        color: white !important;
        border-radius: 15px !important;
        padding: 15px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border: none !important;
        display: block !important;
        text-align: center !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGO ---
try:
    st.image("photo_2026-02-17_10-14-26.jpg", width=120)
except:
    st.title("💧 MOVAS WATER")

# --- CUSTOMER DETAILS ---
st.write("### 👤 Customer Information")
c_col1, c_col2 = st.columns(2)
with c_col1:
    cust_name = st.text_input("Full Name", placeholder="Enter your name")
with c_col2:
    cust_phone = st.text_input("Phone Number", placeholder="e.g. 08012345678")

st.divider()

# --- PRODUCTS ---
st.write("### 🛒 Select Your Order")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    try: st.image("photo_3_2026-02-17_10-12-40.jpg")
    except: st.write("📦 75ml Image")
    st.write("#### 75ml (Big)")
    st.write("₦1,300/pack")
    q75 = st.number_input("Qty", min_value=0, key="q75", step=1)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    try: st.image("photo_1_2026-02-17_10-12-40.jpg")
    except: st.write("📦 50ml Image")
    st.write("#### 50ml (Medium)")
    st.write("₦1,300/pack")
    q50 = st.number_input("Qty", min_value=0, key="q50", step=1)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    try: st.image("photo_2_2026-02-17_10-12-40.jpg")
    except: st.write("📦 30ml Image")
    st.write("#### 30ml (Small)")
    st.write("₦1,900/pack")
    q30 = st.number_input("Qty", min_value=0, key="q30", step=1)
    st.markdown('</div>', unsafe_allow_html=True)

# --- TOTAL & CHECKOUT ---
total = (q75 * 1300) + (q50 * 1300) + (q30 * 1900)

if total > 0:
    st.divider()
    st.markdown(f"## Total: ₦{total:,}")
    
    st.success(f"🏦 Transfer ₦{total:,} to: **OPAY (8026294248)**")
    
    delivery = st.radio("Delivery Type", ["Pick-Up", "Home Delivery"])
    addr = ""
    if delivery == "Home Delivery":
        addr = st.text_area("Enter Detailed Delivery Address", placeholder="Street name, House number, Area...")

    # --- THE WHATSAPP MESSAGE ---
    # This combines Name, Phone, and Address into the message
    order_details = f"""*MOVAS WATER ORDER* 💧
---
👤 *Customer:* {cust_name}
📞 *Phone:* {cust_phone}
---
📦 *Items:*
- 75ml (Big): {q75} packs
- 50ml (Medium): {q50} packs
- 30ml (Small): {q30} packs

💰 *Total Amount:* ₦{total:,}
🚚 *Delivery:* {delivery}
📍 *Address:* {addr if addr else 'Pick up at Shop'}
---
*Check my next message for the transfer receipt!* ✅"""

    wa_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(order_details)}"

    # --- FINAL STEP ---
    st.write("### Step 2: Finalize")
    if not cust_name or not cust_phone:
        st.warning("⚠️ Please enter your Name and Phone Number to continue.")
    else:
        if st.button("I HAVE PAID - SHOW THANK YOU PAGE"):
            st.balloons()
            st.markdown(f"""
            <div style="background-color:rgba(255,255,255,0.1); padding:20px; border-radius:15px; text-align:center;">
                <h3>Thank You, {cust_name}! 🫡</h3>
                <p>Your order for ₦{total:,} is ready. Click below to send the details to us on WhatsApp.</p>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("SEND ORDER TO WHATSAPP ✅", wa_url)

st.divider()
# Footer
f1, f2 = st.columns(2)
with f1:
    st.link_button("📞 CALL FOR ENQUIRY", f"tel:{CALL_NUMBER}")
with f2:
    st.link_button("💬 CHAT WITH SUPPORT", f"https://wa.me/{WHATSAPP_NUMBER}")
