import six
from django.contrib import admin

if six.PY2:
    from models import Step
else:
    from .models import Step


class StepAdmin(admin.ModelAdmin):
    pass

admin.site.register(Step, StepAdmin)
