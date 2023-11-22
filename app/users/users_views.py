from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models.users import Users
from .serializers import UserSerializer

class UserView(APIView):
    queryset = Users.objects.all()
    print(queryset)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        qs = Users.objects.all()
        serializer = UserSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'result':True})