from django.urls import path

from toy.views import current_datetime, display_request, carousel_view

urlpatterns = [
    path('', carousel_view),
    path('demo', display_request)
]
