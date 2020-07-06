import json
import argparse
import os


#getting user inputs 
parser = argparse.ArgumentParser()
parser.add_argument('--input_json', help='discovery JSON file to split', type=str)
parser.add_argument('--output_dir', help='directory where to generate splitted files', type=str)
args = parser.parse_args()


if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)


with open(args.input_json) as json_file:
    data = json.load(json_file)
    #print(data['results'][0]['metadata']['name'])

    for i in range(len(data['results'])):
        current_file_name = 'grain'+str(i)+'.json'
        current_data = data['results'][i]['metadata']
        with open(args.output_dir+'/'+current_file_name, 'w', encoding='utf-8') as outfile:
            json.dump(current_data, outfile)
