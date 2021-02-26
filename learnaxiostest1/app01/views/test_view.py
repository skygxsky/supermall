from django.shortcuts import render,HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from loguru import logger
import json

url = ""

class MultiData(APIView):

    def get(self,request,*args,**kwargs):
        url = 'http://123.207.32.32:8000/home/multidata'
        # url = 'http://123.207.32.32:8000/home/data'
        result = requests.get(url).json()
        logger.debug(result)
        # return HttpResponse(json.dumps(result))
        return Response(result)
class Data(APIView):

    def get(self,request,*args,**kwargs):
        logger.debug(request.query_params)
        url = 'http://152.136.185.210:7878/api/m5/home/data'
        params = request.query_params
        result = requests.get(url,params).json()
        logger.debug(result)

        return Response(result)

class Category(APIView):

    def get(self,request,*args,**kwargs):
        url = 'http://152.136.185.210:7878/api/m5/category'
        result = requests.get(url).json()
        logger.debug(result)
        return Response(result)


