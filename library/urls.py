from django.urls import path
from library.views import home_form

urlpatterns = [
    path('', home_form),
]
