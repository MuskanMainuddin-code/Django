from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from kenyanfood import models
from kenyanfood import serializers

# Create your views here.
@api_view(['GET'])
def getFood(request):
	food_obj = models.Food.objects.all().values()
	print("----------------food_obj")
	print(food_obj)
	# serializer_class = serializers.FoodSerializer
	return Response(food_obj)