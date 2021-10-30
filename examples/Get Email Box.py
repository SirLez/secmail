import secmail

sec = secmail.SecMail()
messages = sec.get_messages("< Email Here >")

for msgId in messages.id:
    print(msgId)
