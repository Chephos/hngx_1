from django.shortcuts import render
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework.response import Response

from . import serializers

# Create your views here.


class UserDetails(APIView):
    def get(self, request):
        github_file_url = "https://github.com/Chephos/hngx_1/blob/main/api/views.py"
        github_repo_url = "https://github.com/Chephos/hngx_1"

        data = {
            "slack_name": request.query_params.get("slack_name", "Efosa Charles-Abu"),
            "current_day": timezone.now().strftime("%A"),
            "utc_time": timezone.now(),
            "track": request.query_params.get("track", "backend"),
            "github_file_url": github_file_url,
            "github_repo_url": github_repo_url,
            "status_code": 200,
        }
        serializer = serializers.UserDetails(data)
        return Response(serializer.data)
