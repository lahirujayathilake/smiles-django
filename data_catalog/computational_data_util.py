import data_catalog_pb2 as pb2
import json

from data_catalog.models import ComputationalDataProduct


def create_computational_product_entity(request):
    # Get data from request body
    # data = json.loads(request.body)
    # comp_data_product = ComputationalDataProduct(data_product_id=data.get('data_product_id'), name=data.get('name'),
    #                                              mw=87.0)
    #
    comp_data_product = ComputationalDataProduct(data_product_id='data_product_id0349348', name='namedf34343', mw=87.0)
    comp_data_product.metadata = json.dumps({"mw": comp_data_product.mw, "absorb": 834})

    return comp_data_product


def map_comp_data_to_data_product(smiles_data_product: ComputationalDataProduct) -> pb2.DataProduct:
    data_catalog_product = pb2.DataProduct()
    data_catalog_product.data_product_id = smiles_data_product.data_product_id
    data_catalog_product.parent_data_product_id = smiles_data_product.parent_data_product_id
    data_catalog_product.metadata = smiles_data_product.metadata

    return data_catalog_product
