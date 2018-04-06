'''
This program handles the scheduling job parts
'''

import schedule, datetime

from . utility import sendemail

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

days = 0
hours = 0
minutes = 0
seconds = 0
job_status = 'idle'
job_type = ''
job_info_content = 'Vivek, stay hungry. stay foolish. Never give up!'


def set_job_type(job_type_arg, job_info_content_arg):
    global job_type, job_info_content
    job_type = job_type_arg
    job_info_content = job_info_content_arg


def get_job_type_alone():
    global job_type
    return job_type


def get_job_info_content_alone():
    global job_info_content
    return 'Vivek, stay hungry. stay foolish. Never give up!'


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
    global job_status
    return job_status


def get_schedule_parameters():
    global days, hours, minutes, seconds
    return days, hours, minutes, seconds


def set_job_function():
    pass


def job_start():
    print('Job Status: ', get_job_status())
    if get_job_status() == 'start':
        while True:
            day_arg, hour_arg, minute_arg, second_arg = get_schedule_parameters()
            print('Job is running...')
            if get_job_type_alone() == 'email':
                schedule.every(second_arg).seconds.do(
                    sendemail.send_mail(
                        'askkeviv@gmail.com',
                        'digitaled123',
                        'techengineervivek@gmail.com',
                        'Scheduled email at' + datetime.datetime.now().strftime('%H:%M:%S'),
                        get_job_info_content_alone()
                    )
                )
    elif get_job_status() == 'stop':
        schedule.clear('daily-tasks')
        print('Job stopped...')
    else:
        print('No Job is running...')
        pass

# have to use this one!
'''    
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
        pass
'''


def schedule_job(day, hour, minute, second):
    pass