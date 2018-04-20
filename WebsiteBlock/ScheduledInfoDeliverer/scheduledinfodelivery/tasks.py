from .WorkshopInfoHandler import send_mail
# from __future__ import absolute_import, unicode_literals # this thing is making few import issues. dig deeper on this
import random
from celery import task

@task(name="send_email_task")
def send_email_task():
    print("sending email task...")
    send_mail()
