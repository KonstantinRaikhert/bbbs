from datetime import datetime

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from common.models import City, Meeting
from users.models import Profile


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class MyCitySerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "id", "city"
        lookup_field = "city"


class MeetingSerializer(ModelSerializer):
    name = serializers.CharField(read_only=True, max_length=100)
    place = serializers.CharField(max_length=50, min_length=2)
    description = serializers.CharField(max_length=5000, min_length=2)
    date = serializers.DateField()

    def validate(self, data):
        if data["date"] > datetime.now().date():
            raise serializers.ValidationError(
                "date can not be more than today"
            )
        return data

    class Meta:
        model = Meeting
        fields = "__all__"
        read_only_fields = ["user"]


class MeetingMessageSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)
