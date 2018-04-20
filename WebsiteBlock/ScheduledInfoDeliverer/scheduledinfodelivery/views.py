import os
from django.shortcuts import render, redirect
from . forms import LoginForms, RegisterForms, InfoForms, SchedForms, EmailForms
from . WorkshopInfoHandler import get_workshop_info
from django.core.exceptions import ObjectDoesNotExist
from . models import User, UserInfo, Information, UserLog
from django.http import HttpResponse
from . import scheduler
from django.utils import timezone

# this is how we could access other directory
import sys
sys.path.append(os.path.join('..', 'ScheduledInfoDeliverer'))
from ScheduledInfoDeliverer import settings

# user_ref is used to show the username at home page
user_exists = False
user_ref = ''
user_log_obj = ''


def logout(request):
    try:
        user_log_obj.last_logged_out=timezone.now()
        user_log_obj.save()
    except User.DoesNotExist:
        print('Error occurred while trying to log the logout')
    del_session(request)
    return redirect('index')

def del_session(request):
    global user_exists, user_ref, user_log_obj
    user_exists = False
    user_ref = ''
    user_log_obj = ''

    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponse('Session deleted...')


def validate_login(request):
    global user_exists, user_ref, user_log_obj

    try:
        user = User.objects.get(username=request.POST['username'])
        if user.password == request.POST['password']:
            print('password matched...')
            user_exists = True
            user_ref = request.POST['username']
            request.session['user_id'] = user.id
            user_log_obj = user.userlog_set.create(last_logged_in=timezone.now())
            return True
        else:
            print('password does not match....')
            del_session(request)
            return False
    except User.DoesNotExist:
        print('value does not exist in table...')
        del_session(request)
        return False


def index(request):
    login_form = LoginForms()

    if request.method == 'POST':
        if login_form.is_valid:
            if validate_login(request):
                return redirect('home')
            else:
                context = {'loginform' : login_form, 'message' : 'Username and Password did not match'}
                return render(request, 'scheduledinfodelivery/index.html', context)
    else:
        del_session(request)
        context = {'loginform' : login_form}
        return render(request, 'scheduledinfodelivery/index.html', context)


def register(request):
    register_form = RegisterForms()

    if request.method == 'POST' and register_form.is_valid:
        user_obj = User(
            username = request.POST['username'],
            password=request.POST['password'],
            recovery_answer=request.POST['recovery_answer'],
            recovery_email=request.POST['recovery_email']
        )
        user_obj.save()

        userinfo_obj = UserInfo(
            user = user_obj,
            first_name=request.POST['first_name'],
            middle_name=request.POST['middle_name'],
            department=request.POST['department'],
            last_name=request.POST['last_name'],
            phone_number=request.POST['phone_number']
        )
        userinfo_obj.save()

        return redirect('index')
    else:
        context = {'regform' : register_form}
        return render(request, 'scheduledinfodelivery/register.html', context)


def home(request):
    info_form = InfoForms()
    email_form = EmailForms()
    TEMPLATE_WORKSHOP_INFO_DIR = os.path.join(list(settings.TEMPLATE_DIRS)[0], 'scheduledinfodelivery', 'workshopinfo.txt')
    workshops_category, workshops_title, workshops_duration, workshops_location = get_workshop_info(TEMPLATE_WORKSHOP_INFO_DIR) # read workshop information
    # using zip to iterate over all workshop info entities easily
    workshops_info = zip(workshops_category, workshops_title, workshops_duration, workshops_location)
    if user_exists:
        if request.method == 'POST' and info_form.is_valid:
            return redirect('home')
        else:
            context = {'username' : user_ref,
                       'infoform' : info_form,
                       'emailform' : email_form,
                       'workshops_info' : workshops_info,
                       }
            return render(request, 'scheduledinfodelivery/home.html', context)
    else:
        return HttpResponse('Login again using the link: \'http://127.0.0.1:8000/infodeliver/\' ')

def handle_info(request):
    pass


def schedule(request):
    if user_exists and request.method == 'POST':
        scheduler.set_job_status('start')
        scheduler.set_job_type(
            'email', request.POST['info_content']
        )
        scheduler.set_schedule_parameters(
            request.POST['day'],
            request.POST['hour'],
            request.POST['minute'],
            request.POST['second']
        )
        scheduler.job_start()
        return redirect('home')
    else:
        return redirect('index')


def stop_schedule(request):
    if user_exists:
        scheduler.set_job_status('stop')
        scheduler.job_start()
        return redirect('home')
    else:
        return redirect('index')

