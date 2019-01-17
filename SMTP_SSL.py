import smtplib
import ssl

port = 465  # SSL
password = input('Type your password and press Enter: ')

# Secure SSL connection
# load the system’s trusted CA certificates,
# enable certificate validation and hostname checking,
# and try to choose reasonably secure protocol and cipher settings.
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login('manukian.dev@gmail.com', password)
    # Sending email