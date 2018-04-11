from celery import task
from celery.utils.log import get_task_logger
from . utility import sendemail

# def send_mail(sender_email='askkeviv@gmail.com',
# sender_email_password='digitaled123',
# receiver_email=None,
# subject=None,
# message=None):

logger = get_task_logger(__name__)

@task(name="send_feedback_email_task")
def send_email_task(email_reciver, email_subject, info_content, day_arg, hour_arg, minute_arg, second_arg):
    """sends an email when feedback form is filled successfully"""
    logger.info("Task started... Trying to send email...")
    sendemail.send_mail(
        'askkeviv@gmail.com',
        'digitaled123',
        str(email_reciver),
        str(email_subject),
        str(info_content)
    )
    # sendemail.send_mail('askkeviv@gmail.com', 'digitaled123', 'techengineervivek@gmail.com', 'Vivek. Never Give Up!', 'Stay Hungry Stay Foolsih')
