from rest_framework import serializers
from statistical_counters.models import Statistics


class StatDetailsSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateField()

    class Meta:
        model = Statistics
        fields = ['id', 'timestamp', 'views', 'clicks', 'cost_of_click']


class StatQuerySerializer(serializers.ModelSerializer):
    timestamp = serializers.DateField()
    views = serializers.IntegerField()
    clicks = serializers.IntegerField()
    cost_of_click = serializers.FloatField()
    cpc = serializers.ReadOnlyField()
    cpm = serializers.ReadOnlyField()

    class Meta:
        model = Statistics
        fields = ['id', 'timestamp', 'views', 'clicks', 'cost_of_click', 'cpc', 'cpm']