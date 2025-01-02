import spacy

from spacy import displacy

text='Real Madrid is the best club in Europe'

nlp=spacy.load('en_core_web_sm')

doc = nlp(text)

print('\nNamed Entitie\n')

for ent in doc.ents:
    print(ent.text,ent.label_)

displacy.render(doc,style='ent',jupyter='True')
