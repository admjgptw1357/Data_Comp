from django.contrib import admin

# Register your models here.

from django.contrib import admin
from app.models import Submission, Competition

admin.site.register(Competition)
admin.site.register(Submission)