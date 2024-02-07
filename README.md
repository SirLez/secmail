# secmail - Python Client Library for 1secmail API

This is a Python client library for generating email addresses and accessing mailbox messages using the 1secmail API.

## Installation

Install via pip:

```bash
pip install secmail
```

# Usage
```py
# Import the secmail module
from secmail import SecMail

# Create a SecMail instance
sec = SecMail()

# Generate a single email address
email = sec.generate_email()
print("Generated email address:", email)

# Generate multiple email addresses by setting the count parameter
# Returns a list of emails
emails = sec.generate_email(count=3)
print("Generated email addresses:", emails)

# Get messages for a specific email address
messages = sec.get_messages(email)
print("Messages:", messages)

# Assuming there is at least one message in the inbox
if messages:
    # Read the first message in the inbox
    message_id = messages[0].id
    message_info = sec.read_message(email, message_id)
    print("Message ID:", message_info.info.id)
    print("Message Sender:", message_info.info.sender)
    print("Message Title:", message_info.info.title)
    print("Message Date:", message_info.info.date)
    print("Message Content:", message_info.content)
    print("Message HTML Body:", message_info.htmlBody)
    print("Message Attachments:", message_info.attachments)
else:
    print("No messages found in the inbox.")
```
