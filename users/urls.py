from django.urls import path
from .views import register, user_login, user_logout
​
app_name = 'users'
​
urlpatterns = [
​
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('user_login/', user_login, name='user_login'),
    path('students/', students, name='students')
]
