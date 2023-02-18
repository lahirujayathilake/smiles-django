import json

import grpc
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import data_catalog_pb2
import data_catalog_pb2_grpc
from data_product.models import ComputationalDataProduct


@csrf_exempt
def create_computational_data_product(request):
    # Get data from request body
    data = json.loads(request.body)
    comp_data_product = ComputationalDataProduct(data_product_id=data.get('data_product_id'), name=data.get('name'),
                                                 mw=87.0)
    comp_data_product.metadata = json.dumps({"mw": comp_data_product.mw, "absorb": 834})

    result_dp = create_data_product(comp_data_product)
    return JsonResponse({'data_product_id': result_dp.data_product_id}, status=201)


def create_data_product(smiles_data_product):
    # Common data assignments for Computational, Experimental, and Literature Data Products
    data_catalog_product = data_catalog_pb2.DataProduct()
    data_catalog_product.data_product_id = smiles_data_product.data_product_id
    data_catalog_product.parent_data_product_id = smiles_data_product.parent_data_product_id
    data_catalog_product.metadata = smiles_data_product.metadata

    # Connect to the gRPC service (DataCatalogAPI gRPC Server)
    channel = grpc.insecure_channel('localhost:6565')
    stub = data_catalog_pb2_grpc.DataCatalogAPIServiceStub(channel)

    # Call Data Catalog API to create DP
    create_request = data_catalog_pb2.DataProductCreateRequest()
    create_request.data_product.CopyFrom(data_catalog_product)
    create_response = stub.createDataProduct(create_request)

    return create_response.data_product
