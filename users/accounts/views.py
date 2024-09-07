from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken # for generating token
from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

from .serializers import UserSerializer
from .models import CustomUser







user = get_user_model() # get CustomUser Model from settings.py file 


class UserLoginAPI(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data) # for creating object in serilazer
        serializer.is_valid(raise_exception=True) # for validation data 
        user = serializer.validated_data['user'] # user= email comming from input  دا عشان نعمل للايمل دا توكن و عشان نجيب ال يوز اللي عامل لوجن

        token, created = Token.objects.get_or_create(user=user) # create or get token if not exist 
        return Response({'token': token.key}, status=status.HTTP_200_OK) # for returning token



        
class UserLogoutAPI(APIView):
    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
        



class ChangePasswordAPI(APIView):
    def put(self,request):
        user = request.user
        data = request.date

        if not user.check_password(data.get('old_password')):
            return Response({'message': 'Old password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)
        
        # update password 
        user.set_password(data.get('new_password'))
        user.save()
        return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)




class ResendActivationCodeAPI(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        try:
            user = user.objects.get(email=email)
        except Exception as e :
            return Response({'error': e})
        
        if user.is_active:
            return Response({"error": 'user account is already activate'}, status=status.HTTP_400_BAD_REQUEST)
        # Activation link in email
        current_site =  get_current_site(request) # get domain
        mail_subject = 'Activate You Account' # subject
        # render email content in html template 
        message = render_to_string('accounts/activation_email.html', {
            'user':user,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.id)),
            'token': default_token_generator.make_token(user),

        })

        to_email = user.email
        send_mail(mail_subject, message, 'mmohamedabdelm@gmail.com', [to_email])
        return Response({'success':'User Created Successfully, Check Your Email To Activate Your Account'}, status=status.HTTP_200_OK)



class ResetPasswordAPI(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email') # عشان اجيب الميل من الفورم
        try:
            user = user.objects.get(email=email)
        except Exception as e :
            return Response({'error': e})
        
        if user.is_active:
            return Response({"error": 'user account is already activate'}, status=status.HTTP_400_BAD_REQUEST)
        # Activation link in email
        current_site =  get_current_site(request) # get domain
        mail_subject = 'Reset Your Password' # subject
        # render email content in html template 
        message = render_to_string('accounts/password_rest_email.html', {
            'user':user,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.id)),
            'token': default_token_generator.make_token(user),

        })

        to_email = user.email
        send_mail(mail_subject, message, 'mmohamedabdelm@gmail.com', [to_email])
        return Response({'success':'User Created Successfully, Check Your Email To Activate Your Account'}, status=status.HTTP_200_OK)



class UserSignupAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save() # create user
            user.is_active = False # prevent user from login until activate
            user.save()

            # Activation link in email
            current_site =  get_current_site(request) # get domain
            mail_subject = 'Activate You Account' # subject
            # render email content in html template 
            message = render_to_string('accounts/activation_email.html', {
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.id)),
                'token': default_token_generator.make_token(user),

            })

            to_email = user.email
            send_mail(mail_subject, message, 'mmohamedabdelm@gmail.com', [to_email])
            return Response({'success':'User Created Successfully, Check Your Email To Activate Your Account'}, status=status.HTTP_201_CREATED)

        return Response({ 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




class ResetPasswordAPI(APIView):
    pass


class UserProfileAPI(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user # for get user now  او كد جبت المستخم الحالي 
        serializer = UserSerializer(user) # for conver data user for json 
        return Response(serializer.data, status=status.HTTP_200_OK) # for return data json and status