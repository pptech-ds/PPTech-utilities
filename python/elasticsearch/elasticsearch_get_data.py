import requests
import argparse


#getting user inputs 
parser = argparse.ArgumentParser()
parser.add_argument('--index', help='Elasticsearch index name"', type=str)
parser.add_argument('--type', help='Elasticsearch type"', type=str)
parser.add_argument('--keywords_list', help='keywords list to query"', type=str)
args = parser.parse_args()

# es_index = 'discovery_dev' # equivalent to SQL database
# es_type = '_doc' # equivalent to SQL table: mandatory to use _doc for text elements
# keywords_list = 'crêpes'

es_index = args.index
es_type = args.type
keywords_list = args.keywords_list

res = requests.get('https://search-PPTECH1-zrhgle3vemuqzhhs7fudth7cae.eu-west-3.es.amazonaws.com/'+es_index+'/_search?q='+keywords_list)


print(res.status_code)
if res.status_code != 200:
    print('ERROR during GET search')
    exit(1)
else:
    print('element correctly GET search!')

print(res)

res_json = res.json()
print(res_json)

