from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

def index(request):
    return render(request,'index.html')


@api_view(['GET'])
def bookList(request):
    tasks = Book.objects.all()
    serializer = BookSerializer(tasks, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def bookDetail(request,pk):
    task = Book.objects.get(id=pk)
    serializer = BookSerializer(task, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def bookCreate(request):
    serializer = BookSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def bookUpdate(request,pk):
    task = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=task,data= request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def bookDelete(request,pk):
    task = Book.objects.get(id=pk) 
    task.delete()

    return Response("Item deleted successfully")

