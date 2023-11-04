import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy
nlp = spacy.load('fr_core_news_sm')


class TextProcesser:
    def __init__(self, path):
        with open(path, encoding='utf-8') as f:
            self.raw_txt = f.read()
        self.preprocess()
        self.tokenize(self.processed_txt)
        self.filter()
        self.tag()
        


    def preprocess(self):
        self.processed_txt = self.raw_txt.lower()
        self.processed_txt = self.raw_txt.translate(str.maketrans('', '', string.punctuation))
        self.processed_txt = re.sub(r'[^\w\s]', '', self.raw_txt)


    def tokenize(self, txt):
        self.tokenized_txt = word_tokenize(txt)


    def filter(self):
        self.filtered_tokens = [
            word for word in self.tokenized_txt
                if word not in stopwords.words('french')
        ]


    def tag(self):
        self.filtered_txt = " ".join(self.filtered_tokens)
        self.tagged = nlp(self.filtered_txt)


    def processedToFile(self):
        with open("processed.txt", "w", encoding='utf-8') as f:
            f.write(self.filtered_txt)
    
    def full_print(self):
        print(self.filtered_txt)
        print(self.tagged)
        print(self.tagged.ents)
        print(self.tagged.noun_chunks)
        for token in self.tagged:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                token.shape_, token.is_alpha, token.is_stop)

    def showEntities(self):
        with open("entities.txt", "w", encoding='utf-8') as f:
            for ent in self.tagged.ents:
                f.write(ent.text + " " + ent.label_ + "\n")
