import secmail

sec = secmail.SecMail()
msg = sec.read_message("< Email Here >", "< MessageId Here >")
print(msg.htmlBody)
