from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics

from api import serializers
from api.models import Post


class UserList(generics.ListAPIView):
    """view for get data about all users"""

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """view for get data about a specific user"""

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class PostList(generics.ListCreateAPIView):
    """view for get and create for a list of posts"""

    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        """Allows the creation of a post"""
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """view for get, update and delete a specific post"""

    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
