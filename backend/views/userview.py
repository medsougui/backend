import base64
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import AuthUser
from ..serializers.userser import AuthUserSerializer

class AuthUserViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer

    @action(detail=False, methods=['post'], url_path='get-by-email-and-password')
    def get_by_email_and_password(self, request):
        """
        Custom endpoint to authenticate a user by email and password.
        """
        email = request.data.get('email')
        password = str(request.data.get('password'))
        
        if not email or not password:
            return Response({"detail": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = AuthUser.objects.get(email=email)
        except AuthUser.DoesNotExist:
            return Response({"detail": "Invalid email or password."}, status=status.HTTP_401_UNAUTHORIZED)

        if password!=user.password:
            return Response({"detail": "Invalid email or password."}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='find-by-email')
    def find_by_email(self, request):
        """
        Check if a user exists by email.
        """
        email = request.data.get('email')

        if not email:
            return Response({"detail": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user with this email exists
        user_exists = AuthUser.objects.filter(email=email).exists()

        return Response(user_exists, status=status.HTTP_200_OK)