from fileinput import filename
import smtplib, ssl
from email.message import EmailMessage
from tkinter import filedialog

def send_email():
    reciever_email = input("Send e-mail to: ")
    theme = input("Theme: ")
    content = input("Content: ")
    content = """<!DOCTYPE html>
<head>
</head>
<body>
<h1>Sending an HTML email from Python</h1>
<p>Hello there,</p>
<a href="https://tahvel.edu.ee/">Here's a link to tahvel!</a>
</body>
</html>"""
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    your_email = input("Your Email: ")
    key = input("Your email key: ")

    msg = EmailMessage()
    msg['Subject'] = theme
    msg['From'] = your_email
    msg['To'] = reciever_email
    msg.set_content(content)

    file=filedialog.askopenfilename(title="Pick file", filetypes=[("All files", "*.*")])
    
    with open('message.html', 'r') as file_:
        file_content = file_.read()
        msg.set_content(file_content, subtype='html')

    with open(file,'rb') as f:
        file_content=f.read()
        file_name=file.split("/")[-1]
        msg.add_attachment(file_content,maintype="application", subtype="octet-stream", filename=file_name)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(your_email, key)
            server.send_message(msg)
        print("Email sent!")
    except Exception as E:
        print(f"Error: {E}")

send_email()
