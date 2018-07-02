from django.urls import include, path
from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginView, name='login'),
    url(r'^logout/', views.logoutview, name='logout'),
]
