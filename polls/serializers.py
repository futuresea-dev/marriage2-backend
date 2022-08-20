from rest_framework import serializers
from .models import *


class inviteMarried_requestSerializer(serializers.ModelSerializer):
    class Meta:
        model = inviteMarried_request
        fields = '__all__'