import smtplib
import time

# insert your gmail here
mail = "email@gmail.com"
# insert your password here; password must be a password app
passwd = "[insert your password]"
# insert the frequency time (in seconds) of sending emails
timeToSend = 600


def send_mail():
    email = smtplib.SMTP("smtp.gmail.com", 587)
    email.starttls()
    email.login(mail, passwd)
    email.sendmail(mail, mail, message)
    email.quit()


while True:
    message = open("log.txt", "r").read()
    send_mail()
    time.sleep(timeToSend)
