from django.urls import path, include, re_path
from .views import todo_items_create, todo_items_detail, todo_items_all
from accounts.views import GoogleLogin, GoogleLoginCallback

urlpatterns= [
    # path("",views.home, name="home"),
    path("todoitems/", todo_items_all, name="all-todoitems"),
    path("todoitems/create/", todo_items_create, name="todoitem-view-create"),
    path("todoitems/<int:pk>/", todo_items_detail, name="todoitem-view-detail"),
    path("v1/auth/", include("dj_rest_auth.urls")),
    path('v1/auth/registration/', include('dj_rest_auth.registration.urls')),

    path("v1/auth/", include("dj_rest_auth.urls")),
    re_path(r"^v1/auth/accounts/", include("allauth.urls")),
    path("v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path("v1/auth/google/", GoogleLogin.as_view(), name="google_login"),
    path("v1/auth/google/callback/",  GoogleLoginCallback.as_view(), name="google_login_callback",),

]