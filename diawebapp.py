# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 21:59:49 2022

@author: mallu
"""

import numpy as np
import pickle
import streamlit as st
from PIL import Image

#loading the saved file
loaded_model  = pickle.load(open('diabetes_model.sav','rb'))


#creating a function for prediction
def diabetes_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return('The person is not diabetic')
    else:
      return('The person is diabetic')



import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('d2.jpg')
    

#steamlit library code
def main():
    
    col1, col2, col3 = st.columns(3)

    with col1:
        
        st.write("")

    with col2:
        
        img = Image.open("d1.jpg")
        st.image(img,width=150)

    with col3:
        
        st.write("")
    #giving the title
    st.title('DIABETES PREDICTION WEB APP')
   
    
    #getting the iput data from the uder
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('SkinThickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    
    #code for prediction
    Diagnosis=''
    
    #creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        Diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(Diagnosis)
    
    
if __name__=='__main__':
    main()
    
    
    
    
 
    
 
    
 
    
 
    
 
    
 
    
  
    
  
    
  
