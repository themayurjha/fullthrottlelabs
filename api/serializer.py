from rest_framework import serializers
from .models import Members, ActivityPeriods

'''
Serializing models and selecting fields to show
field values in JSON response
'''


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriods
        fields = [
            "start_time",
            "end_time",
        ]



class MemberSerializers(serializers.ModelSerializer):
    activity_periods = ActivitySerializer(many=True)
    class Meta:
        model = Members
        fields = [
            "id",
            "real_name",
            "tz",
            "activity_periods",
        ]