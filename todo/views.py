from django.shortcuts import render


# 3rd party imports
from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    def get(request, *args, **kwargs):
        data = {
            "Name": "Gary",
            "ToDo": "Learn to Code",
        }
        return Response(data)

# Create your views here.
