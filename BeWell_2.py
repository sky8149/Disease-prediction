# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 07:41:14 2022

@author: shogu
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

#diabetes_model = pickle.load(open('C:/BeWell/diabetes_model_1.sav','rb'))
#heart_disease_model = pickle.load(open('C:/BeWell/heart_disease1.sav','rb'))

diabetes_model = pickle.load(open('diabetes_model_1.pkl','rb'))
heart_disease_model = pickle.load(open('heart_disease1.pkl','rb'))

# sidebar for navigation
with st.sidebar :
    selected = option_menu('BeWell',['Diabetes Prediction','Heart Disease Prediction']
            ,icons =['activity','heart']
                           ,default_index = 0)
    
# diabetes prediction page

if(selected == 'Diabetes Prediction'):
    # page title
    st.title('BeWell Diabetes Predictor')
    
    # getting the input data from the user
    # creating columns for better visualisation 
    col1, col2, col3 = st.columns(3)
   
    with col1:
       Pregnancies = st.text_input('Number of Pregnancies')
       
    with col2:
       Glucose = st.text_input('Glucose Level(0-200)')
   
    with col3:
       BloodPressure = st.text_input('Blood Pressure value(0-130)')
   
    with col1:
       SkinThickness = st.text_input('Skin Thickness value(0-100)')
   
    with col2:
       Insulin = st.text_input('Insulin Level(0-800)')
   
    with col3:
       BMI = st.text_input('BMI value(0.0-70.0)')
   
    with col1:
       DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value(0.00-3.00)')
   
    with col2:
       Age = st.text_input('Age of the Person')
   
   
    # code for Prediction
    diab_diagnosis = ''
   
    # creating a button for Prediction
   
    if st.button('Diabetes Test Result'):
       diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
       
       if (diab_prediction[0] == 1):
         diab_diagnosis = 'The person is diabetic'
       
       else:
         diab_diagnosis = 'The person is not diabetic'
       
    st.success(diab_diagnosis)
    
if(selected == 'Heart Disease Prediction'):
    #page title
    st.title('BeWell Heart Disease Predictor')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex(1 = male; 0 = female)')
        
    with col3:
        cp = st.text_input('Chest Pain types(0-3)')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure(90-200)')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl(120-565)')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl(1=T;0=F)')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results(0-2)')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved(70-200)')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina(1=yes;0=no)')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise(0.0-6.5)')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment(0:UP,1:FLAT,2:DOWN)')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy(0-3)')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)


