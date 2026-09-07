from django.urls import path
from .views import *

urlpatterns = [

    # Single Page Portfolio
    path('', Home.as_view(), name='home'),

    # Contact Form
    path('contact/', ContactView.as_view(), name='contact'),

    # Admin
    path('admin-login/', AdminLogin.as_view(), name='admin_login'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('view/<int:id>/', ViewContact.as_view(), name='view'),
    path('edit/<int:id>/', EditContact.as_view(), name='edit'),
    path('delete/<int:id>/', DeleteContact.as_view(), name='delete'),
]