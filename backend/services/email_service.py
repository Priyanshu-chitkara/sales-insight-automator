import smtplib
from email.mime.text import MIMEText

def send_email(to_email, summary):

    sender = "shardapriyanshu10@gmail.com"
    password = "lazf xjer faqf ojkl"

    msg = MIMEText(summary)
    msg["Subject"] = "Sales Insight Summary"
    msg["From"] = sender
    msg["To"] = to_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)