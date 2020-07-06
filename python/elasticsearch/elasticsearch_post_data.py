import requests
import os
import argparse
import json
import unidecode
import re
import csv
import pandas as pd
import string
import spacy



#getting user inputs 
parser = argparse.ArgumentParser()
parser.add_argument('--data_dir', help='directory where JSON are stored', type=str)
args = parser.parse_args()


es_index = 'discovery_dev_clean' # equivalent to SQL database
es_type = '_doc' # equivalent to SQL table: mandatory to use _doc for text elements
es_id_num_init = 1

# init index
# res = requests.post('https://search-PPTECH1-zrhgle3vemuqzhhs7fudth7cae.eu-west-3.es.amazonaws.com/'+es_index+'/'+es_type+'/'+str(es_id_num_init), json=data)

# if res.status_code != 200:
#     print('ERROR during init index !')
#     exit(1)

# List all files in a directory using os.listdir
with os.scandir(args.data_dir) as files:
    for file in files:
        if file.is_file():
            #print(args.data_dir)
            #print(file.name)
            with open(args.data_dir+'/'+file.name) as json_file:
                data = json.load(json_file)
                # data['value'] = clean_text(data['value'])
                # print('data to POST: {}\n'.format(data))
                # print('string POST command: {}\n'.format('https://search-PPTECH1-zrhgle3vemuqzhhs7fudth7cae.eu-west-3.es.amazonaws.com/'+es_index+'/'+es_type+'/'+str(es_id_num_init)))
                res = requests.post('https://search-PPTECH1-zrhgle3vemuqzhhs7fudth7cae.eu-west-3.es.amazonaws.com/'+es_index+'/'+es_type+'/'+str(es_id_num_init), json=data)
                # res = requests.post('https://search-PPTECH1-zrhgle3vemuqzhhs7fudth7cae.eu-west-3.es.amazonaws.com/'+es_index+'/'+es_type+'/'+str(es_id_num_init), json=data)
                es_id_num_init = es_id_num_init + 1

                # if res.status_code != 200:
                #     print('ERROR during POSTING file {} error !'.format(file.name))
                #     exit(1)
                # else:
                #     print('File {} correctly added in index {}'.format(file.name, es_index))
    
                if((res.status_code == 200) or (res.status_code == 201) ):
                    print('File {} correctly added in index {}'.format(file.name, es_index))
                else:
                    print('ERROR during POSTING file {} error !'.format(file.name))
                    exit(1)
    


# es_index = 'movies' # equivalent to SQL database
# es_type = '_doc' # equivalent to SQL table

# res = requests.post('https://search-PPTECH1-zrhgle3vemuqzhhs7fudth7cae.eu-west-3.es.amazonaws.com/movies/_doc/2', json={"director": "toto, Tim", "genre": ["Comedy","Sci-Fi"], "year": 1996, "actor": ["Jack Nicholson","Pierce Brosnan","Sarah Jessica Parker"], "title": "Mars Attacks!"})

# # verification si l'authentification utilisateur a bien fonctionné
# print(res.status_code)
# if res.status_code != 200:
#     print('request::request_from_db: Error, not connected during POST')
#     exit(1)
# else:
#     print('element correctly added in es!')

# res = requests.get('https://search-PPTECH1-zrhgle3vemuqzhhs7fudth7cae.eu-west-3.es.amazonaws.com/movies/_search?q=toto')

# print(res.status_code)
# if res.status_code != 200:
#     print('request::request_from_db: Error, not connected during GET')
#     exit(1)
# else:
#     print('element correctly GET in es!')

# res_json = res.json()
# print(res_json)
