import secmail

sec = secmail.SecMail()
email = sec.generate_email(count=1)
print(email)
