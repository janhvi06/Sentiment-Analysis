import streamlit as st
import sklearn
import joblib
model = joblib.load('https://github.com/janhvi06/Sentiment-Analysis/blob/main/SentimentAnalysis_model')
st.title('Sentiment Analysis Classifier')
ip = st.text_input("Enter the message")
op = model.predict([ip])
if st.button('Sentiment'):
  st.title(op[0])   
