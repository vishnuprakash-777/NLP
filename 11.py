import spacy

text = 'I am the king Vishnu,king of paris'

nlp=spacy.load('en_core_web_sm')

doc = nlp(text)

print("\nTokens\n")

for token in doc:
    print(token.text)

print('\nPOS-tagging\n')

for token in doc:
    print(token.text,token.pos_,token)

print('\nNamed Entities\n')

for ent in doc.ents:
    print(ent.text,ent.label_)

'''
print('\nDependency Parsing\n')

for token in doc:
    print(token.text,token.dep_,token.head.text)
    
   

print('\nLemmatizaation\n')

for token in doc:
    print(token.text,token.lemma_)'''