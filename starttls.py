import smtplib
import ssl

smtp_server = 'smtp.gmail.com'
port = 587
sender_email = 'manukian.dev@gmail.com'
# TODO Implement getpass
password = input('Type your password and press Enter: ')

# Secure SSL connection
context = ssl.create_default_context()

# Try to login to server and send email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)  # Secure connection
    server.ehlo()
    server.login(sender_email, password)
    # Sending email
except Exception as e:
    print(e)
finally:
    server.quit()
