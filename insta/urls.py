from django.urls import path
from .views import (
    HomePageView,
    UserView, UserFollowView, UserUnfollowView,
    InstaPostView, InstaPostLikeView, InstaPostUnlikeView
)

urlpatterns = [
    path('users', UserView.as_view(), name='users'),
    path('users/follow', UserFollowView.as_view(), name='user_follow'),
    path('users/unfollow', UserUnfollowView.as_view(), name='user_unfollow'),
    path('posts', InstaPostView.as_view(), name='posts'),
    path('posts/like', InstaPostLikeView.as_view(), name='post_like'),
    path('posts/unlike', InstaPostUnlikeView.as_view(), name='post_unlike'),
    path('home', HomePageView.as_view(), name='home_page')
]