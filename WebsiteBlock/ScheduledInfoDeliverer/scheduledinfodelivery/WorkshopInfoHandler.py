"""
WorkshopInfoHandler

This file handles the response received from the API/Graphql

"""

import os, smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# this is how we could access other directory
import sys
sys.path.append(os.path.join('..', 'ScheduledInfoDeliverer'))
from ScheduledInfoDeliverer import settings

emailAddress = ''
emailPassword = ''
contactFileLocation = ''
messageFileLocation = ''
workshopFileLocation = ''

def setup_mail_user_info():
    global emailAddress, emailPassword
    emailAddress = 'askkeviv@gmail.com'
    emailPassword = 'digitaled123'


def setup_file_location():
    global contactFileLocation, messageFileLocation, workshopFileLocation
    TEMPLATE_CONTACTS_DIR = os.path.join(list(settings.TEMPLATE_DIRS)[0], 'scheduledinfodelivery', 'contacts.txt')
    TEMPLATE_MESSAGE_DIR = os.path.join(list(settings.TEMPLATE_DIRS)[0], 'scheduledinfodelivery', 'message.txt')
    TEMPLATE_WORKSHOP_INFO_DIR = os.path.join(list(settings.TEMPLATE_DIRS)[0], 'scheduledinfodelivery', 'workshopinfo.txt')

    contactFileLocation = TEMPLATE_CONTACTS_DIR
    messageFileLocation = TEMPLATE_MESSAGE_DIR
    workshopFileLocation = TEMPLATE_WORKSHOP_INFO_DIR


# Function to read the contacts from a given contact file and return a
# list of names and email addresses
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split('#$')[1])
            emails.append(a_contact.split('#$')[2])
    return names, emails


# Function to read the workshop information from a given workshopinfo file and return a
# list of category, title and duration info
def get_workshop_info(filename):
    category = []
    title = []
    duration = []
    location = []
    with open(filename, mode='r', encoding='utf-8') as workshops_info_file:
        for workshop_info in workshops_info_file:
            category.append(workshop_info.split('#$')[1])
            title.append(workshop_info.split('#$')[2])
            duration.append(workshop_info.split('#$')[3])
            location.append(workshop_info.split('#$')[4])
    return category, title, duration, location


