from django.urls import path
from .views import *

urlpatterns = [

    path('', Home.as_view(), name='home'),

    path('about/', About.as_view(), name='about'),

    path('skills/', Skills.as_view(), name='skills'),

    path('resume/', Resume.as_view(), name='resume'),

    path('contact/', ContactView.as_view(), name='contact'),

    path('admin-login/', AdminLogin.as_view(), name='admin_login'),

    path('dashboard/', Dashboard.as_view(), name='dashboard'),

    path('view/<int:id>/', ViewContact.as_view(), name='view'),

    path('edit/<int:id>/', EditContact.as_view(), name='edit'),

    path('delete/<int:id>/', DeleteContact.as_view(), name='delete'),

]