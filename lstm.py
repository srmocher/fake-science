from keras.preprocessing.text import Tokenizer
import pandas as pd

import re
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from os import listdir
from os.path import isfile, join
from pathlib2 import Path
import numpy as np
from gensim.models import KeyedVectors

docs = []


real_path = "./Science Data - Climate/Real"
fake_path = "./Science Data - Climate/Fake"
real_files = [f for f in listdir(real_path) if isfile(join(real_path, f))]
fake_files = [f for f in listdir(fake_path) if isfile(join(fake_path, f))]

stemmer = SnowballStemmer('english')
MAX_NB_WORDS = 200000
EMBEDDING_DIM = 150
MAX_SEQUENCE_LEN = 30
for file in real_files:
    contents = open(real_path+"/"+file,'r',encoding="utf-8",errors="ignore").read()
    doc = {}
    doc['label'] = 1
    doc['text'] = contents
    docs.append(doc)

for file in fake_files:
    contents = open(fake_path +'/'+file,encoding="utf-8",errors="ignore").read()
    doc = {}
    doc['label'] = 0
    doc['text'] = contents
    docs.append(doc)

word2_vec = KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin",limit=50000)
data = pd.DataFrame(docs)
data['text'] = data['text'].apply(lambda x:x.lower())
data['text'] = data['text'].apply(lambda x:re.sub('[^a-zA-Z0-9\s]','',x))

for index,row in data['text'].iteritems():
    text = row
    text = text.split()
    stemmed_words = [stemmer.stem(word) for word in text]
    text = " ".join(stemmed_words)
    data.set_value(index,'text',text)


max_features = 10000
max_len = 10000
tokenizer = Tokenizer(num_words=max_features,split=" ")
tokenizer.fit_on_texts(data['text'].values)
x = tokenizer.texts_to_sequences(data['text'].values)
word_index = tokenizer.word_index
x_train = sequence.pad_sequences(x,maxlen=max_len)
print(x_train.shape)
y = data.label
train_y = y

nb_words = min(max_features,len(word_index))+1

model = Sequential()
embedding_matrix = np.zeros((nb_words,EMBEDDING_DIM))
for word,i in word_index.items():
    if word in word2_vec.vocab:
        embedding_matrix[i] = word2_vec.word_vec(word)
#model.add(Embedding(max_features,200,input_length=x_train.shape[1]))
model.add(Embedding(nb_words,EMBEDDING_DIM,weights=[embedding_matrix],input_length=max_len,trainable=False))
model.add(LSTM(EMBEDDING_DIM))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='nadam',metrics=['acc'])
model.summary()
model.fit(x_train,train_y,epochs=3,batch_size=128,validation_split=0.30)


