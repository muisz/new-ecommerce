from django.conf import settings
from django.db import connections
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models.product import Shops
from ..models.user import Customers
from ..serializers.product import ShopSerializer
from ..serializers.user import CustomerSerializer
from utils.response import AssertionErrorResponse, BadRequestResponse, NotFoundResponse
from utils.utils import checkIfExist
from utils.encryption import generate_password, verify_password

class CustomerView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = CustomerSerializer(data = data)
            if serializer.is_valid():
                saved = serializer.save()
                password = generate_password(saved.password)
                saved.password = password
                saved.save()
                return Response({"status":"success", "message":"data successfully craeted"})
            else:
                raise
            
        except AssertionError as error:
            print(str(error))
            return Response({"status":"error", "message":str(error)})

        except:
            return BadRequestResponse()