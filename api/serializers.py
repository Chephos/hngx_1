from rest_framework import serializers


class UserDetails(serializers.Serializer):
    slack_name = serializers.CharField()
    current_day = serializers.CharField()
    utc_time = serializers.DateTimeField()
    track = serializers.CharField()
    github_file_url = serializers.URLField()
    github_repo_url = serializers.URLField()
    status_code = serializers.IntegerField()