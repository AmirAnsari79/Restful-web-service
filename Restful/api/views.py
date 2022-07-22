from django.shortcuts import render

# Create your views here.


# implement api with json
from django.http import HttpResponse
from .models import Store, Item
import json


def rest_store(request):
    store_list = Store.objects.all()
    store_names = [{'name': store.title} for store in store_list]
    return HttpResponse(json.dumps(store_names), content_type='application/json')  # we can use xml or json


# implement api with django.serializer
from django.http import HttpResponse
from .models import Store, Item
from django.core import serializers


def rest_store_id(request, store_id=None):
    """
    if store_id is None return all of store by xml or json
    if store_id is not None return store
    """
    store_list = Store.objects.all()
    if store_id:
        store_list = store_list.filter(id=store_id)
    if 'type' in request.GET and request.GET['type'] == 'xml':
        serialized_store = serializers.serialize(format='xml', queryset=store_list)
        return HttpResponse(serialized_store, content_type='application/xml')
    else:
        serialized_store = serializers.serialize(format='json', queryset=store_list)
        return HttpResponse(serialized_store, content_type='application/json')
