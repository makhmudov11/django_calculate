from django.urls import path
from calculate.views import calculator_view, history_view
urlpatterns = [
    path('history/', history_view),
    path('', calculator_view)
]