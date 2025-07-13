from django.shortcuts import render, redirect
from .models import Thread
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer 

# @login_required
# def join_chat(request):
#     if request.method == "POST":
#         thread_id = request.POST.get("thread_id")
#         thread, created = Thread.objects.get_or_create(thread_id=thread_id)
#         thread.users.add(request.user)
#         return redirect(f"/chat/{thread_id}/")
#     return render(request, "chatapp/join_chat.html")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def join_thread(request):
    thread_id = request.data.get("thread_id")
    if not thread_id:
        return Response({"error": "Thread ID required"}, status=400)
    thread, created = Thread.objects.get_or_create(thread_id=thread_id)
    thread.users.add(request.user)
    return Response({"message": "Joined thread", "thread_id": thread_id})

# @login_required
# def chat_room(request, thread_id):
#     thread = Thread.objects.get(thread_id=thread_id)
#     if request.user not in thread.users.all():
#         return redirect("join_chat")
#     return render(request, "chatapp/chat_room.html", {"thread_id": thread_id})



@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
