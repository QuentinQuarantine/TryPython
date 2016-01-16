from django.contrib import admin
from models import Step


class StepAdmin(admin.ModelAdmin):
    pass

admin.site.register(Step, StepAdmin)
