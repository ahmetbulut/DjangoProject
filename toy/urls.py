from django.urls import path

from toy.views import current_datetime, display_request, current_datetime_better

urlpatterns = [
    path('', current_datetime_better),
    path('demo', display_request)
]
