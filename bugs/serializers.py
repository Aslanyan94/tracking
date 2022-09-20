from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers

from bugs.models import Bug, Comment


class BugSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    assigned = serializers.IntegerField(required=False)
    status = serializers.CharField()

    def create(self, validated_data):
        return Bug.objects.create(**validated_data)


class BugsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = ('id', 'title', 'body', 'assigned', 'status')


class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CommentSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    bug = serializers.CharField(help_text="Bug id")

    def create(self, validated_data):
        return Bug.objects.create(**validated_data)
