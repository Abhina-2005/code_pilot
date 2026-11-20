from rest_framework import serializers

from submission.models import Submission

class SubmissionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Submission

        fields = "__all__"

        read_only_fields = ['id','student','assessment','started_at','created_at','updated_at']

       