"""
URL configuration for user app.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('show/', views.show_user, name='show_user'),
    path('edit/<int:id>', views.edit_user, name='edit_user'),
    path('update/', views.update_user, name='update_user'),
    path('delete/<int:id>', views.delete_user, name='delete_user'),
    path('login/>', views.user_login, name='user_login'),
    path('profile/>', views.user_profile, name='user_profile'),
    path('logout/>', views.user_logout, name='user_logout'),
    path('change_pass/>', views.change_password, name='change_pass'),
    path('reset_pass/>', views.reset_password, name='reset_pass'),
    
]
