import json
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('WOMqeAx8wH8S-0CX6Nzn3B_4AC8hyqwEz8KbgPgii4jA')
discovery = DiscoveryV1(
    version='2018-12-03',
    authenticator=authenticator)
discovery.set_service_url('https://gateway.watsonplatform.net/discovery/api')

# collections = discovery.list_collections('{environment_id}').get_result()
# # collections = discovery.list_collections('64f857a3-89ce-4970-a3e5-636145c8eb30').get_result()
# # print('list_collections:')
# # print(json.dumps(collections, indent=2),'-------------------------\n\n')

# collection = discovery.get_collection(
#     '{environment_id}', 
#     '{collection_id}').get_result()
# collection = discovery.get_collection(
#     '64f857a3-89ce-4970-a3e5-636145c8eb30', 
#     '67b29f32-9482-4acd-b1ff-897bbb6e2272').get_result()
# print('get_collection:')
# print(json.dumps(collection, indent=2),'-------------------------\n\n')


# DS_TRIALS
query_collection = discovery.query('64f857a3-89ce-4970-a3e5-636145c8eb30', '67b29f32-9482-4acd-b1ff-897bbb6e2272', filter=None, query=None, natural_language_query=None, passages=None, aggregation=None, count=10000, return_=None, offset=None, sort=None, highlight=None, passages_fields=None, passages_count=None, passages_characters=None, deduplicate=None, deduplicate_field=None, similar=None, similar_document_ids=None, similar_fields=None, bias=None, spelling_suggestions=None, x_watson_logging_opt_out=None).get_result()
# DEV
# query_collection = discovery.query('64f857a3-89ce-4970-a3e5-636145c8eb30', 'b3349210-fe02-442f-bd4a-d6c3d14a5584', filter=None, query=None, natural_language_query=None, passages=None, aggregation=None, count=10000, return_=None, offset=None, sort=None, highlight=None, passages_fields=None, passages_count=None, passages_characters=None, deduplicate=None, deduplicate_field=None, similar=None, similar_document_ids=None, similar_fields=None, bias=None, spelling_suggestions=None, x_watson_logging_opt_out=None).get_result()
print('query:')
# print(json.dumps(query_collection, indent=2),'-------------------------\n\n')
number_of_docs = len(query_collection['results'])
print('number of docs= {}'.format(number_of_docs))
# for i in range(number_of_docs):
#     print('name[{}]: {}'.format(i, json.dumps(query_collection['results'][i]['name'])))
#     print('id[{}]: {}'.format(i, json.dumps(query_collection['results'][i]['id'])))

# print(json.dumps(query_collection, indent=2),'-------------------------\n\n')
    