from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from core.serializers import UserInputSerializer, MainDBSerializer
from core.models import MainDB
from rest_framework.response import Response
from services.output import rewrite_text


class TotalEntriesAPI(APIView):
    def get(self, request):
        data=MainDB.objects.all()
        serial=MainDBSerializer(data, many=True)
        return Response(serial.data)

    def post(self, request):
        serial=UserInputSerializer(data=request.data)
        if serial.is_valid(raise_exception=True):
            text=serial.validated_data['input']
            style=serial.validated_data['style']
            
            output=rewrite_text(text=text, style=style)
            obj=MainDB.objects.create(input=text, style=style, output=output)
            serialized=MainDBSerializer(obj)
            return Response(serialized.data)
        else:
            return Response({ 'invalid':'invalid inputs' })

class FinalOutputAPI(APIView):
    def get(self, request, pk):
        data=get_object_or_404(MainDB, id=pk)
        serial=MainDBSerializer(data)
        return Response(serial.data)
    
