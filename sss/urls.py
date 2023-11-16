from django.urls import path
from sss.views import home, get_customer, create_customer

urlpatterns = [
    path('', home),
    path('search', get_customer),
    path('create', create_customer)
]
