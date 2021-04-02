from django.conf import settings
from django.db import connections
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models.product import Shops
from ..models.user import Customers
from ..serializers.product import ShopSerializer
from utils.response import AssertionErrorResponse, BadRequestResponse, NotFoundResponse
from utils.utils import checkIfExist

class ShopViews(APIView):
    def post(self, request):
        # try:
            data = request.data
            is_customer_exist = checkIfExist(Customers, id = int(data['customer_id']))
            if not is_customer_exist:
                return AssertionErrorResponse("customer id not found, please check your customer id::404")
            serializer = ShopSerializer(data = data)
            if serializer.is_valid():
                saved = serializer.save()
                is_customer_exist.is_shop_owner = True
                is_customer_exist.save()
                return Response({"status":"success", "message":"data successfully craeted"})

        # except:
        #     return BadRequestResponse()