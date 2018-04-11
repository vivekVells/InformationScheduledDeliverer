from django.shortcuts import render, redirect
from . forms import LoginForms, RegisterForms, InfoForms, SchedForms, EmailForms
from django.core.exceptions import ObjectDoesNotExist
from . models import User, UserInfo, Information, ScheduleInforDeliver
from django.http import HttpResponse
from . import scheduler
from . import tasks

# user_ref is used to show the username at home page
user_exists = False
user_ref = ''


def logout(request):
    del_session(request)
    return redirect('index')


def del_session(request):
    global user_exists, user_ref
    user_exists = False
    user_ref = ''

    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponse('Session deleted...')


def validate_login(request):
    global user_exists, user_ref

    try:
        user = User.objects.get(username=request.POST['username'])
        if user.password == request.POST['password']:
            print('password matched...')
            user_exists = True
            user_ref = request.POST['username']
            request.session['user_id'] = user.id
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
    sched_form = SchedForms()
    email_form = EmailForms()

    if user_exists:
        if request.method == 'POST' and info_form.is_valid:
            return redirect('home')
        else:
            context = {'request':request, 'infoform' : info_form, 'schedform' : sched_form, 'emailform' : email_form, 'username' : user_ref}
            return render(request, 'scheduledinfodelivery/home.html', context)
    else:
        return HttpResponse('Login again using the link: \'http://127.0.0.1:8000/infodeliver/\' ')

def handle_info(request):
    pass


def schedule(request):
    if user_exists and request.method == 'POST':
        '''
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
        '''

        '''
        scheduler.set_username(user_ref)
        user_obj = User.objects.get(username=str(user_ref))
        user_scheduler = user_obj.scheduleinfordeliver_set.all()[0]

        # the following are the updation quries
        user_scheduler.job_status = 'start'
        user_scheduler.job_type = 'email'
        user_scheduler.job_info_content = request.POST['info_content']
        user_scheduler.day = request.POST['day']
        user_scheduler.hour = request.POST['hour']
        user_scheduler.minute = request.POST['minute']
        user_scheduler.second = request.POST['second']

        # have to create a db entry for this one
        email_receiver = request.POST['to_address']
        email_subject = request.POST['email_subject']

        # never forget to save after updation
        user_scheduler.save()
        '''

        scheduler.job_start(
            'start',
            'email',
            request.POST['to_address'],
            request.POST['email_subject'],
            request.POST['info_content'],
            request.POST['day'],
            request.POST['hour'],
            request.POST['minute'],
            request.POST['second']
        )

        '''
        tasks.send_email_task.delay(
            'email', 'message'
        )
        '''
        return redirect('home')
    else:
        return redirect('index')


def stop_schedule(request):
    if user_exists:
        user_obj = User.objects.get(username=user_ref)
        user_scheduler = user_obj.scheduleinfordeliver_set.all()[0]

        user_scheduler.job_status = 'stop'
        user_scheduler.save()
        # scheduler.set_job_status('stop')
        scheduler.job_start()
        return redirect('home')
    else:
        return redirect('index')

