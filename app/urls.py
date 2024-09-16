from django.urls import path
from .views import LoginAPIView, LogoutAPIView, DeclarationCreateAPIView

urlpatterns = [
    #authentication
    path("login/",LoginAPIView.as_view(),name="login"),
    path("logout/",LogoutAPIView.as_view(),name="logout"),

    #declaration
    path("create-declaration/",DeclarationCreateAPIView.as_view(),name="create-declaration"),
]
