from django.shortcuts import render


# 3rd party imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post

class TestView(APIView):

    permission_classes = (IsAuthenticated,)
    def get(request, *args, **kwargs):
        qs = Post.objects.all()
        post = qs.first()
        # for serializing one instance of the queryset
        serializer = PostSerializer(post)
        # serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
# Create your views here.
