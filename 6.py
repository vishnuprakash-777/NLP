import nltk
from nltk.corpus import treebank
from nltk.tag import CRFTagger

nltk.download('treebank')

data=treebank.tagged_sents()
train_data=data[:3000]
test_data=data[3000:]

ct=CRFTagger()
ct.train(train_data,'model.crf.tagger')
print('Training Model Saved.')

accuracy=ct.evaluate(test_data)
print('Accuracy',accuracy)

sentence=['hii','hello']
tages=ct.tag(sentence)
print(tages)
