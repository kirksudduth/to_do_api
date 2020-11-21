from django.shortcuts import render


# 3rd party imports
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post

class TestView(APIView):
    def get(request, *args, **kwargs):
        data = {
            "Name": "Gary",
            "ToDo": "Learn to Code",
        }
        return Response(data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
# Create your views here.
