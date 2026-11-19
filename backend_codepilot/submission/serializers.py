from rest_framework import serializers

from submission.models import Submission

class SubmissionSerializer(serializers.ModelSerializer):

    student = serializers.StringRelatedField(read_only=True)

    class Meta:

        model = Submission

        fields = "__all__"

        read_only_fields = ['id','student','assessment','status','started_at','submitted_at','total_marks','evaluation_status']

        