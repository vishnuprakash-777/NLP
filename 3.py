import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from collections import Counter
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

text='hi how are you,long time'

tokens = word_tokenize(text.lower())

unigrams=list(ngrams(tokens,1))
bigrams=list(ngrams(tokens,2))
trigrams=list(ngrams(tokens,3))

unigrams_count =Counter(unigrams)
bigrams_count =Counter(bigrams)
trigrams_count =Counter(trigrams)
print(bigrams_count)
print(trigrams_count)

bigram_probabilities={
    bigram:count / unigrams_count[(bigram[0],)]
    for bigram,count in bigrams_count.items()
}

trigarm_probabilities={
    trigram:count / bigrams_count[(trigram[0],trigram[1])]
    for trigram,count in trigrams_count.items()
}

for bigram,prob in bigram_probabilities.items():
  print(f'Bigram:{bigram},Probability{prob:4f}')

for trigram,prob in trigarm_probabilities.items():
  print(f'Trigram:{trigram},Probability{prob:4f}')