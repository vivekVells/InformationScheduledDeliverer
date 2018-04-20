from django.contrib import admin
from . models import User, UserInfo, Information, UserLog

admin.site.register(User)
admin.site.register(UserInfo)
admin.site.register(UserLog)
admin.site.register(Information)
