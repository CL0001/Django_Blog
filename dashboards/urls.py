from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # Category curd
    path('categories/', views.categories, name='categories'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:pk>/', views.edit_category, name='edit_category'),
    path('delete_category/<int:pk>/', views.delete_category, name='delete_category'),

    # Blog curd
    path('posts/', views.posts, name='posts'),
    path('post/add/', views.add_post, name='add_post'),
    path('post/edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('post/delete/<int:pk>/', views.delete_post, name='delete_post'),
]