from django.urls import path
from . import views

urlpatterns = [
    path('rest_store/', views.rest_store, ),
    path('rest_store_id/<int:store_id>/', views.rest_store_id, )
]
