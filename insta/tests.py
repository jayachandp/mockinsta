from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework.test import force_authenticate
from .models import InstaPost, UserFollow
from .views import (
    UserView, UserFollowView, UserUnfollowView, HomePageView,
    InstaPostView, InstaPostLikeView, InstaPostUnlikeView
)

# Create your tests here.
class TestUserView(APITestCase):
    fixtures = ["initial_data.json", ]

    def setUp(self):
        self.request_factory = APIRequestFactory()
        self.user = User.objects.get(id=4)
        self.view = UserView.as_view()

    def test_user_view(self):
        url = reverse('users')
        request = self.request_factory.get(url)
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), User.objects.all().count())


class TestUserFollowView(APITestCase):
    def setUp(self):
        self.request_factory = APIRequestFactory()
        self.user = User.objects.get(id=4)
        self.view = UserFollowView.as_view()
    
    def test_user_follow_view(self):
        url = reverse('user_follow')
        request = self.request_factory.post(url, data={'user_id': 2})
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class TestUserUnfollowView(APITestCase):
    def setUp(self):
        self.request_factory = APIRequestFactory()
        self.user = User.objects.get(id=4)
        self.view = UserUnfollowView.as_view()
    
    def test_user_unfollow_view(self):
        url = reverse('user_unfollow')
        request = self.request_factory.post(url, data={'user_id': 3})
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class TestInstaPostView(APITestCase):
    def setUp(self):
        self.request_factory = APIRequestFactory()
        self.user = User.objects.get(id=4)
        self.view = InstaPostView.as_view()
    
    def test_user_unfollow_view(self):
        url = reverse('posts')
        request = self.request_factory.get(url)
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class TestInstaPostLikeView(APITestCase):
    def setUp(self):
        self.request_factory = APIRequestFactory()
        self.user = User.objects.get(id=4)
        self.view = InstaPostLikeView.as_view()
    
    def test_instapost_like_view(self):
        url = reverse('posts_like')
        request = self.request_factory.post(url, data={'post_id': 1})
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class TestInstaPostUnlikeView(APITestCase):
    def setUp(self):
        self.request_factory = APIRequestFactory()
        self.user = User.objects.get(id=4)
        self.view = InstaPostUnlikeView.as_view()
    
    def test_instapost_unlike_view(self):
        url = reverse('posts_unlike')
        request = self.request_factory.post(url, data={'post_id': 2})
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class TestHomePageView(APITestCase):
    def setUp(self):
        self.request_factory = APIRequestFactory()
        self.user = User.objects.get(id=4)
        self.view = HomePageView.as_view()
    
    def test_instapost_unlike_view(self):
        url = reverse('home_page')
        request = self.request_factory.get(url)
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
