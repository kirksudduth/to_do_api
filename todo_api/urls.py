from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from todo.views import *

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', PostView.as_view(), name="test"),
    path('register/', register, name="register"),
    path('create/', PostCreateView.as_view(), name="create"),
    path('create-list/', PostListCreateView.as_view(), name="create-list"),
    path('api/token/', obtain_auth_token, name="obtain-token"),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
