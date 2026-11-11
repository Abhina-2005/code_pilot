
from assessment.models import Assessment
from rest_framework import serializers


class AssessmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assessment

        fields = '__all__'

        read_only_fields = [
            'id',
            'creator',
            'created_at',
            'updated_at'
            
        ]

