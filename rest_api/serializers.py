from rest_framework import serializers
from .models import (Category, Activity)



class ActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            "start_time", "end_time"
        ]


class CategorySerializers(serializers.ModelSerializer):
    activity_periods = ActivitySerializers(many=True)
    class Meta:
        model = Category
        fields = [
            "id", "real_name", "tz", "activity_periods"
        ]
