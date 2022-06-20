# core/restconf/djoser/views.py
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from social_core.backends.facebook import FacebookOAuth2

from rest_framework.views import APIView


class CustomFacebookOAuth2(FacebookOAuth2):
    REDIRECT_STATE = False


class RedirectSocial(View):

    def get(self, request, *args, **kwargs):
        code, state = str(request.GET['code']), str(request.GET['state'])
        json_obj = {'code': code, 'state': state}
        print(json_obj)
        # Headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        # data = {
        #     'code': code,
        #     "state": state
        # }
        # response = requests.post(
        #     'https://django-facebook-production.up.railway.app/api/auth/social/o/facebook/', headers=Headers, json=data)

        return JsonResponse(json_obj)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class GetUsers(View):
    def get(self, request, *args, **kwargs):
        super = User.objects.create_superuser(
            username='yareds', email="mem@mmm.com", password='!@34QWer')
        return Response({'succes': super})


class ExampleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        print(request.user.email)
        content = {
            'user': request.user,
            'email': request.user.email,

        }
        return Response(content)
