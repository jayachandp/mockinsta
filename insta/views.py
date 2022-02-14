from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import InstaPost, UserFollow
from .serializers import UserSerializer, InstaPostSerializer

# Create your views here.
class UserView(ListAPIView, RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class InstaPostView(ListAPIView):
    serializer_class = InstaPostSerializer

    def get_queryset(self):
        queryset = sorted(InstaPost.objects.all(), key=lambda post: post.no_of_likes, reverse=True)
        return queryset


class UserFollowView(APIView):
    
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        follower = request.user
        try:
            user = User.objects.get(id=user_id)
            UserFollow.objects.create(user=user, follower=follower)
        except User.DoesNotExist:
            return Response(
                {'Error': f'User with {user_id} not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        except IntegrityError:
            return Response(
                {'Error': f'{str(follower)} already follows {str(user)}'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {'Message': f'Succesfully followed {str(user)}'},
            status=status.HTTP_201_CREATED
        )


class UserUnfollowView(APIView):
    
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        follower = request.user
        try:
            user = User.objects.get(id=user_id)
            UserFollow.objects.get(user=user, follower=follower).delete()
        except User.DoesNotExist:
            return Response(
                {'Error': f'User with {user_id} not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        except UserFollow.DoesNotExist:
            return Response(
                {'Error': f'{str(follower)} does not follow {str(user)}'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {'Message': f'Succesfully unfollowed {str(user)}'},
            status=status.HTTP_200_OK
        )


class InstaPostLikeView(APIView):
    
    def post(self, request, *args, **kwargs):
        post_id = request.data.get('post_id')
        try:
            insta_post = InstaPost.objects.get(id=post_id)
            insta_post.likes.add(request.user)
        except InstaPost.DoesNotExist:
            return Response(
                {'Error': f'Post with f{post_id} not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            {'Message': f'Succesfully liked {str(insta_post)}'},
            status=status.HTTP_201_CREATED
        )


class InstaPostUnlikeView(APIView):

    def post(self, request, *args, **kwargs):
        post_id = request.data.get('post_id')
        try:
            insta_post = InstaPost.objects.get(id=post_id)
            insta_post.likes.remove(request.user)
        except InstaPost.DoesNotExist:
            return Response(
                {'Error': f'Post with f{post_id} not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            {'Message': f'Succesfully unliked {str(insta_post)}'},
            status=status.HTTP_201_CREATED
        )


class HomePageView(ListAPIView):
    serializer_class = InstaPostSerializer

    def get_queryset(self):
        following = UserFollow.objects.filter(
            follower=self.request.user
        ).values_list('user', flat=True)
        insta_posts = InstaPost.objects.filter(
            owner__in=following
        ).order_by('-post_added')
        return insta_posts

