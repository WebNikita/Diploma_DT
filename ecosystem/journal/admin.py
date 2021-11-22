from django.contrib import admin
from .models import Student, Teacher, School_subject, Group, Turnout


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(School_subject)
class School_subjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Turnout)
class TurnoutAdmin(admin.ModelAdmin):
    pass
