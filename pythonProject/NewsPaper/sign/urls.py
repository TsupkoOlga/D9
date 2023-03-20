from django.urls import path
from .views import ProfileView
from .views import upgrade_me

urlpatterns = [
    path('', ProfileView.as_view()),
    path('sign/upgrade/', upgrade_me, name = 'upgrade')
]