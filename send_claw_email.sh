#!/bin/bash

# Simple wrapper script to send emails from OpenClaw
# Usage: ./send_claw_email.sh "recipient@email.com" "Subject" "Message Body"

if [ $# -lt 3 ]; then
    echo "Usage: $0 <recipient> <subject> <message> [attachment_path]"
    exit 1
fi

RECIPIENT="$1"
SUBJECT="$2"
MESSAGE="$3"
ATTACHMENT="$4"

if [ -n "$ATTACHMENT" ] && [ -f "$ATTACHMENT" ]; then
    python3 /home/codespace/.openclaw/workspace/send_email.py "$RECIPIENT" "$SUBJECT" "$MESSAGE" "$ATTACHMENT"
else
    python3 /home/codespace/.openclaw/workspace/send_email.py "$RECIPIENT" "$SUBJECT" "$MESSAGE"
fi