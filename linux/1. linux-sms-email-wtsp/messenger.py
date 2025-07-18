import os
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def send_email(receiver, message):
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")

    msg = MIMEText(message)
    msg["Subject"] = "Message from Linux Terminal"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Email failed: {e}")

def send_whatsapp(to_number, message):
    client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    try:
        msg = client.messages.create(
            from_="whatsapp:+14155238886",  # Twilio Sandbox
            body=message,
            to=f"whatsapp:{to_number}"
        )
        print(f"✅ WhatsApp sent: SID {msg.sid}")
    except Exception as e:
        print(f"❌ WhatsApp failed: {e}")

def send_sms(to_number, message):
    client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    from_number = os.getenv("TWILIO_SMS_FROM")
    try:
        msg = client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        print(f"✅ SMS sent: SID {msg.sid}")
    except Exception as e:
        print(f"❌ SMS failed: {e}")

def main():
    print("\n📬 Linux Terminal Messenger")
    print("1. Send Email")
    print("2. Send WhatsApp Message")
    print("3. Send SMS")
    choice = input("👉 Select an option (1/2/3): ").strip()

    if choice == "1":
        receiver = input("📧 Enter receiver's email address: ").strip()
        message = input("✉️  Enter your message: ").strip()
        send_email(receiver, message)

    elif choice == "2":
        number = input("📱 Enter WhatsApp number with country code (e.g. +91xxxxxxxxxx): ").strip()
        message = input("💬 Enter your message: ").strip()
        send_whatsapp(number, message)

    elif choice == "3":
        number = input("📲 Enter SMS number with country code (e.g. +91xxxxxxxxxx): ").strip()
        message = input("📝 Enter your message: ").strip()
        send_sms(number, message)

    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
