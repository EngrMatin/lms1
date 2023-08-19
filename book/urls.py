"""
URL configuration for book app.

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
    # path('about/', views.about, name='about'),              # for function based view
    # path('about/', views.TemplateView.as_view(template_name='about.html')),          # without creating any view
    path('about/<int:roll>/', views.MyTemplateView.as_view(template_name='about.html'), {'author':'Sakib'}, name='about'),          # for class based view # template_name='' is optional and will override template_name='' in the views.py
    # path('add/', views.add_book, name='add_book'),
    path('add/', views.AddBookView.as_view(), name='add_book'),
    # path('show/', views.show_book, name='show_book'),
    path('show/', views.BookListView.as_view(), name='show_book'),
    path('details/<int:id>', views.BookDetailsView.as_view(), name='book_details'),
    # path('edit/<int:id>', views.edit_book, name='edit_book'),
    path('edit/<int:pk>', views.UpdateBookView.as_view(), name='edit_book'),
    # path('delete/<int:id>', views.delete_book, name='delete_book'),
    path('delete/<int:pk>', views.DeleteBookView.as_view(), name='delete_book'),
    
]
