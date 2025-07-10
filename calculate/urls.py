from django.urls import path
from calculate.views import calculator_view
urlpatterns = [
    path('', calculator_view)
]