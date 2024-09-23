from email_assistant._vendor.simplegmail import Gmail

gmail_access_token = "ya29.a0AcM612zLanKBJ7OdAOGrNitjJtPuiVa_4_UPJtYELQChtBUhhEEfE53YrR9SVsFlcqH604xn7g8NTL6DjZftKzQpgPODbG_lc-Xobqoo_0bp71Wl1yE1GDQMmlCOum21X6A5_0xoYhiJWpNXYVe0j979iPq5OdyvHnsmcTu8aCgYKAZcSARESFQHGX2Miq3hPDBQGPBcxFBIeMtKgVw0175"

gmail = Gmail.from_token(access_token=gmail_access_token)

# # Send email
# params = {
#   "to": "gptfintech@gmail.com",
#   "sender": "steveflyer7@gmail.com",
#   "subject": "My first email from Autom",
#   "msg_html": "<h1>Woah, my first email!</h1><br />This is an HTML email.",
#   "msg_plain": "Hi\nThis is a plain text email.",
#   "signature": True  # use my account signature
# }
# message = gmail.send_message(**params)

# Read emails
messages = gmail.get_messages(query="invoice", limit=5)
for message in messages:
    print("To: " + message.recipient)
    print("From: " + message.sender)
    print("Subject: " + message.subject)
    print("Date: " + message.date)
    print("Preview: " + message.snippet)

    message_body = message.plain or message.html or "No message body"
    print("Message Body: " + message_body)  # or message.html
    print("-----------------")
