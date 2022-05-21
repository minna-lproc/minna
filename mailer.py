import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from flask_mail import Mail, Message
from config import MAIL_SERVER, MAIL_USERNAME, MAIL_PASSWORD



sender_email = "MAIL_USERNAME"
receiver_email = "alemaniacamilleite111@gmail.com"
password = "MAIL_PASSWORD"

# msg = Message (
#       subject  = f"Mail from {name} ",
#       body = f" Name: {name}\nE-Mail: {email}\n Organization:{organization}\n\nMessage: {message}",
#       sender = email,
#       recipients = ['alemaniacamilleite111@gmail.com']
# )

#   msg = Message(
#     subject  = f"Mail from {name} ",
#     body = f" Name: {name}\nE-Mail: {email}\n Organization:{organization}\n\nMessage: {message}",
#     sender = email,
#         recipients = ['alemaniacamilleite111@gmail.com']
#         )


msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = COMMASPACE.join(receiver_email)
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = subject
msg['file'] = file

msg.attach(MIMEText(message))

if not server:
    server = MAIL_SERVER

for path in files:
    part = MIMEBase('application', "octet-stream")
with open(path, 'rb') as file:
    part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename={}'.format(Path(path).name))
msg.attach(part)

smtp = smtplib.SMTP(server, port)
if use_tls:
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()
