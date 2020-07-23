from django.urls import path
from api.views import APIDataView


urlpatterns = [
    path('', APIDataView.as_view()),
]