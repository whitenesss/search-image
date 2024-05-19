from django.urls import path

from search_image.views import index

urlpatterns = [
    path('', index)
]

