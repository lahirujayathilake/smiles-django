# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_catalog.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x64\x61ta_catalog.proto\"A\n\x08UserInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x16\n\ttenant_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0c\n\n_tenant_id\"C\n\tGroupInfo\x12\x10\n\x08group_id\x18\x01 \x01(\t\x12\x16\n\ttenant_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0c\n\n_tenant_id\"\xb2\x01\n\x0b\x44\x61taProduct\x12\x17\n\x0f\x64\x61ta_product_id\x18\x01 \x01(\t\x12#\n\x16parent_data_product_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x15\n\x08metadata\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x10metadata_schemas\x18\x05 \x03(\tB\x19\n\x17_parent_data_product_idB\x0b\n\t_metadata\"%\n\x0eMetadataSchema\x12\x13\n\x0bschema_name\x18\x01 \x01(\t\"v\n\x13MetadataSchemaField\x12\x13\n\x0bschema_name\x18\x01 \x01(\t\x12\x12\n\nfield_name\x18\x02 \x01(\t\x12\x11\n\tjson_path\x18\x03 \x01(\t\x12#\n\nvalue_type\x18\x04 \x01(\x0e\x32\x0f.FieldValueType\">\n\x18\x44\x61taProductCreateRequest\x12\"\n\x0c\x64\x61ta_product\x18\x01 \x01(\x0b\x32\x0c.DataProduct\"?\n\x19\x44\x61taProductCreateResponse\x12\"\n\x0c\x64\x61ta_product\x18\x01 \x01(\x0b\x32\x0c.DataProduct\">\n\x18\x44\x61taProductUpdateRequest\x12\"\n\x0c\x64\x61ta_product\x18\x01 \x01(\x0b\x32\x0c.DataProduct\"?\n\x19\x44\x61taProductUpdateResponse\x12\"\n\x0c\x64\x61ta_product\x18\x01 \x01(\x0b\x32\x0c.DataProduct\"0\n\x15\x44\x61taProductGetRequest\x12\x17\n\x0f\x64\x61ta_product_id\x18\x01 \x01(\t\"<\n\x16\x44\x61taProductGetResponse\x12\"\n\x0c\x64\x61ta_product\x18\x01 \x01(\x0b\x32\x0c.DataProduct\"3\n\x18\x44\x61taProductDeleteRequest\x12\x17\n\x0f\x64\x61ta_product_id\x18\x01 \x01(\t\"\x1b\n\x19\x44\x61taProductDeleteResponse\"M\n\x18MetadataSchemaGetRequest\x12\x1c\n\tuser_info\x18\x01 \x01(\x0b\x32\t.UserInfo\x12\x13\n\x0bschema_name\x18\x02 \x01(\t\"E\n\x19MetadataSchemaGetResponse\x12(\n\x0fmetadata_schema\x18\x01 \x01(\x0b\x32\x0f.MetadataSchema\"e\n\x1bMetadataSchemaCreateRequest\x12\x1c\n\tuser_info\x18\x01 \x01(\x0b\x32\t.UserInfo\x12(\n\x0fmetadata_schema\x18\x02 \x01(\x0b\x32\x0f.MetadataSchema\"H\n\x1cMetadataSchemaCreateResponse\x12(\n\x0fmetadata_schema\x18\x01 \x01(\x0b\x32\x0f.MetadataSchema\"e\n\x1bMetadataSchemaDeleteRequest\x12\x1c\n\tuser_info\x18\x01 \x01(\x0b\x32\t.UserInfo\x12(\n\x0fmetadata_schema\x18\x02 \x01(\x0b\x32\x0f.MetadataSchema\"\x1e\n\x1cMetadataSchemaDeleteResponse\"f\n\x1dMetadataSchemaFieldGetRequest\x12\x1c\n\tuser_info\x18\x01 \x01(\x0b\x32\t.UserInfo\x12\x13\n\x0bschema_name\x18\x02 \x01(\t\x12\x12\n\nfield_name\x18\x03 \x01(\t\"U\n\x1eMetadataSchemaFieldGetResponse\x12\x33\n\x15metadata_schema_field\x18\x01 \x01(\x0b\x32\x14.MetadataSchemaField\"u\n MetadataSchemaFieldCreateRequest\x12\x1c\n\tuser_info\x18\x01 \x01(\x0b\x32\t.UserInfo\x12\x33\n\x15metadata_schema_field\x18\x02 \x01(\x0b\x32\x14.MetadataSchemaField\"X\n!MetadataSchemaFieldCreateResponse\x12\x33\n\x15metadata_schema_field\x18\x01 \x01(\x0b\x32\x14.MetadataSchemaField\"u\n MetadataSchemaFieldUpdateRequest\x12\x1c\n\tuser_info\x18\x01 \x01(\x0b\x32\t.UserInfo\x12\x33\n\x15metadata_schema_field\x18\x02 \x01(\x0b\x32\x14.MetadataSchemaField\"X\n!MetadataSchemaFieldUpdateResponse\x12\x33\n\x15metadata_schema_field\x18\x01 \x01(\x0b\x32\x14.MetadataSchemaField\"u\n MetadataSchemaFieldDeleteRequest\x12\x1c\n\tuser_info\x18\x01 \x01(\x0b\x32\t.UserInfo\x12\x33\n\x15metadata_schema_field\x18\x02 \x01(\x0b\x32\x14.MetadataSchemaField\"#\n!MetadataSchemaFieldDeleteResponse\"S\n\x1eMetadataSchemaFieldListRequest\x12\x1c\n\tuser_info\x18\x01 \x01(\x0b\x32\t.UserInfo\x12\x13\n\x0bschema_name\x18\x02 \x01(\t\"W\n\x1fMetadataSchemaFieldListResponse\x12\x34\n\x16metadata_schema_fields\x18\x01 \x03(\x0b\x32\x14.MetadataSchemaField\"s\n%DataProductAddToMetadataSchemaRequest\x12\x1c\n\tuser_info\x18\x01 \x01(\x0b\x32\t.UserInfo\x12\x17\n\x0f\x64\x61ta_product_id\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\"L\n&DataProductAddToMetadataSchemaResponse\x12\"\n\x0c\x64\x61ta_product\x18\x01 \x01(\x0b\x32\x0c.DataProduct\"x\n*DataProductRemoveFromMetadataSchemaRequest\x12\x1c\n\tuser_info\x18\x01 \x01(\x0b\x32\t.UserInfo\x12\x17\n\x0f\x64\x61ta_product_id\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t\"Q\n+DataProductRemoveFromMetadataSchemaResponse\x12\"\n\x0c\x64\x61ta_product\x18\x01 \x01(\x0b\x32\x0c.DataProduct*g\n\nPermission\x12\t\n\x05OWNER\x10\x00\x12\x08\n\x04READ\x10\x01\x12\x11\n\rREAD_METADATA\x10\x02\x12\t\n\x05WRITE\x10\x03\x12\x12\n\x0eWRITE_METADATA\x10\x04\x12\x12\n\x0eMANAGE_SHARING\x10\x05*Q\n\x0e\x46ieldValueType\x12\n\n\x06STRING\x10\x00\x12\x0b\n\x07INTEGER\x10\x01\x12\t\n\x05\x46LOAT\x10\x02\x12\x0b\n\x07\x42OOLEAN\x10\x03\x12\x0e\n\nDATESTRING\x10\x04\x32\xab\n\n\x15\x44\x61taCatalogAPIService\x12L\n\x11\x63reateDataProduct\x12\x19.DataProductCreateRequest\x1a\x1a.DataProductCreateResponse\"\x00\x12L\n\x11updateDataProduct\x12\x19.DataProductUpdateRequest\x1a\x1a.DataProductUpdateResponse\"\x00\x12\x43\n\x0egetDataProduct\x12\x16.DataProductGetRequest\x1a\x17.DataProductGetResponse\"\x00\x12L\n\x11\x64\x65leteDataProduct\x12\x19.DataProductDeleteRequest\x1a\x1a.DataProductDeleteResponse\"\x00\x12L\n\x11getMetadataSchema\x12\x19.MetadataSchemaGetRequest\x1a\x1a.MetadataSchemaGetResponse\"\x00\x12U\n\x14\x63reateMetadataSchema\x12\x1c.MetadataSchemaCreateRequest\x1a\x1d.MetadataSchemaCreateResponse\"\x00\x12U\n\x14\x64\x65leteMetadataSchema\x12\x1c.MetadataSchemaDeleteRequest\x1a\x1d.MetadataSchemaDeleteResponse\"\x00\x12[\n\x16getMetadataSchemaField\x12\x1e.MetadataSchemaFieldGetRequest\x1a\x1f.MetadataSchemaFieldGetResponse\"\x00\x12\x64\n\x19\x63reateMetadataSchemaField\x12!.MetadataSchemaFieldCreateRequest\x1a\".MetadataSchemaFieldCreateResponse\"\x00\x12\x64\n\x19updateMetadataSchemaField\x12!.MetadataSchemaFieldUpdateRequest\x1a\".MetadataSchemaFieldUpdateResponse\"\x00\x12\x64\n\x19\x64\x65leteMetadataSchemaField\x12!.MetadataSchemaFieldDeleteRequest\x1a\".MetadataSchemaFieldDeleteResponse\"\x00\x12^\n\x17getMetadataSchemaFields\x12\x1f.MetadataSchemaFieldListRequest\x1a .MetadataSchemaFieldListResponse\"\x00\x12s\n\x1e\x61\x64\x64\x44\x61taProductToMetadataSchema\x12&.DataProductAddToMetadataSchemaRequest\x1a\'.DataProductAddToMetadataSchemaResponse\"\x00\x12\x82\x01\n#removeDataProductFromMetadataSchema\x12+.DataProductRemoveFromMetadataSchemaRequest\x1a,.DataProductRemoveFromMetadataSchemaResponse\"\x00\x42\'\n#org.apache.airavata.datacatalog.apiP\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'data_catalog_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#org.apache.airavata.datacatalog.apiP\001'
  _PERMISSION._serialized_start=2751
  _PERMISSION._serialized_end=2854
  _FIELDVALUETYPE._serialized_start=2856
  _FIELDVALUETYPE._serialized_end=2937
  _USERINFO._serialized_start=22
  _USERINFO._serialized_end=87
  _GROUPINFO._serialized_start=89
  _GROUPINFO._serialized_end=156
  _DATAPRODUCT._serialized_start=159
  _DATAPRODUCT._serialized_end=337
  _METADATASCHEMA._serialized_start=339
  _METADATASCHEMA._serialized_end=376
  _METADATASCHEMAFIELD._serialized_start=378
  _METADATASCHEMAFIELD._serialized_end=496
  _DATAPRODUCTCREATEREQUEST._serialized_start=498
  _DATAPRODUCTCREATEREQUEST._serialized_end=560
  _DATAPRODUCTCREATERESPONSE._serialized_start=562
  _DATAPRODUCTCREATERESPONSE._serialized_end=625
  _DATAPRODUCTUPDATEREQUEST._serialized_start=627
  _DATAPRODUCTUPDATEREQUEST._serialized_end=689
  _DATAPRODUCTUPDATERESPONSE._serialized_start=691
  _DATAPRODUCTUPDATERESPONSE._serialized_end=754
  _DATAPRODUCTGETREQUEST._serialized_start=756
  _DATAPRODUCTGETREQUEST._serialized_end=804
  _DATAPRODUCTGETRESPONSE._serialized_start=806
  _DATAPRODUCTGETRESPONSE._serialized_end=866
  _DATAPRODUCTDELETEREQUEST._serialized_start=868
  _DATAPRODUCTDELETEREQUEST._serialized_end=919
  _DATAPRODUCTDELETERESPONSE._serialized_start=921
  _DATAPRODUCTDELETERESPONSE._serialized_end=948
  _METADATASCHEMAGETREQUEST._serialized_start=950
  _METADATASCHEMAGETREQUEST._serialized_end=1027
  _METADATASCHEMAGETRESPONSE._serialized_start=1029
  _METADATASCHEMAGETRESPONSE._serialized_end=1098
  _METADATASCHEMACREATEREQUEST._serialized_start=1100
  _METADATASCHEMACREATEREQUEST._serialized_end=1201
  _METADATASCHEMACREATERESPONSE._serialized_start=1203
  _METADATASCHEMACREATERESPONSE._serialized_end=1275
  _METADATASCHEMADELETEREQUEST._serialized_start=1277
  _METADATASCHEMADELETEREQUEST._serialized_end=1378
  _METADATASCHEMADELETERESPONSE._serialized_start=1380
  _METADATASCHEMADELETERESPONSE._serialized_end=1410
  _METADATASCHEMAFIELDGETREQUEST._serialized_start=1412
  _METADATASCHEMAFIELDGETREQUEST._serialized_end=1514
  _METADATASCHEMAFIELDGETRESPONSE._serialized_start=1516
  _METADATASCHEMAFIELDGETRESPONSE._serialized_end=1601
  _METADATASCHEMAFIELDCREATEREQUEST._serialized_start=1603
  _METADATASCHEMAFIELDCREATEREQUEST._serialized_end=1720
  _METADATASCHEMAFIELDCREATERESPONSE._serialized_start=1722
  _METADATASCHEMAFIELDCREATERESPONSE._serialized_end=1810
  _METADATASCHEMAFIELDUPDATEREQUEST._serialized_start=1812
  _METADATASCHEMAFIELDUPDATEREQUEST._serialized_end=1929
  _METADATASCHEMAFIELDUPDATERESPONSE._serialized_start=1931
  _METADATASCHEMAFIELDUPDATERESPONSE._serialized_end=2019
  _METADATASCHEMAFIELDDELETEREQUEST._serialized_start=2021
  _METADATASCHEMAFIELDDELETEREQUEST._serialized_end=2138
  _METADATASCHEMAFIELDDELETERESPONSE._serialized_start=2140
  _METADATASCHEMAFIELDDELETERESPONSE._serialized_end=2175
  _METADATASCHEMAFIELDLISTREQUEST._serialized_start=2177
  _METADATASCHEMAFIELDLISTREQUEST._serialized_end=2260
  _METADATASCHEMAFIELDLISTRESPONSE._serialized_start=2262
  _METADATASCHEMAFIELDLISTRESPONSE._serialized_end=2349
  _DATAPRODUCTADDTOMETADATASCHEMAREQUEST._serialized_start=2351
  _DATAPRODUCTADDTOMETADATASCHEMAREQUEST._serialized_end=2466
  _DATAPRODUCTADDTOMETADATASCHEMARESPONSE._serialized_start=2468
  _DATAPRODUCTADDTOMETADATASCHEMARESPONSE._serialized_end=2544
  _DATAPRODUCTREMOVEFROMMETADATASCHEMAREQUEST._serialized_start=2546
  _DATAPRODUCTREMOVEFROMMETADATASCHEMAREQUEST._serialized_end=2666
  _DATAPRODUCTREMOVEFROMMETADATASCHEMARESPONSE._serialized_start=2668
  _DATAPRODUCTREMOVEFROMMETADATASCHEMARESPONSE._serialized_end=2749
  _DATACATALOGAPISERVICE._serialized_start=2940
  _DATACATALOGAPISERVICE._serialized_end=4263
# @@protoc_insertion_point(module_scope)
