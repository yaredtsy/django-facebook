# core/restconf/djoser/views.py
from django.http import JsonResponse
from django.views import View


from social_core.backends.facebook import FacebookOAuth2


class CustomFacebookOAuth2(FacebookOAuth2):
    REDIRECT_STATE = False

class RedirectSocial(View):

    def get(self, request, *args, **kwargs):
        code, state = str(request.GET['code']), str(request.GET['state'])
        json_obj = {'code': code, 'state': state}
        print(json_obj)
        return JsonResponse(json_obj)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
