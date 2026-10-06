from django.contrib import admin

from .models import User, UserVerificationCode


admin.site.register([User, UserVerificationCode])
