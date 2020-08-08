from rest_framework import generics
from rest_framework.views import APIView
from rest_api.models import (Category, Activity)
from rest_api.serializers import (ActivitySerializers, CategorySerializers)


class CategoryListAPIView(generics.ListAPIView):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


from rest_framework.response import Response
# from rest_framework.status import HTTP_200_OK
from rest_framework import status

class MainListAPIView(APIView):
    def get(self, request, format=None):

        data = Category.objects.all()
        category_ser = CategorySerializers(data, many=True)
        members = []

        for record in category_ser.data:
            _id = record['id']
            real_name = record['real_name']
            tz = record['tz']
            activity_periods = record['activity_periods']

            members.append({"id":_id, "real_name":real_name, "tz":tz, "activity_periods":activity_periods})
        
        return Response({	"ok": "true","members":members}, status=status.HTTP_200_OK)