from django.urls import path
from .views import FridgeView

urlpatterns = [
    path('fridge/', FridgeView().as_view(), name='fridge_view')
]