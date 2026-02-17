# --- UPDATED CONFIGURATION ---
SENDER_EMAIL = "adamsoluwatosin65@gmail.com" 
# REPLACE THE LINE BELOW WITH YOUR NEW 16-CHARACTER APP PASSWORD
SENDER_PASS = "your 16 digit app password here" 

def send_movas_email(subject, receiver, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = f"Movas Water Shop <{SENDER_EMAIL}>"
    msg['To'] = receiver
    
    try:
        # Using port 465 for SSL (More secure and stable for Gmail)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASS)
            server.send_message(msg)
        return True
    except smtplib.SMTPAuthenticationError:
        st.error("❌ Authentication Failed: Did you use the 16-digit App Password?")
        return False
    except Exception as e:
        st.error(f"❌ Connection Error: {e}")
        return False
