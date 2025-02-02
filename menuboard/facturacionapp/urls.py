from django.urls import path

from estadisticas import views
from .views import *

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('create-checkout-session/', create_checkout_session, name='create_checkout_session'),
    path('success/<int:factura_id>/', payment_success, name='payment_success'),
    path('cancel/', payment_cancel, name='payment_cancel'),
    path('index/',views.index)
]