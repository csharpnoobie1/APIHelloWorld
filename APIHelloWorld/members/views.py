from django.shortcuts import render
from django.http import JsonResponse
from .models import User  # Zorg ervoor dat je de juiste modelnaam gebruikt
from django.core import serializers

def user_list(request):
    users = User.objects.all()  # Verzamelt alle user objecten uit de database
    data = serializers.serialize('json', users)  # Serialiseert de queryset naar JSON
    return JsonResponse(data, safe=False)  # Retourneert een JsonResponse met de serialized data

