import smtplib
s= smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("sumeetssk.2388@gmail.com","sumeet2388")
msg="Hii how r u..?"
s.sendmail("sumeetssk.2388@gmail.com","sumeetssk.2388@gmail.com",msg)
s.quit()

