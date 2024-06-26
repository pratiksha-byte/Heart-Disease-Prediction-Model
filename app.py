import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import joblib


# Loading The saved Model

Heart_model = joblib.load('heart.joblib')

columns=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']

# Sidebar for Navigation

with st.sidebar:
    
    selected = option_menu('Heart Disease Prediction using ML',
                           ['Heart Disease prediction'],
                           
                           icons = ['heart'],
                           
                           default_index = 0)
    
    
# Heart disease Prediction
if (selected == 'Heart Disease prediction'):
    
    # Page Title
    st.title('Heart Disease Prediction using ML')
    
    # Creating The Input Columns
    
    col1, col2, = st.columns(2)
     
    with col1:
        age = st.number_input('1.Age',29,77)
        
    with col2:
        sex = st.selectbox('2.Select Gender',['Male',' Female'])
    with col1:
        cp = st.selectbox('3. Select Chest Pain Type ',
                           ['Cardiac','Asymptomatic','Abnormal','Non cardiac'])
        
    with col2:
        trestbps = st.number_input('4.Enter Resting Blood Pressure',94,200)
    
    with col1:
        chol = st.number_input('5.Enter Serum Cholestral ',126,564)
        
    with col2:
        fbs = st.selectbox('6 Select Sugar ',["sugar","No Sugar"])
        
    with col1:
        restecg = st.selectbox('7.Select Resting Electrocardiographic Result ',
                                ['Normal','Anmormal','Hyper'])
        
    with col2:
        thalach = st.number_input('8.Enter Maximum Heart Rate achieved',72,202)
        
    with col1:
        exang = st.selectbox('9.Select Exercise Induced Angina',
                             ['Yes','No '])
        
    with col2:
        oldpeak = st.number_input('10.ST Depression induced by Exercise  (0 - 6.2)',step =0.1)
        
    with col1:
        slope = st.selectbox('11.Select Slope of the Peak ',
                              ['Up','Flat','Down'])
        
    with col2:
        ca = st.selectbox('12.Select Number of Vessels Coloured by  Flouroscopy',[0,1,2])
        
    with col1:
        thal = st.selectbox('13.Select Thal Defect ',
                             ['Normal','Fixed defect','Reversible Defect'])
                           
    
    
    # Code for Prediction
    
    def predict(): 
      row = np.array([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]) 
      X = pd.DataFrame([row], columns = columns)
      prediction = Heart_model.predict(X)
      if prediction[0] == 0: 
         st.success('Person does not have heart disease :thumbsup:')
      else: 
          st.error('Person have heart disease :thumbsdown:') 

    trigger = st.button('Predict', on_click=predict)
