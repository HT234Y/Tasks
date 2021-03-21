from django.urls import path

from django.contrib.auth import views as authViews
from users import views as userViews

from . import views


urlpatterns = [
	path('registration/', userViews.register, name = 'reg'),
	path('login/', authViews.LoginView.as_view(template_name='users/login.html'), name="login"),
]