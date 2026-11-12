from rest_framework import serializers
from answer.models import Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields="__all__"
        read_only_fields=["id","submission","question","awarded_marks","feedback"]