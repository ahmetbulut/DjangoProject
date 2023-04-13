from django.urls import path
from library.views import home, save_author

urlpatterns = [
    path('', home),
    path('success', save_author)
]
