# It was harder than anticipated to make a good NER in french tried a lot of my own ideas then other's
# Finally found a good one on github and adapted it to my needs : https://github.com/hzjken/character-network/

import spacy
from nltk.tokenize import sent_tokenize
nlp = spacy.load('fr_core_news_sm')


def flatten(input_list):
    '''
    A function to flatten complex list.
    :param input_list: The list to be flatten
    :return: the flattened list.
    '''

    flat_list = []
    for i in input_list:
        if type(i) == list:
            flat_list += flatten(i)
        else:
            flat_list += [i]

    return flat_list


def read_text(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        data = f.read().replace('\n', '').replace('\r', '').replace("\'", "'")

    return data

def name_entity_recognition(sentence):
    doc = nlp(sentence)
     # retrieve person and organization's name from the sentence
    name_entity = [x for x in doc.ents if x.label_ in ['PER', 'ORG']]
    # convert all names to lowercase and remove 's in names
    name_entity = [str(x).lower().replace("'s","") for x in name_entity]
    # split names into single words ('Harry Potter' -> ['Harry', 'Potter'])
    name_entity = [x.split(' ') for x in name_entity]
    # flatten the name list
    name_entity = flatten(name_entity)
    # remove name words that are less than 3 letters to raise recognition accuracy
    name_entity = [x for x in name_entity if len(x) >= 3]
    if len(name_entity) > 0:
        return name_entity
    

if __name__ == '__main__':
    path = "C:\\Users\\kenan\\code\\python\\nlp\\characterAnalysis\\letranger3.txt"
    text = read_text(path)
    text = sent_tokenize(text)
    ent_list = []
    for sentence in text:
        ent = name_entity_recognition(sentence)
        if ent != None:
            ent_list.append(ent)

    ent_list = flatten(ent_list)
    print(ent_list)
