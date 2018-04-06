'''
This program is exclusively used for sending mail
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(sender_email='askkeviv@gmail.com', sender_email_password='digitaled123', receiver_email=None, subject=None, message=None):
    try:
        # set up the server object
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(sender_email, sender_email_password)

        msg = MIMEMultipart()  # create a message

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # add in the message body
        msg.attach(MIMEText(message, 'html'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

        print("Mail sent....")
        # Terminate the SMTP session and close the connection
        s.quit()
    except:
        print('Email Not Sent')