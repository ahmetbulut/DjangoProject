from django.urls import path
from library.views import home, save_author, home_form

urlpatterns = [
    path('', home_form),
    path('success', save_author)
]
