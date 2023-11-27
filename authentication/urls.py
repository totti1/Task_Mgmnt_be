from django.urls import path
# from authentication.views import MyObtainTokenPairView
# from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token
from .views import Register_Users, Login_User, User_logout


urlpatterns = [
    path('login/', Login_User, name='login_user'),
    path('register/',Register_Users, name='register_user'),
    path('logout/',Register_Users, name='logout_user'),
]