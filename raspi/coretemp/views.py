from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import os
import time

def coretemp(request):
    with open("/code/coretemp/coretemp.value") as file:
        temp = file.read()
    data = {"temp": temp.replace("temp=","")}
    return JsonResponse(data)
