from django.contrib import admin
from django.contrib.sessions.models import Session
from models import Step


class SessionAdmin(admin.ModelAdmin):

    def _session_data(self, obj):
        return obj.get_decoded()

    list_display = ['_session_data']


class StepAdmin(admin.ModelAdmin):
    pass


admin.site.register(Session, SessionAdmin)
admin.site.register(Step, StepAdmin)
