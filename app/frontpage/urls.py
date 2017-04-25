from django.conf.urls import url
from frontpage import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]