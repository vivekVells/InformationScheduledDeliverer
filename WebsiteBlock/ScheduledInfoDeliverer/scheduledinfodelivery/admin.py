from django.contrib import admin
from . models import User, UserInfo, Information, ScheduleInforDeliver

admin.site.register(User)
admin.site.register(UserInfo)
admin.site.register(Information)
admin.site.register(ScheduleInforDeliver)
