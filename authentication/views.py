from django.shortcuts import render

from .serializers import RegistrationSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError
from rest_framework.response import Response

from django.contrib.auth import logout
from rest_framework.decorators import api_view, permission_classes
from django.db import IntegrityError
from django.contrib.auth import get_user_model, login
from django.contrib.auth.hashers import check_password, make_password
import json


User = get_user_model()

#Class based view to register user
@api_view(["POST"])
@permission_classes([AllowAny])
def Register_Users(request):
    try:
        data = {}
        serializer = RegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.validated_data['password']= make_password(serializer.validated_data['password'])
            serializer.validated_data['username']=serializer.validated_data['email']
            account = serializer.save()
            account.is_active = True
            account.save()
            token = Token.objects.get_or_create(user=account)[0].key
            data["message"] = "user registered successfully"
            data["email"] = account.email
            data["token"] = token

        else:
            data = serializer.errors


        return Response({"data": data, "status": 200})
    except IntegrityError as e:
        account=User.objects.filter(email='').first()
        # account.delete()
        return Response({"message": f'{str(e)}', "status": 400})

    except KeyError as e:
        return Response({"message": f'Field {str(e)} missing', "status": 400})

@api_view(["POST"])
@permission_classes([AllowAny])
def Login_User(request):

        data = {}
        reqBody = json.loads(request.body)
        email1 = reqBody['email']
        password = reqBody['password']
        try:

            Account = User.objects.get(email=email1)
        except BaseException as e:
            # print()
            return Response({"message": f'{str(e)}', "status": 400})

        token = Token.objects.get_or_create(user=Account)[0].key
        if not check_password(password, Account.password):
            return Response({"message": "Incorrect Login credentials", "status": 401})

        if Account:
            if Account.is_active:
                print(request.user)
                login(request, Account)
                data["message"] = "user logged in"
                data["email_address"] = Account.email

                Res = {"data": data, "token": token, "status": 200}

                return Response(Res)

            else:
                return Response({"status":400, "message":'Account not active'})

        else:
            return Response({"status":400, "message":'Account doesnt exist'})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def User_logout(request):

    request.user.auth_token.delete()

    logout(request)

    return Response('User Logged out successfully')