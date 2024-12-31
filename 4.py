import nltk
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('punkt')
nltk.download('punkt_tab')

def pos_sentence(sentence):
  print('Tokens\n')
  tokens=nltk.word_tokenize(sentence)
  print(tokens)
  print('\nPOS Tags\n')
  pos=nltk.pos_tag(tokens)
  print(pos)

user_input=input("Enter the sentence to tag: ")
pos_sentence(user_input)