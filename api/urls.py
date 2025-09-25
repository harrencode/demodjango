from django.urls import path, include
from .views import todo_items_create, todo_items_detail, todo_items_all
from django.contrib import admin
from api.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns= [
    path("todoitems/", todo_items_all, name="all-todoitems"),
    path("todoitems/create/", todo_items_create, name="todoitem-view-create"),
    path("todoitems/<int:pk>/", todo_items_detail, name="todoitem-view-detail"),



    path ('user/register/', UserCreate.as_view(), name='user_create'),
    path ('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path ('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path ('auth/user/', UserDetailView.as_view(), name='user_detail'),
    path ('google/validate_token/', validate_google_token, name='validate_token'),


    #three paths have been added to url.py as they are nor in the api/


]