from rest_framework import serializers

class UserRegistrationSerializer(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    role = serializers.CharField()
