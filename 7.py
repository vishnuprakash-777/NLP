import re
from nltk import sent_tokenize, word_tokenize, pos_tag
import nltk
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('punkt_tab')
# Function to resolve pronouns
def resolve_pronouns(text):
    # Tokenize text into sentences
    sentences = sent_tokenize(text)
    entities = []  # To store potential antecedents
    resolved_text = []  # To store sentences with resolved pronouns
    for sentence in sentences:
        words = word_tokenize(sentence)
        tagged = nltk.pos_tag(words) 
        resolved_sentence =[]

        for word,tag in tagged:
            if tag in ['PRP','PRP$']:
                if entities:
                    resoloved_word=entities[-1]
                    if word.lower() in ['his','her','their']:
                        resoloved_word +='s'
                    resolved_sentence.append(resoloved_word)
                else:
                    resolved_sentence.append(word)

            else:
                if tag in ['NNP','NNP$']:
                    entities.append(word)
                resolved_sentence.append(word)

        resolved_text.append(" ".join(resolved_sentence))

    return " ".join(resolved_text)
# Example text
text = "John and Mary went to the store. He and she bought some groceries."
# Resolve coreferences manually
resolved_text = resolve_pronouns(text)
print("Original Text:", text)
print("Resolved Text:", resolved_text)
