from django.contrib import admin

from .models import Student,StudentAdmin,lab,labAdmin
# Register your models here.
admin.site.register(Student,StudentAdmin)
admin.site.register(lab,labAdmin)
