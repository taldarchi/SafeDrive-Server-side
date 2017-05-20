from rest_framework import serializers
from safedriveapp.models import DataDriver


class DataDriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataDriver
