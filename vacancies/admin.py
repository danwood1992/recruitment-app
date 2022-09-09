from django.contrib import admin

# Register your models here.
from.models import Vacancy, Tag, Salary, hourlyWage, jobType, Benefit

admin.site.register(Vacancy)
admin.site.register(Tag)
admin.site.register(Salary)
admin.site.register(hourlyWage)
admin.site.register(jobType)
admin.site.register(Benefit)