from django.db import models
import json


class DataCatalogProduct(models.Model):
    managed = False
    data_product_id = models.CharField(max_length=255)
    parent_data_product_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    metadata = models.TextField()

    def set_json_data(self, data):
        self.metadata = json.dumps(data)

    def get_json_data(self):
        return json.loads(self.metadata)


class MetadataSchemaField(models.Model):
    managed = False
    schema_name = models.CharField(max_length=255)
    field_name = models.CharField(max_length=255)
    json_path = models.CharField(max_length=255)

    # FIELD_VALUE_TYPES = [(e.value, e.name) for e in data_catalog_pb2.FieldValueType()]
    # value_type = models.CharField(choices=FIELD_VALUE_TYPES, max_length=20)


class MetadataSchema(models.Model):
    managed = False
    schema_name = models.CharField(max_length=255)


class ComputationalDataProduct(DataCatalogProduct):
    mw = models.CharField(max_length=255)
