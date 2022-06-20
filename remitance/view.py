# core/restconf/djoser/views.py
from django.http import JsonResponse
from django.views import View

import requests
from social_core.backends.facebook import FacebookOAuth2


class CustomFacebookOAuth2(FacebookOAuth2):
    REDIRECT_STATE = False


class RedirectSocial(View):

    def get(self, request, *args, **kwargs):
        code, state = str(request.GET['code']), str(request.GET['state'])
        json_obj = {'code': code, 'state': state}
        print(json_obj)
        Headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            'code': code,
            "state": state
        }
        response = requests.post(
            'https://django-facebook-production.up.railway.app/api/auth/social/o/facebook/', headers=Headers, json=data)

        return JsonResponse(response.json())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
