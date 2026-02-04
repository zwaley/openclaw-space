#!/usr/bin/env python3
"""
Email sending utility for OpenClaw
"""
import smtplib
import ssl
import sys
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(to_email, subject, body, attachments=None):
    # Email configuration
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    username = "qlscool@gmail.com"
    
    # Get password from environment variable or use the provided one
    password = os.getenv('GMAIL_APP_PASSWORD', 'eupx hvsp bzlo mvtq')  # Replace with your actual app password
    
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add body to email
    msg.attach(MIMEText(body, "plain"))

    # Add attachments if provided
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
        
        print(f"Email sent successfully to {to_email}!")
        return True
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return False

def main():
    if len(sys.argv) < 4:
        print("Usage: python send_email.py <to_email> <subject> <body> [attachment_paths...]")
        sys.exit(1)
    
    to_email = sys.argv[1]
    subject = sys.argv[2]
    body = sys.argv[3]
    attachments = sys.argv[4:] if len(sys.argv) > 4 else None
    
    success = send_email(to_email, subject, body, attachments)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()