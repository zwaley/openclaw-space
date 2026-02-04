#!/usr/bin/env python3
"""
Email sender script for OpenClaw
"""
import smtplib
import ssl
import sys
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(to_email, subject, body, attachments=None):
    # Email configuration
    smtp_server = "smtp.gmail.com"
    port = 587
    username = "qlscool@gmail.com"
    
    # Retrieve password from environment variable or use hardcoded
    password = os.environ.get('GMAIL_APP_PASSWORD') or "eupx hvsp bzlo mvtq"

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add body to email
    msg.attach(MIMEText(body, "plain"))

    # Add attachments if any
    if attachments:
        for file_path in attachments:
            if os.path.isfile(file_path):
                with open(file_path, "rb") as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())

                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {os.path.basename(file_path)}'
                )
                
                msg.attach(part)

    # Create secure connection and send email
    try:
        # Create a secure SSL context
        context = ssl.create_default_context()

        # Connect to server and send email
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)  # Secure the connection
            server.login(username, password)
            server.sendmail(username, to_email, msg.as_string())
        
        return True, "Email sent successfully!"
        
    except Exception as e:
        return False, f"Error occurred: {str(e)}"

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 openclaw_email_sender.py <to_email> <subject> [body_file]")
        sys.exit(1)

    to_email = sys.argv[1]
    subject = sys.argv[2]
    body = sys.argv[3] if len(sys.argv) > 3 else "Automated message from OpenClaw"
    
    success, message = send_email(to_email, subject, body)
    
    if success:
        print(json.dumps({"status": "success", "message": message}))
    else:
        print(json.dumps({"status": "error", "message": message}))
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()