from django.conf.urls import include, url
from . import api_views

urlpatterns = [
    url(r'^list$', api_views.TuetListAPI.as_view()),
]