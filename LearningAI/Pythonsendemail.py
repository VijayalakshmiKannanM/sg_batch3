import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail credentials
sender_email = "your_email@gmail.com"
app_password = "your_16_character_app_password"
receiver_email = "mskvijidba@gmail.com"

# Create the email
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Test Email from Python"

body = """
Hello!

This is a test email sent from a Python script using Gmail SMTP.

Best regards,
Python Automation Script
"""
msg.attach(MIMEText(body, "plain"))

# Connect to Gmail SMTP and send
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, app_password)
        server.send_message(msg)
        print("✅ Email sent successfully!")
except Exception as e:
    print("❌ Error:", e)
