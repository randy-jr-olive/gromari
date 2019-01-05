from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import os
import time

def coretemp(request):
    with open("coretemp.value”) as file:
        temp = file.read()
do something with data
    data = {"temp": temp.replace("temp=","")}
    return JsonResponse(data)
