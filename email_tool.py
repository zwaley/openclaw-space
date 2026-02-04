#!/usr/bin/env python3
"""
Email tool for OpenClaw
"""
import smtplib
import ssl
import sys
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(to_email, subject, body):
    # Email configuration
    smtp_server = "smtp.gmail.com"
    port = 587
    username = "qlscool@gmail.com"
    password = "eupx hvsp bzlo mvtq"  # Gmail app password

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add body to email
    msg.attach(MIMEText(body, "plain"))

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

if __name__ == "__main__":
    if len(sys.argv) < 3:
        result = {"status": "error", "message": "Usage: python3 email_tool.py <to_email> <subject> [body]"}
    else:
        to_email = sys.argv[1]
        subject = sys.argv[2]
        body = sys.argv[3] if len(sys.argv) > 3 else "Automated message from OpenClaw"
        
        success, message = send_email(to_email, subject, body)
        
        result = {
            "status": "success" if success else "error",
            "message": message
        }
    
    print(json.dumps(result))