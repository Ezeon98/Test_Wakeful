from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_data = serializer.data
        response_data['status'] = 'success'
        response_data['message'] = 'User created successfully'
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)