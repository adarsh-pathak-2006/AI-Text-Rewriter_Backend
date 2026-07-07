from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from core.serializers import UserInputSerializer, OutputSerializer, MainDBSerializer
from core.models import MainDB
from rest_framework.response import Response


class TotalEntriesAPI(APIView):
    def get(self, request):
        data=MainDB.objects.all()
        serial=MainDBSerializer(data, many=True)
        return Response(serial.data)

    def post(self, request):
        serial=UserInputSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response({ 'invalid':'invalid inputs' })
        
class AIRequestAPI(APIView):
    def get(self, request, pk):
        data=get_object_or_404(MainDB, id=pk)
        serial=UserInputSerializer(data)
        return Response(serial)
    
    def put(self, request, pk):
        instance=get_object_or_404(MainDB, id=pk)
        serial=OutputSerializer(instance, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response({ 'invalid':'invalid Input' })
        

class FinalOutputAPI(APIView):
    def get(self, request, pk):
        data=get_object_or_404(MainDB, id=pk)
        serial=MainDBSerializer(data)
        return Response(serial.data)
    
    