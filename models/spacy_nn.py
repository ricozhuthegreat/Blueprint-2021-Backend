
import spacy

class Spacy_Entity_Extractor():

    def __init__(self, text):
        # Load English tokenizer, tagger, parser, NER and word vectors
        self.nlp = spacy.load("en_core_web_sm")
        self.text_in = text
        self.doc = self.nlp(self.text_in)
        self.nouns = [chunk.text for chunk in self.doc.noun_chunks]
        self.verbs = [token.lemma_ for token in self.doc if token.pos_ == "VERB"]

    def get_nouns(self):
        return self.nouns

    def get_verbs(self):
        return self.verbs

    def print_lem(self):
        for entity in self.doc.ents:
            print(entity.text, entity.label_)