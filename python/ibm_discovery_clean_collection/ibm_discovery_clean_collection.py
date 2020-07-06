import unidecode
import re
import csv
import pandas as pd
import string
import json
import spacy
import argparse
import os



from string import punctuation

# s'assure que le paramètre passé est bien encodé en utf-8
def ensureUtf(s):
    try:
        if type(s) == unicode:
            return s.encode('utf8', 'ignore')
    except: 
        return str(s)


# enleve les accents du mot s'il y en a
def remove_accent(word):
    accented_string = ensureUtf(word)
    unaccented_string = unidecode.unidecode(accented_string)

    return unaccented_string


# remplace les accents html format par des accents normaux
def replace_html_accent(text):
    text1 = text.replace("&acirc;", "â")
    text2 = text1.replace("&agrave;", "à")
    text3 = text2.replace("&eacute;", "é")
    text4 = text3.replace("&ecirc;", "ê")
    text5 = text4.replace("&egrave;", "è")
    text6 = text5.replace("&euml;", "ë")
    text7 = text6.replace("&icirc;", "î")
    text8 = text7.replace("&iuml;", "ï")
    text9 = text8.replace("&ocirc;", "ô")
    text10 = text9.replace("&oelig;", "œ")
    text11 = text10.replace("&ugrave;", "û")
    text12 = text11.replace("&uuml;", "ü")
    text13 = text12.replace("&ccedil;", "ç")

    return text13



def replace_special_characters(text):
    text1 = text.replace("â", "a")
    text2 = text1.replace("à", "a")
    text3 = text2.replace("é", "e")
    text4 = text3.replace("ê", "e")
    text5 = text4.replace("è", "e")
    text6 = text5.replace("ë", "e")
    text7 = text6.replace("î", "i")
    text8 = text7.replace("ï", "i")
    text9 = text8.replace("ô", "o") 
    text10 = text9.replace("œ", "oe")
    text11 = text10.replace("û", "u")
    text12 = text11.replace("ü", "u")
    text13 = text12.replace("ç", "c")
    text14 = text13.replace("\n", " ")

    return text14


# clean le html en enlevant les balises
def clean_html(raw_html):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', raw_html)

    return cleantext


def define_custom_ponctuations(ponctuations):
    new_ponctuations = ''
    for i in range(len(ponctuations)):
        if(ponctuations[i] != "'"):
            new_ponctuations = new_ponctuations+ponctuations[i]
    
    return new_ponctuations

# clean le text en enlevant les symboles specifiques, les ponctuations
def clean_text(text):
    #print('in clean_text')
    # print('functions::clean_text: punctuation: {}'.format(punctuation))
    # print('functions::clean_text: define_custom_ponctuations(punctuation): {}'.format(define_custom_ponctuations(punctuation)))
    # print('functions::clean_text: type(punctuation): {}'.format(type(punctuation)))
    text_accent_fixed = replace_html_accent(text)
    text_accent_fixed2 = replace_special_characters(text_accent_fixed)
    char_to_remove = ['(',')','[',']','{','}']
    raw_text = clean_html(text_accent_fixed2)
    text_punctation_removed = ''.join(c for c in raw_text if c not in define_custom_ponctuations(punctuation))
    text_whitespace_removed = text_punctation_removed.strip()
    text_replace_characters = ''.join(c for c in text_whitespace_removed if c not in char_to_remove)
    #text_replace_characters_lower = text_replace_characters.lower()

    return text_replace_characters



#getting user inputs 
parser = argparse.ArgumentParser()
parser.add_argument('--input_json', help='discovery JSON file to split', type=str)
parser.add_argument('--output_dir', help='directory where to generate splitted files', type=str)
args = parser.parse_args()


if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)

filename_wo_extention = os.path.splitext(args.input_json)[0]

filename_cleaned = filename_wo_extention+'_cleaned.json'

with open(args.input_json) as json_file:
    data = json.load(json_file)
    #print(data['results'][0]['metadata']['name'])

    for i in range(len(data['results'])):
        data['results'][i]['metadata']['value'] = clean_text(data['results'][i]['metadata']['value'])
        # d['new_name'] = d.pop('old_name')
        
        # if('Knowledge_id' not in data['results'][i]['metadata']):
        #     data['results'][i]['metadata']['knowledge_id'] = data['results'][i]['metadata'].pop('knowledge_id')
        # else:
        #     data['results'][i]['metadata']['knowledge_id'] = data['results'][i]['metadata'].pop('Knowledge_id')

        if('Knowledge_id' in data['results'][i]['metadata']):
            data['results'][i]['metadata']['knowledge_id'] = data['results'][i]['metadata'].pop('Knowledge_id')
        

    with open(filename_cleaned, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile)
