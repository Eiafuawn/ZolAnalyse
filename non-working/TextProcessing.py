import spacy
from spacy import displacy
nlp = spacy.load('fr_core_news_md')


class TextProcesser:
    def __init__(self, path):
        with open(path, encoding='utf-8') as f:
            self.raw_txt = f.read()
        self.doc = nlp(self.raw_txt)        
        self.sentences = list(self.doc.sents)

    
    def processBySentence(self):
        self.entities_by_sentence = []
        for sentence in self.sentences:
            entities = [(e.text, e.start_char, e.end_char, e.label_) for e in sentence.ents]
            self.entities_by_sentence.append(entities)

    def render(self, opt):
        if (opt == "entities"):
            displacy.serve(self.doc, style='ent')
        if (opt == "sentence"):
            displacy.serve(self.doc, style='dep')
        if (opt == "entities_by_sentence"):
            print(self.entities_by_sentence)
