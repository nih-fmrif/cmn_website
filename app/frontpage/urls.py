from django.conf.urls import url
from frontpage import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^workshops$', views.WorkshopView.as_view()),
    url(r'^dsst$', views.DSSTView.as_view()),
]
