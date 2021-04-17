from django.contrib import admin
from .models import Student, Resume

# Register your models here
class ResumeInline(admin.TabularInline):
    model = Resume

class StudentAdmin(admin.ModelAdmin):
    model = Student
    inlines = [ResumeInline]


admin.site.register(Student, StudentAdmin)
admin.site.register(Resume)
