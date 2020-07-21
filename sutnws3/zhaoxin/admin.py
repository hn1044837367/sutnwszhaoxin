from django.contrib import admin

from zhaoxin.models import Student,StudentAd


class StuAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'sex', 'subject', 'phone', 'first', 'second', 'command','interview')
    ordering = ('id', )


class StuAdAdmin(admin.ModelAdmin):

    list_display = ( 'name','password')
    ordering = ('name',)


admin.site.register(Student, StuAdmin)
admin.site.register(StudentAd, StuAdAdmin)
