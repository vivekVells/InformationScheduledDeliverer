'''
This program handles the scheduling job parts
https://code.tutsplus.com/tutorials/managing-cron-jobs-using-python--cms-28231
'''

import schedule, datetime, time
from . models import User, ScheduleInforDeliver
from . tasks import send_email_task

'''
def stopMailer():
    schedule.clear('daily-tasks')
    print('Job Scheduled Stopped!')
'''

'''
def job():
    print("I'm working...")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
'''
'''
username = ''
days = 0
hours = 0
minutes = 0
seconds = 0
job_status = 'idle'
job_type = ''
job_info_content = 'Vivek, stay hungry. stay foolish. Never give up!'
'''

username = ''

def set_username(username_arg):
    global username
    username = username_arg


def get_username():
    return str(username)
'''
user_obj = User.objects.get(username='keviv22')
user_scheduler = user_obj.scheduleinfordeliver_set.all()[0]
job_status = user_scheduler.job_status
job_type = user_scheduler.job_type
job_info_content = user_scheduler.job_info_content
days = user_scheduler.day
hours = user_scheduler.hour
minutes = user_scheduler.minute
seconds = user_scheduler.second


def set_job_type(job_type_arg, job_info_content_arg):
    global job_type, job_info_content
    job_type = job_type_arg
    job_info_content = job_info_content_arg


def get_job_type_alone():
    # return job_type
    return user_scheduler.job_type


def get_job_info_content_alone():
    return str(user_scheduler.job_info_content)
    # return 'Vivek, stay hungry. stay foolish. Never give up!'


def set_schedule_parameters(day, hour, minute, second):
    global days, hours, minutes, seconds
    days = day
    hours = hour
    minutes = minute
    seconds = second
    print("Schedule parameters set...")


def set_job_status(job_status_arg):
    global job_status
    job_status = job_status_arg


def get_job_status():
    return user_scheduler.job_status


def get_schedule_parameters():
    # return days, hours, minutes, seconds
    return user_scheduler.day, user_scheduler.hour, user_scheduler.minute, user_scheduler.second


def set_job_function():
    pass
'''

def job_start(job_status, job_type, email_reciver, email_subject, email_info_content, day_arg, hour_arg, minute_arg, second_arg):
    print('Job Status: ', job_status)
    if job_status == 'start':
        # day_arg, hour_arg, minute_arg, second_arg = get_schedule_parameters()
        print('Job is running...')
        if job_type == 'email':
            send_email_task.delay(
                email_reciver,
                email_subject,
                email_info_content,
                day_arg,
                hour_arg,
                minute_arg,
                second_arg
            )
            # schedule.every(second_arg).seconds.do(send_mail_job)
    elif job_status == 'stop':
        schedule.clear('daily-tasks')
        print('Job stopped...')
    else:
        print('No Job is running...')

'''
# have to use this one!
while True:
    day_arg, hour_arg, minute_arg, second_arg = get_schedule_parameters()
    if get_job_status() == 'start':
        print('Job is running...')
        if get_job_type_alone() == 'email':
            schedule.every(10).seconds.do(
                sendemail.send_mail(
                    'askkeviv@gmail.com',
                    'digitaled123',
                    'techengineervivek@gmail.com',
                    'Scheduled email at' + datetime.datetime.now().strftime('%H:%M:%S'),
                    job_info_content
                )
            )
    elif get_job_status() == 'stop':
        schedule.clear('daily-tasks')
        print('Job stopped...')
    else:
        print('No Job is running...')
'''

def schedule_job(day, hour, minute, second):
    pass