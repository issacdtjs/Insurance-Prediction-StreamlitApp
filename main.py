# streamlit run main.py

import streamlit as st
import pickle
import time


st.title("Insurance Claim Prediction")

# Load model
model = pickle.load(open('insurance_prediction.pkl', 'rb'))

with st.form('user_inputs'):
    age = st.number_input('Age', min_value=0)
    sex = st.selectbox('Sex', options=['Female', 'Male'])
    bmi = st.number_input('Body Mass Index', min_value=0.000, format="%.3f")
    steps = st.number_input('Average Walking Steps', min_value=0)
    children = st.number_input('Number of children', min_value=0)
    smoker = st.selectbox('Are you a Smoker?', options=['Yes', 'No'])
    region = st.selectbox('Residential Area', options=['Northeast=0', 'Northwest=1', 'Southeast=2', 'Southwest=3'])
    charges = st.number_input('Individual medical costs billed by health insurance', min_value=0.00000, format="%.5f")

    if sex == 'Male':
        sex = 1
    elif sex == 'Female':
        sex = 0

    if smoker == 'Yes':
        smoker = 1
    elif smoker == 'No':
        smoker = 0

    if region == 'Northeast=0':
        region = 0
    elif region == 'Northwest=1':
        region = 1
    elif region == 'Southeast=2':
        region = 2
    elif region == 'Southwest=3':
        region = 3

    submit = st.form_submit_button("Predict")

    if submit:
        start = time.time()
        new_prediction = model.predict([[age, sex, bmi, steps, children, smoker,
                                       region, charges]])
        end = time.time()
        st.write("Prediction time taken: ", round(end - start, 4), "seconds")

        if new_prediction[0] == 1:
            result = 'Yes'
        elif new_prediction[0] == 0:
            result = 'No'

        st.write("Predicted Claim: ", result)
