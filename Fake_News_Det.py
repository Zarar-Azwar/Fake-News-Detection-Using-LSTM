from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Embedding,LSTM,Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import one_hot
import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer
stemmer=PorterStemmer()
import re
from nltk.corpus import stopwords
nltk.download('stopwords')
model=load_model('E:\WebApplication\Fake_News_Detection-master\Fake_News_Detection-master\FakeNews.h5')

app = Flask(__name__)

def fake_news_det(new):
    sent=re.sub('[^A-Za-z]',' ',new)
    sent=sent.lower()
    sent=sent.split()
    sent=[stemmer.stem(word) for word in sent if word not in set(stopwords.words('english'))]
    sent=' '.join(sent)
    ohRep=[one_hot(sent,5000)] #one hot representation
    pSeq=pad_sequences(ohRep,padding='pre',maxlen=20)
    d=np.array(pSeq)
    predVal=model.predict(d)
    if predVal < 0.5:
        val='FAKE'
    else:

        val='REAL'
    
    return val,predVal

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        pred,predVal = fake_news_det(message)
        print(pred,predVal,sep='\t')
        return render_template('index.html', prediction=pred)
    else:
        return render_template('index.html', prediction="Something went wrong")

if __name__ == '__main__':
    app.run(debug=True)