from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import os
import time

def enviro(request):
    with open("/code/enviro/enviro.value") as file:
        enviro = file.read()
    data = {"enviro": enviro}
    return JsonResponse(data)
