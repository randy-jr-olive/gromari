from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import os
import time

def coretemp(request):
    temp = os.popen("vcgencmd measure_temp").readline()
    data = {"temp": temp.replace("temp=","")}
    return JsonResponse(data)
