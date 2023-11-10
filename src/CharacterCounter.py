# It was harder than anticipated to make a good NER in french tried a lot of my own ideas then other's
# Finally found a good one on github and adapted it to my needs : https://github.com/hzjken/character-network/

import spacy
from nltk.tokenize import sent_tokenize
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("camembert-base")
model = AutoModelForSequenceClassification.from_pretrained("camembert-base-emotion")

# French sentiment analysis model
nlp_sent = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

# French NER model
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
    '''
    A function to recognize the name entity in a sentence.
    '''
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
 

def extract_adjectives(sentence):
    '''
    A function to extract adjectives from a sentence.
    '''
    doc = nlp(sentence)
    adjectives = [token.text for token in doc if token.pos_ == "ADJ"]
    return adjectives


def perform_sentiment_analysis(sentence):
    sentiment = nlp_sent(sentence)
    return sentiment


""" def perform_emotion_detection(text):
    inputs = tokenizer(text, return_tensors="pt")
    labels = torch.tensor([1]).unsqueeze(0)  # Assuming "1" represents a generic label
    with torch.no_grad():
        outputs = model(**inputs, labels=labels)
        logits = outputs.logits
    return logits[0].tolist() """

if __name__ == '__main__':
    path = "C:\\Users\\kenan\\code\\python\\nlp\\characterAnalysis\\letranger3.txt"
    text = read_text(path)
    text = sent_tokenize(text)
    ent_list = []
    adj_list = []
    sent_scores = []
    # emo_labels = []
    # emo_scores = []

    for sentence in text:
        ent = name_entity_recognition(sentence)
        if ent is not None:
            ent_list.append(ent)
        
        adj = extract_adjectives(sentence)
        if adj:
            adj_list.extend(adj)

        sentiment_score = perform_sentiment_analysis(sentence)
        sent_scores.append(sentiment_score)

    print("Named Entities:", ent_list)
    print("Adjectives:", adj_list)
    print("Sentiment Scores:", sent_scores)
    # print("Emotion Labels:", emo_labels)
    # print("Emotion Scores:", emo_scores)
