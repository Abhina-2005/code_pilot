from rest_framework import serializers

from user.models import User,StudentProfile

class AdminSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id","username","email","password","phone","role"]

        read_only_fields = ["id","role"]

    def create(self, validated_data):

        return User.objects.create_superuser(**validated_data,role = "admin")

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
   

        model = User

        fields = ["id","username","password","email","phone","role"]
        
        read_only_fields =["id","role"]
        

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)


class StudentProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = StudentProfile

        fields = "__all__"

        read_only_fields = ["id","student","created_at","updated_at"]


