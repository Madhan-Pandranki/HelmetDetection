# views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, LoginSerializer, FileUploadSerializer,NameURLSerializer
from .models import Frame, NameURL
import os

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(f"username: {serializer.validated_data.username}, password: {serializer.validated_data.password}")
        user = authenticate(username=serializer.validated_data.username, password=serializer.validated_data.password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FileUploadView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            uploaded_file = serializer.save()
            f_path = uploaded_file.file.url 
            current_directory = os.getcwd()
            print(current_directory)
            file_path=current_directory+f_path
            print (file_path)
            command_v = f"cd yolov9 && rm -rf ./runs/detect && python detect.py --source {file_path} --weights '/home/jitu/Projects/Hdetect/backend/hdetect/yolov9/best.pt' --save-crop && cd .. && python ./main.py"
            return_code = os.system(command_v)
            file_path = "/home/jitu/Projects/Hdetect/backend/hdetect/temp.txt"
            line1 = ""
            with open(file_path, 'r') as file:
                line1 = file.readline()
            return Response({'message': 'File processed', 'output': line1}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NameURLView(generics.ListCreateAPIView):
    queryset = NameURL.objects.all()
    serializer_class = NameURLSerializer

class CamDetectView(APIView):
    def get(self, request, pk, format=None):
        name_url = get_object_or_404(NameURL, pk=pk)
        url = name_url.url
        command_v = f"python /home/jitu/Projects/Hdetect/backend/hdetect/yolov9/detect.py --weights /home/jitu/Projects/Hdetect/backend/hdetect/yolov9/best.pt --conf 0.5 --source {url} --device cpu"
        return_code = os.system(command_v)
        return Response({'message': 'Camera detection started', 'return_code': return_code}, status=status.HTTP_200_OK)