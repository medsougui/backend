from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.emailverif import send_verification_email

class VerificationEmailView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')

        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Send the verification email
        code = send_verification_email(email)

        # Optionally, save the code in the database or a cache for later verification
        # For simplicity, we'll assume the code is being returned
        print(code)
        return Response({"code": code}, status=status.HTTP_200_OK)
