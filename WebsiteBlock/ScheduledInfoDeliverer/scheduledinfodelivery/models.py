from django.db import models
from django.utils import timezone

''''
Models AuthType and LoginUsing logic will be used after the prototype start
Model ScheduledInfo will be done later since got into a problem of inability to redirect while
    scheduled job is running
'''
class AuthType(models.Model):
    organizationyn = models.CharField(max_length=1)
    name = models.CharField(max_length=200)
    auth_passcode = models.CharField(max_length=200)
    created_on = models.DateTimeField(default=timezone.now)
    deleted_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '%s %s %s' % (self.organizationyn, self.name, self.auth_passcode)

class LoginUsing(models.Model):
    authtype = models.ForeignKey('AuthType', on_delete=models.CASCADE)
    organizationyn = models.CharField(max_length=1)

    def __str__(self):
        return '%s %s' % (self.authtype, self.organizationyn)

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    recovery_answer = models.CharField(max_length=20)
    recovery_email = models.CharField(max_length=20)
    created_on = models.DateTimeField(default=timezone.now)
    last_updated_on = models.DateTimeField(blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "ID: %d Username: %s Password: %s" % (self.id, self.username, self.password)


class UserInfo(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank=True, default='')
    last_name = models.CharField(max_length=40)
    department = models.CharField(max_length=50, default='')
    phone_number = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    deleted_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "ID: %d First Name: %s Middle Name: %s Last Name: %s Phone Number: %s" % (self.id, self.first_name, self.middle_name, self.last_name, self.phone_number)


class UserLog(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    last_logged_in = models.CharField(max_length=100)
    last_logged_out = models.CharField(max_length=100, blank=True, null=True)

class Information(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    data = models.CharField(max_length=10000)
    created_on = models.DateTimeField(default=timezone.now)
    deleted_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "%ID: %d type: %s data: %s" % (self.id, self.type, self.data)

'''
Will be implemented later. Unable to redirect properly when the scheduled job is running.
'''
class ScheduledInfo(models.Model):
    # user = models.ForeignKey('User', on_delete=models.CASCADE)
    duration_date = models.DateField()
    duration_time = models.TimeField()
    created_on = models.DateTimeField(default=timezone.now)
    deleted_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "%ID: duration_date: %s duration_time: %s " % (self.id, self.duration_date, self.duration_time)
