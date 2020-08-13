from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Members, ActivityPeriods
from .serializer import MemberSerializers, ActivitySerializer
import json


class MemberView(APIView):
    def get(self, request):
        member = Members.objects.all()
        serializer = MemberSerializers(member,many=True)
        data = {"members": serializer.data}
        return HttpResponse(json.dumps(data), content_type='application/json')


class ActivityView(APIView):
    activity = ActivityPeriods.objects.all()
    activity_serializer = ActivitySerializer(activity, many=True)
