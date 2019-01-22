import smtplib
import ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465  # SSL
# TODO Implement getpass
password = input('Type your password and press Enter: ')

sender_email = 'manukian.dev@gmail.com'
receiver_email = 'manukian.artur.94@gmail.com'

message = MIMEMultipart('alternative')
message['Subject'] = 'multipart test'
message['From'] = sender_email
message['To'] = receiver_email

text = '''\
Hi,
How are you?
Read Python documentation:
https://docs.python.org/3'''

html = '''\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       Read <a href='https://docs.python.org/3'>Python documentation</a>.
  </body>
</html>
'''

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

message.attach(part1)
message.attach(part2)

# Secure SSL connection
# load the system’s trusted CA certificates,
# enable certificate validation and hostname checking,
# and try to choose reasonably secure protocol and cipher settings.
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login('manukian.dev@gmail.com', password)
    server.sendmail(sender_email, receiver_email, message.as_string())
