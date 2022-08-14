from django.db import models
from rest_framework import serializers
from backend.models import *

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDate
        fields = '__all__'

class EventVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventVote
        fields = '__all__'