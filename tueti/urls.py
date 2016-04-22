from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^list$', views.TuetList.as_view()),
]