from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.user_register_view, name='register'),
    path('edit_profile/', views.user_edit_view, name='edit_profile'),
    path('password/', views.passwords_change_view, name='change_password'),
    path('password_success/', views.password_success, name='password_success'),
    path('<int:pk>/profile/', views.show_profile_page_view, name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', views.edit_profile_page_view, name='edit_profile_page'),
    path('create_profile_page/', views.create_profile_page_view, name='create_profile_page'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
