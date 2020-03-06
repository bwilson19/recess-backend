from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('games/', views.GameList.as_view(), name='game_list'),
    path('games/<int:pk>', views.GameDetail.as_view(), name='game_detail'),
    path('leagues/', views.LeagueList.as_view(), name="league_list"),
    path('leagues/<int:pk>', views.LeagueDetail.as_view(), name="league_detail"),
    path('users/', views.UserProfileList.as_view(), name="user_list"),
    path('users/<int:pk>', views.UserProfileDetail.as_view(), name="user_detail"),
    path('posts/', views.PostList.as_view(), name="post_list"),
    path('posts/<int:pk>', views.PostDetail.as_view(), name="post_detail"),
    path('comments/', views.CommentList.as_view(), name="comment_list"),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name="comment_detail"),
]
