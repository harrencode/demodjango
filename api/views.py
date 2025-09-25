from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from rest_framework import generics, status
from . serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from allauth.socialaccount.models import SocialToken, SocialAccount
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from.models import TodoItem
from.serializers import TodoItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.

# def home(request):
#     return HttpResponse("hello django")


# class TodoListCreate(generics.ListCreateAPIView):
#     queryset=TodoItem.objects.all()
#     serializer_class=TodoItemSerializer

@api_view(['GET'])
def todo_items_all(request):
    try:
        todoitems=TodoItem.objects.all()
        serilaizer=TodoItemSerializer(todoitems,many=True)
        return Response(serilaizer.data)
    except TodoItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def todo_items_create(request):
    serializer = TodoItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE','PATCH'])
def todo_items_detail(request,pk):
    try:
        todoitem =TodoItem.objects.get(pk=pk)
    except TodoItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=TodoItemSerializer(todoitem)
        return Response(serializer.data)
        

    elif request.method =='PUT':
        serializer=TodoItemSerializer(todoitem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        todoitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PATCH':
        serializer = TodoItemSerializer(todoitem, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    


# @api_view(['GET', 'POST'])
# def todo_items_create(request):
#     if request.method == 'GET':
#         items = TodoItem.objects.all()
#         serializer = TodoItemSerializer(items, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = TodoItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)



# user authentications view


User = get_user_model()

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_objects(self):
        return self.request.user
    


@login_required
def google_login_callback(request):
    user = request.user

    social_accounts = SocialAccount.objects.filter(user=user)
    print("Social Account for user:", social_accounts)

    social_account = social_accounts.first()

    if not social_account:
        print("No social account for user:", user)
        return redirect('http://localhost:3000/login/callback/?error=NoSocialAccount')
    
    token= SocialToken.objects.filter(account=social_account, account__providers='google').first()

    if token:
        print('Google token found:', token.token)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        return redirect(f'http://localhost:3000/login/callback/?access_token={access_token}')
    
    else:
        print('No Google token found for user', user)
        return redirect(f'http://localhost:3000/login/callback/?error=NoGoogleToken')

# validate google token

@csrf_exempt
def validate_google_token(request):
    if request.method== 'POST':
        try:
            data=json.loads(request.body)
            google_access_token= data.get('access_token')
            print(google_access_token)

            if not google_access_token:
                return JsonResponse({'detail':'Access Token is missing'},status=400)
            return JsonResponse({'valid':True})
        except json.JSONDecodeError:
            return JsonResponse({'detail':'invalid HSON.'}, status=400)
    return JsonResponse({'details':'Method not allowed.'},status=405)
