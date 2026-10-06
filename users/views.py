from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


class RegisterView(APIView):
    def post(self, reqeust: Request) -> Response:
        pass

