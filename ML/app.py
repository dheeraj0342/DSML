import streamlit as st
import pandas as pd
import pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('Package prediction')

cgpa = st.number_input('Enter your CGPA',min_value=0.0, max_value=10.0, value=0.0, step=0.1)

if st.button('Predict'):
    prediction = model.predict([[cgpa]])
    st.success(f'Your predicted package is {prediction[0]}')