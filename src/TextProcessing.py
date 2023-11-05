import re
import string
import spacy
from spacy import displacy
# nlp = spacy.load('fr_dep_news_trf')
nlp = spacy.load('fr_core_news_sm')


class TextProcesser:
    def __init__(self, path):
        with open(path, encoding='utf-8') as f:
            self.raw_txt = f.read()
        self.preprocess()
        


    def preprocess(self):
        # Process the text by removing punctuation, special chars and making it lowercase
        self.processed_txt = self.raw_txt.translate(str.maketrans('', '', string.punctuation))
        self.processed_txt = re.sub(r'[^\w\s]', '', self.raw_txt)
        self.processed_txt = self.raw_txt.lower()
        self.doc = nlp(self.processed_txt)
        self.sentences = list(self.doc.sents)
        self.entities = [(e.text, e.start_char, e.end_char, e.label_) for e in self.doc.ents]


    def render(self, opt):
        if (opt == "entities"):
            displacy.serve(self.doc, style='ent')


    """ def getSentence(self, print):
        if (print == False):
            with open("sentences.txt", "w", encoding='utf-8') as f:
                for s in self.sentences:
                    f.write(s.text)
        else:
            print(self.sentences)
    

    def getProcessedTxt(self, print):
        if (print == False):
            with open("processed.txt", "w", encoding='utf-8') as f:
                f.write(self.processed_txt)
        else:
            print(self.processed_txt)


    def getEntities(self, print):
        if (print == False):
            with open("entities.txt", "w", encoding='utf-8') as f:
                for ents in self.entities:
                    f.write(str(ents) + "\n")
        else:
            print(self.entities)
 """
