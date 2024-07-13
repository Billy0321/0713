import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
sender = "Billy10040321@gmail.com"
receiver = ["An10ma04@gmail.com","Billy_yu@asus.com"]

for i in receiver:
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = i
    header = Header("Test Send Email","utf-8")
    msg["subject"] = header.encode()

    body = "This is email send from Python"
    msg.attach(MIMEText(body))
    ssl_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context) as server:
        server.login(sender,"tzoz zvtt bglr bpzz")
        server.sendmail(sender,receiver,msg.as_string())
    print("success send email")