from django.urls import path
from .views.user import CustomerView
from .views.product import ShopViews

urlpatterns = [
    path('customers/', CustomerView.as_view()),
    path('shops/', ShopViews.as_view())
]