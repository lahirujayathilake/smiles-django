from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from . import computational_data_util as comp_util
from . import data_catalog_service as dcs


@csrf_exempt
def create_computational_data_product(request):
    comp_data_product = comp_util.create_computational_product_entity(request)
    data_product = comp_util.map_comp_data_to_data_product(comp_data_product)
    data_catalog_service = dcs.DataCatalogService()
    result_dp = data_catalog_service.create_data_product(data_product)

    return JsonResponse({'data_product_id': result_dp.data_product_id}, status=201)
