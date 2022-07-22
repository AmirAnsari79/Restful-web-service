from django.shortcuts import render


# implement api with json


def rest_store(request):
    from django.http import HttpResponse
    from .models import Store, Item
    import json

    store_list = Store.objects.all()
    store_names = [{'name': store.title} for store in store_list]
    return HttpResponse(json.dumps(store_names), content_type='application/json')  # we can use xml or json


# implement api with django.serializer

def rest_store_id(request, store_id=None):
    from django.http import HttpResponse
    from .models import Store, Item
    from django.core import serializers
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


# implement by drf and function view
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def rest_store_drf(request):
    from .models import Store
    from rest_framework.response import Response
    from .serial import StoreSerializer
    if request.method == 'GET':
        store = Store.objects.all()
        serializer = StoreSerializer(instance=store, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        pass


# implement view bookserial
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serial import BookSerializer
from rest_framework.status import HTTP_201_CREATED


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(data=request.data, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST' and request.user.is_authenticated:
        serializer = BookSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, id):
    NotImplementedError()


# # implement hyperlink with generic class
# from rest_framework import generics
# from .models import Book
# from .serial import BookSerializer
# class BookList(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDetail(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = "id"


# APIVIEW
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Store
from .serial import StoreSerializer


class StoreList(APIView):
    def get(self, request, format=None):
        store = Store.objects.all()
        serializer = StoreSerializer(instance=store, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        pass

    def put(self):
        pass


# mixin and genericview
from .models import Store
from .serial import StoreSerializer
from rest_framework import mixins, generics


class StoreListMixin(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

