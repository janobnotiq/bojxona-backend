from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,models
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework import generics
from .serializers import DeclarationSerializer
from .models import Declaration


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Foydalanuvchini autentifikatsiya qilish
        user = authenticate(username=username, password=password)

        if user is not None:
            # Agar foydalanuvchi mavjud bo'lsa, JWT tokenlar yaratamiz
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            # Agar login xato bo'lsa, javob qaytaramiz
            return Response({'detail': 'Login yoki parol xato.'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()  # Tokenni blacklist qilish
            return Response({'detail': 'Logout muvaffaqiyatli.'}, status=status.HTTP_205_RESET_CONTENT)
        except TokenError as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class DeclarationCreateAPIView(generics.CreateAPIView):
    queryset = Declaration.objects.all()
    serializer_class = DeclarationSerializer

    def perform_create(self,serializer):
        serializer.save(declarant=models.User.objects.filter(id=2).last())