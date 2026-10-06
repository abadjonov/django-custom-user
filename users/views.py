from django.contrib.auth.models import make_password

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterUserSerializer
from .models import User, UserVerificationCode
from .utils import generate_otp


class RegisterView(APIView):
    def post(self, reqeust: Request) -> Response:
        serializer = RegisterUserSerializer(data=reqeust.data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data

            user = User(
                email=validated_data['email'],
                username=validated_data['username'],
                first_name=validated_data.get('first_name', ''),
                last_name=validated_data.get('last_name', ''),
            )
            user.set_password(make_password(validated_data['password']))
            user.save()

            otp = generate_otp()

            uvc = UserVerificationCode(user=user, otp=otp)
            uvc.save()

            return Response({'message': 'email ga kod ketti.'})
