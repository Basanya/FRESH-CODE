from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Apii.models import Product
from .serializer import ProductSerializer

# Create your views here.

@api_view(["GET"])
def api_home(request):
    if request.method == "GET":
        my_Product = Product.objects.all()
        serializer = ProductSerializer(my_Product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def api_detail(request, slug):
    if request.method == "GET":
        my_product = Product.objects.get(slug=slug)
        serializer = ProductSerializer(my_product, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def api_create(request):
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(["POST"])
def api_update(request, slug):
    if request.method == "POST":
        my_product = Product.objects.get(slug=slug)
        serializer = ProductSerializer(instance=my_product, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(["DELETE"])
def api_delete(request, slug):
    if request.method == "DELETE":
        my_product = Product.objects.get(slug=slug)
        my_product.delete()

        return Response ('item successfully deleted')