def read_message(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def send_mail():
    # setting up the file locations and user mail info
    setup_file_location()
    setup_mail_user_info()

    names, emails = get_contacts(contactFileLocation)  # read contacts
    message_template = read_message(messageFileLocation)  # read messages
    workshops_category, workshops_title, workshops_duration, workshops_location = get_workshop_info(workshopFileLocation) # read workshop information
    try:
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(emailAddress, emailPassword)

        # For each contact, send the email:
        for name, email in zip(names, emails):
            for workshop_category, workshop_title, workshop_duration, workshop_location in zip(workshops_category, workshops_title, workshops_duration, workshops_location):
                msg = MIMEMultipart()  # create a message

                # add in the actual person name to the message template
                message = message_template.substitute(
                            PERSON_NAME=name.title(),
                            WORKSHOP_CATEGORY=workshop_category.title(),
                            WORKSHOP_TITLE=workshop_title.title(),
                            WORKSHOP_DURATION=workshop_duration.title(),
                            WORKSHOP_LOCATION=workshop_location.title()
                            )

                # Prints out the message body for our sake
                print(message)

                # setup the parameters of the message
                msg['From'] = emailAddress
                msg['To'] = email
                msg['Subject'] = "CTE Workshop Meeting - " + workshop_title + " - Notification"

                # add in the message body
                msg.attach(MIMEText(message, 'html'))

                # send the message via the server set up earlier.
                s.send_message(msg)
                del msg

        print("Mail sent....")
        # Terminate the SMTP session and close the connection
        s.quit()
    except smtplib.SMTPAuthenticationError:
        print('Email username and password mismatch...\nEmail Not Sent...')
    except MIMEMultipart:
        print('MIMEMultipart errored...\nEmail Not Sent...')
    except MIMEText:
        print('MIMEText errored...\nEmail Not Sent...')
    except:
        print('Error occurred... Email Not Sent...')


'''
Previews:
Mail reception:
Subject: CTE Workshop Meeting - Collaboration through iLearn - Notification

Dear Kevtastic Kraken ,

You have a Workshop Session scheduled today.


Workshop Information Summary: 
Workshop Category: Blended Classroom
Workshop Title: Collaboration Through Ilearn
Workshop Duration Info: March 22Nd, 11:00 Am - 12:00 Pm
Location: Library 303, Library Building

Thanks & regards, 
Vivek Vellaiyappan Surulimuthu 
Digital Education Representative 
Marist College 
Vivek.Surulimuthu1@marist.edu

Program:
D:\Python36\python.exe D:/DigitalEdWorkshopAutoMail/DigitalEdWorkshopAutoMail/SourceRoot/WebsiteBlock/ScheduledInfoDeliverer/scheduledinfodelivery/WorkshopInfoHandler.py
<html>
    <body>
        <p>
            Dear Vivek Vellaiyappan ,

            <p>
                You have a Workshop Session scheduled today.
            </p>

            <br>Workshop Information Summary:
            <br><ul>
                <li><b>Workshop Category:</b> Blended Classroom </li>
                <li><b>Workshop Title:</b> Collaboration Through Ilearn </li>
                <li><b>Workshop Duration Info:</b> March 22Nd, 11:00 Am - 12:00 Pm </li>
                <li><b>Location: </b>Library 303, Library Building
</li>
            </ul>


            <br>Thanks & regards,
            <br>Vivek Vellaiyappan Surulimuthu
            <br>Digital Education Representative
            <br>Marist College
            <br>Vivek.Surulimuthu1@marist.edu
        </p>
    </body>
</html>

<html>
    <body>
        <p>
            Dear Vivek Vellaiyappan ,

            <p>
                You have a Workshop Session scheduled today.
            </p>

            <br>Workshop Information Summary:
            <br><ul>
                <li><b>Workshop Category:</b> New Category </li>
                <li><b>Workshop Title:</b> New Title </li>
                <li><b>Workshop Duration Info:</b> New Duration </li>
                <li><b>Location: </b>New Location</li>
            </ul>


            <br>Thanks & regards,
            <br>Vivek Vellaiyappan Surulimuthu
            <br>Digital Education Representative
            <br>Marist College
            <br>Vivek.Surulimuthu1@marist.edu
        </p>
    </body>
</html>

<html>
    <body>
        <p>
            Dear Kevtastic Kraken ,

            <p>
                You have a Workshop Session scheduled today.
            </p>

            <br>Workshop Information Summary:
            <br><ul>
                <li><b>Workshop Category:</b> Blended Classroom </li>
                <li><b>Workshop Title:</b> Collaboration Through Ilearn </li>
                <li><b>Workshop Duration Info:</b> March 22Nd, 11:00 Am - 12:00 Pm </li>
                <li><b>Location: </b>Library 303, Library Building
</li>
            </ul>


            <br>Thanks & regards,
            <br>Vivek Vellaiyappan Surulimuthu
            <br>Digital Education Representative
            <br>Marist College
            <br>Vivek.Surulimuthu1@marist.edu
        </p>
    </body>
</html>

<html>
    <body>
        <p>
            Dear Kevtastic Kraken ,

            <p>
                You have a Workshop Session scheduled today.
            </p>

            <br>Workshop Information Summary:
            <br><ul>
                <li><b>Workshop Category:</b> New Category </li>
                <li><b>Workshop Title:</b> New Title </li>
                <li><b>Workshop Duration Info:</b> New Duration </li>
                <li><b>Location: </b>New Location</li>
            </ul>


            <br>Thanks & regards,
            <br>Vivek Vellaiyappan Surulimuthu
            <br>Digital Education Representative
            <br>Marist College
            <br>Vivek.Surulimuthu1@marist.edu
        </p>
    </body>
</html>

Mail sent....
'''