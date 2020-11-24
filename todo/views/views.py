from django.shortcuts import render


# 3rd party imports
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from ..serializers import PostSerializer
from ..models import Post


class PostView(mixins.ListModelMixin, 
        mixins.CreateModelMixin,
        generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

    def perform_create(self, serializer):
        # send an email
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# class TestView(APIView):

#     permission_classes = (IsAuthenticated,)

#     def get(request, *args, **kwargs):
#         qs = Post.objects.all()
#         post = qs.first()
#         # for serializing one instance of the queryset
#         serializer = PostSerializer(post)
#         # serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
