from django.conf.urls import include, url
from django.contrib import admin
from try_python_tutorial.views import IndexView, EvalResponseView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r"^$", IndexView.as_view()),
    url(r"^eval", EvalResponseView.as_view())
]
