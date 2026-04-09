from django.urls import path
from . import views
from .views import logout_view

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-coding/', views.add_coding, name='add_coding'),
    path('register/', views.register, name='register'),
    path('viva/', views.viva_page, name='viva'),
    path('edit-coding/<int:pk>/', views.edit_coding, name='edit_coding'),
    path('delete-coding/<int:pk>/', views.delete_coding, name='delete_coding'),
    path('mock-interview/', views.start_mock, name='mock_interview'),
    path('generate-ai-mock/', views.generate_ai_mock, name='generate_ai_mock'),
path('ai-mock/', views.ai_mock, name='ai_mock'),
 path('logout/', logout_view, name='logout'),
# path('generate-mock/', views.generate_mock, name='generate_mock'),
]