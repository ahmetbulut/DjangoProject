from django.urls import path

from toy.views import current_datetime, display_request, carousel_demo, plotly_demo, home

urlpatterns = [
    path('', home),
    path('carousel_demo', carousel_demo),
    path('plotly_demo', plotly_demo),
    path('demo', display_request)
]
