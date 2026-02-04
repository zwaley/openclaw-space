#!/usr/bin/env python3
"""
Test script to send an email using SMTP with Gmail
"""
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_test_email():
    # Email configuration
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    username = "qlscool@gmail.com"
    
    # IMPORTANT: You need to replace this with your actual Gmail App Password
    password = "eupx hvsp bzlo mvtq"  # Replace with your actual app password
    
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = username  # Sending to yourself as a test
    msg['Subject'] = "OpenClaw Test Email"

    # Add body to email
    body = """
    This is a test email sent from OpenClaw.
    
    If you received this email, the SMTP configuration is working correctly.
    You can now use OpenClaw to send emails.
    
    Best regards,
    OpenClaw Assistant
    """
    
    msg.attach(MIMEText(body, "plain"))

    # Create secure connection and send email
    try:
        # Create a secure SSL context
        context = ssl.create_default_context()

        # Connect to server and send email
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)  # Secure the connection
            server.login(username, password)
            server.sendmail(username, username, msg.as_string())
        
        print("Test email sent successfully!")
        return True
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    send_test_email()