import smtplib
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465
# TODO Implement getpass
password = input('Type your password and press Enter: ')

subject = 'Attachment'
body = 'Email with attachment sent from Python'
sender_email = 'manukian.dev@gmail.com'
receiver_email = 'manukian.artur.94@gmail.com'

message = MIMEMultipart()
message['Subject'] = subject
message['From'] = sender_email
message['To'] = receiver_email
message['Bcc'] = receiver_email  # For mass emails (blind copy)

message.attach(MIMEText(body, 'plain'))

filename = 'document.pdf'

with open(filename, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header('Content-Disposition', f'attachment; filename={filename}')

message.attach(part)
text = message.as_string()

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
