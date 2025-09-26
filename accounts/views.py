from django.shortcuts import render

# Create your views here.


 # GoogleLogin view that will be using dj-rest-auth's components inside
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.GOOGLE_OAUTH_CALLBACK_URL
    client_class = OAuth2Client


 # GoogleLogin view that will be using dj-rest-auth's components inside
from urllib.parse import urljoin

import requests
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView



# class GoogleLoginCallback(APIView):
#     def get(self, request, *args, **kwargs):
#         """
#         If you are building a fullstack application (eq. with React app next to Django)
#         you can place this endpoint in your frontend application to receive
#         the JWT tokens there - and store them in the state
#         """

#         code = request.GET.get("code")

#         if code is None:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
        
#         # Remember to replace the localhost:8000 with the actual domain name before deployment
#         token_endpoint_url = urljoin("http://localhost:8000", reverse("google_login"))
#         response = requests.post(url=token_endpoint_url, data={"code": code})

#         return Response(response.json(), status=status.HTTP_200_OK)
    
#fix for JSONDecodeError at /api/v1/auth/google/callback/


class GoogleLoginCallback(APIView):
    def get(self, request, *args, **kwargs):
        code = request.GET.get("code")
        if not code:
            return Response({"error": "No code provided"}, status=400)

        token_url = "https://oauth2.googleapis.com/token"
        data = {
            "code": code,
            "client_id": settings.GOOGLE_OAUTH_CLIENT_ID,
            "client_secret": settings.GOOGLE_OAUTH_CLIENT_SECRET,
            "redirect_uri": settings.GOOGLE_OAUTH_CALLBACK_URL,
            "grant_type": "authorization_code",
        }

        response = requests.post(token_url, data=data)
        print("Google response:", response.text)  # Debug: see actual Google response

        if response.status_code != 200:
            return Response({"error": response.text}, status=response.status_code)

        tokens = response.json()
        return Response(tokens, status=200)



#a simple login page.

from django.conf import settings
from django.shortcuts import render
from django.views import View

...

class LoginPage(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "pages/login.html",
            {
                "google_callback_uri": settings.GOOGLE_OAUTH_CALLBACK_URL,
                "google_client_id": settings.GOOGLE_OAUTH_CLIENT_ID,
            },
        )