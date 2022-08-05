from rest_framework import serializers
from .models import *
from .models import CustomUser


# class TestSer(serializers.Serializer):
#     name = serializers.CharField(max_length=250)
#     surname = serializers.CharField(max_length=250)
#     user = CustomUser.user
#     worker_status = CustomUser.worker_status
#     role = CustomUser.role
#     def create(self, validated_data):

class DjangoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = '__all__'


class TaskImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskImage
        fields = '__all__'


class TeamViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
