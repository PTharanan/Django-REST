from django.urls import path
from .views import SampleAPI

urlpatterns = [
    path('rest/', SampleAPI.as_view())
]

