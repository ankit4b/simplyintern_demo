from django.contrib import admin

from .models import Company, Internship, Profile, InternshipAppliedDB


class InternshipInline(admin.TabularInline):
    model = Internship

class ProfileInline(admin.TabularInline):
    model = Profile

class CompanyAdmin(admin.ModelAdmin):
    model = Company
    inlines = [ProfileInline, InternshipInline]


admin.site.register(Company, CompanyAdmin)
admin.site.register(Internship)
admin.site.register(Profile)
admin.site.register(InternshipAppliedDB)
# admin.site.register(Internship)
