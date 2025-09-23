from django.shortcuts import render,HttpResponse
from rest_framework import generics, status
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

@api_view(['GET','PUT','DELETE'])
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
