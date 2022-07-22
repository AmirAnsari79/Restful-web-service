from django.urls import path
from . import views

urlpatterns = [
    path('rest_store/', views.rest_store, ),
    path('rest_store_id/<int:store_id>/', views.rest_store_id, ),
    path('rest_store_drf', views.rest_store_drf, ),
    # hyperlink 🦷
    # path('book/', views.BookList.as_view(), ),
    # path('book/<int:id>', views.BookDetail.as_view(), ),
    path('books/', views.book_list),
    path('books/<int:id>', views.book_detail)

]
