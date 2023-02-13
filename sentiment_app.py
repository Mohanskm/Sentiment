#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pickle
import streamlit as st

model=pickle.load(open("sentiment.p","rb"))

st.title("Sentiment Analysis Model")
st.write("Enter text for sentiment analysis: ")
message=st.text_area("","Type Here....")
if st.button("PREDICT"):
    a=model.predict([message])[0]
    if(a==0):
        disp="Negative Sentiment!"
    else:
        disp="Positive Sentiment!"
    st.write("The sentiment of given text is: ",disp)    

