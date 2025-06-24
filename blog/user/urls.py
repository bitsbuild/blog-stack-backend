from django.urls import path
from user.views import create_user,delete_user
from rest_framework.authtoken.views import obtain_auth_token
ulrpatterns = [
    path('create/',create_user,name='create'),
    path('token/',obtain_auth_token,name='token'),
    path('delete/',delete_user,name='delete'),
]