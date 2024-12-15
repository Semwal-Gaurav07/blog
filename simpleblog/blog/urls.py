from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('article/<int:pk>', views.article_detail_view, name="article-detail"),
    path('add_post/', views.add_post_view, name="add_post"),
    path('add_category/', views.add_category_view, name="add_category"),
    path('article/edit/<int:pk>', views.update_post_view, name='update_post'),
    path('article/<int:pk>/remove', views.delete_post_view, name='delete_post'),
    path('category/<str:cats>/', views.category_view, name='category'),
    path('category-list/', views.category_list_view, name='category-list'),
    path('like/<int:pk>', views.like_view, name='like_post'),
    path('article/<int:pk>/comment/', views.add_comment_view, name="add_comment"),
]
