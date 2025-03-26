import nltk
import spacy

nltk.download("punkt")

nlp = spacy.load("en_core_web_sm")
doc = nlp("Hello, I am IRIS, your AI assistant !")
print([token.text for token in doc])