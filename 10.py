import pandas as pd
from textblob import TextBlob
from sklearn.metrics import accuracy_score,classification_report

def get_sentiment(text):
    blob=TextBlob(text)

    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        sentiment = 'positive'
    elif polarity < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    return sentiment,polarity,subjectivity


data = {
    'text':['He is a good person','Its an average movie','It is horrible','it is neutral'],
    'label':['positive','neutral','negative','neutral']
}

df = pd.DataFrame(data)

df['predicted_sentimence'],_,_ = zip(*df['text'].apply(get_sentiment))

print(df[['text','label','predicted_sentimence']])

accuracy_score = accuracy_score(df['label'],df['predicted_sentimence'])
print(f'Accuracy : {accuracy_score:2f}')
print(classification_report(df['label'],df['predicted_sentimence']))
