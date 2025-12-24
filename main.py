import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
import streamlit as st

# Load Model and word index
word_index = imdb.get_word_index()
reverse_word_index = {value:key for key,value in word_index.items()}

model = load_model('notebooks/simple_rnn_imdb.h5')

# Helper functions
Max_Vocab_size =1000
def decoder_review (encoded_review):
    return ' '.join([reverse_word_index.get(i-3,'?') for i in encoded_review])

def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word,2)+3
                      if word_index.get(word,2)+3<Max_Vocab_size else 2 for word in words]
    paddded_review = sequence.pad_sequences([encoded_review],maxlen=500)
    return paddded_review


# Streamlit app
st.title(' IMDB Movie Review Sentiment Analysis App')
st.write('Enter a movie review to classify as positive or negative.')

user_input = st.text_area('Movie Review')

if st.button('Classify'):
    
    preprocessed_review = preprocess_text(user_input)
    prediction = model.predict(preprocessed_review)
    
    sentiment = 'Positive' if prediction[0][0]>0.5 else 'Negative'
    
    st.write(f'Sentiment: {sentiment}')
    st.write(f'Prediction Score: {prediction[0][0]}')
else:
    st.write('Please enter a movie review.')

