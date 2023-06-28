from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.login_view, name='login'),
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('add new/', views.new_data_view, name='new_data'),
]