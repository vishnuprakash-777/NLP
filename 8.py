from transformers import MarianMTModel,MarianTokenizer

model_name='Helsinki-NLP/opus-mt-en-hi'
tokensizer=MarianTokenizer.from_pretrained(model_name)
model=MarianMTModel.from_pretrained(model_name)

def translate(text):
  tokenizer_text = tokenizer(text,return_tensors='pt',padding=True,truncation=True)
  translation = model.generate(**tokenizer_text)
  translated_text = tokenizer.decode(translation[0],skip_special_tokens=True)
  return translated_text

text=input('enter the sentence')
print('\'nTranslated Sentence\n',translate(text))
