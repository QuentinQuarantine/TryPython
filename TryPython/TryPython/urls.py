from django.conf.urls import include, url
from django.contrib import admin
from core.views import IndexView, EvalView
from tutorial.views import StepView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r"^$", IndexView.as_view()),
    url(r"^eval", EvalView.as_view()),
    url(r"^step", StepView.as_view())
]
