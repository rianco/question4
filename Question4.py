# -*- coding: utf-8 -*-
"""
Created on Thu May 30 08:36:43 2024

@author: rianc
"""
import numpy as np
import pickle

import streamlit as st 
import pandas as pd


#loading the saved model
loaded_model = pickle.load(open('trained_model.sav','rb'))


def heart_disease_prediction(input_data):
    #to change the input values as numpy array
    input_array=np.asarray(input_data)
    
    #reshape the array as we only predict for 1 at time 
    input_reshaped=input_array.reshape(1, -1)
    column_values = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang', 'oldpeak','slope','ca','thal'] 

    df = pd.DataFrame(data = input_reshaped,  
     columns = column_values) 
    prediction = loaded_model.predict(df)
    print(prediction)
    if(prediction[0]==0):
        return "The pacient is Healthy"
    else:
        return "The pacient have a heart disease"
    
def main():
     #giving a title
     
     st.title('Heart Prediction Web APP')
     
     #age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang, oldpeak,slope,ca,thal,
     
     age = st.number_input('Age of patient',step=1,min_value=18)
     sex = st.selectbox("Select the Sex of the patient",("Male","Female"),index=None)
     if sex== "Male":
         sex=1
     elif sex =="Female":
         sex=0
    
     cp = st.selectbox("Select chest pain type for the patient",("typical angina","atypical angina","non-anginal pain","asymptoatic"),index=None)
     if cp=="typical angina":
         cp=0
     elif cp=="atypical angina":   
         cp=1
     elif cp=="non-anginal pain":   
         cp=2
     elif cp=="asymptoatic":   
         cp=3
    
     trestbps = st.number_input('Resting blood Pressure om mm Hg on admision',step=1,placeholder="Input the blood pressure",value=None)
     chol = st.number_input('Serum Cholestoral in mg/dl',step=1,placeholder="Input the chol of patient",value=None)
     fbs = st.selectbox('fasting blood sugar > 120mg/dl',("True","False"),index=None)
     if fbs=="True":
         fbs=1
     elif fbs =="False":
         fbs=0
     restecg = st.selectbox('Resting electrocardiographic',("Normal","Abnormal","ventricular hypertrophy"),index=None)
     if restecg=="Normal":
         restecg=0
     elif restecg=="Abnormal":
         restecg=1
     elif restecg=="ventricular hypertrophy":
         restecg=2
     thalach = st.number_input('Maximim heart rate achieved of patient',step=1,value=None)
     exang = st.selectbox('Exercise induced angine',("True","False"),index=None)
     if exang=="True":
         exang=1
     elif exang=="False":
         exang=0
     oldpeak = st.number_input('ST depression induced by exercise relative to rest',step=0.1,value=None)
     slope = st.selectbox('The slope of the peak exercise ST segment ',("Upsloping","Flat","Downsloping"),index=None)
     if slope=="Upsloping":
         slope=0
     elif slope =="Flat":
         slope=1
     elif slope =="Downsloping":
         slope=2
     ca = st.number_input('Number of major vessels colored by fluoroscope',step=1,value=None,min_value=0,max_value=4)
     thal = st.selectbox('Status of the heart',("Normal","Fixed defect","Reversible defect","Unknown"),index=None)
     if thal=="Normal":
         thal=1
     elif thal=="Fixed defect":
         thal=2
     elif thal=="Reversible defect":
         thal=3
     elif thal=="Unknown":
         thal=0
     target =''
     
     #create the button for the prediction 
     if st.button('Heart Disease prediction'):
         #cp,trestbps,chol,fbs,restecg,thalach,exang, oldpeak,slope,ca,thal
         if age != None and sex!= None and cp != None and trestbps!= None and chol != None and fbs!= None and restecg!= None and thalach != None and exang!= None and oldpeak != None and ca!= None and thal!= None:
          target=heart_disease_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang, oldpeak,slope,ca,thal])
          st.success(target)
         else:
             st.error(" ERROR Make sure that all the fields are filled ")
     
     
     
if __name__=='__main__':
    main()

    

   
