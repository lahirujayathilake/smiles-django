from django.urls import path
from . import views

urlpatterns = [
    path('create/computational-dp', views.create_computational_data_product, name="create-computational-data-product"),
]
