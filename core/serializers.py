from rest_framework.serializers import ModelSerializer
from core.models import MainDB


class UserInputSerializer(ModelSerializer):
    class Meta:
        model=MainDB
        fields=['input', 'style']

class OutputSerializer(ModelSerializer):
    class Meta:
        model=MainDB
        fields=['output']

class MainDBSerializer(ModelSerializer):
    class Meta:
        model=MainDB
        fields='__all__'