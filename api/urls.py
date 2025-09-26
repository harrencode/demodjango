from django.urls import path, include
from .views import todo_items_create, todo_items_detail, todo_items_all

urlpatterns= [
    # path("",views.home, name="home"),
    path("todoitems/", todo_items_all, name="all-todoitems"),
    path("todoitems/create/", todo_items_create, name="todoitem-view-create"),
    path("todoitems/<int:pk>/", todo_items_detail, name="todoitem-view-detail"),
    path("v1/auth/", include("dj_rest_auth.urls")),

]