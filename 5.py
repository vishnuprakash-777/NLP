import nltk
from nltk.corpus import treebank
from nltk.tag.hmm import HiddenMarkovModelTrainer
from nltk.tokenize import word_tokenize,sent_tokenize


nltk.download('treebank')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('universal_tagset')

def trainer():
    tagged_sents = treebank.tagged_sents(tagset='universal')
    trainer = HiddenMarkovModelTrainer()
    tagger = trainer.train(tagged_sents)
    return tagger

hmm_tagger=trainer()

def pos_tag(sentence,tagger):
  sent = sent_tokenize(sentence)
  full_taggers=[]
  for token in sent:
    tokens = word_tokenize(token)
    tagged_tokens = tagger.tag(tokens)
    full_taggers.append(tagged_tokens)
    
  return full_taggers

user_input='How is the day going'
print(pos_tag(user_input,hmm_tagger))
