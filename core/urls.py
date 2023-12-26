from django.urls import path
from . import views


urlpatterns = [
    path('create-person', views.CreatePersonView.as_view(), name='create_person'),
    path('load-towns', views.load_towns)
]