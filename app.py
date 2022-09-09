import streamlit as st
import pickle

model=pickle.load(open('model.pkl','rb'))

st.title('Student Grade Prediction System')
studytime=st.number_input('Enter duration of studyhours')
failures=st.number_input('Enter number of failed exams')
absences=st.number_input('Enter number of absent classes')
g1=st.number_input('Enter Grades for Mid1')
g2=st.number_input('Enter Grades for Mid2')

if st.button('Predict'):
    dataset=[[studytime,failures,absences,g1,g2]]
    out=model.predict(dataset)
    if(out[0]>20):
        out[0]=20

    st.success(out[0])