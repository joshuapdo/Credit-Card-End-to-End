import os
import pickle
import streamlit as st

# Load the saved model
Loan_Status_model = pickle.load(open('/Users/pdo/Downloads/Credit Card End to End/Saved_model/Loan_Status_model.sav', 'rb'))

# Dictionary for label encoding (with corrected labels)
gender_encoding = {'Male': 0, 'Female': 1}
married_encoding = {'No': 0, 'Yes': 1}
dependents_encoding = {'0': 0, '1': 1, '2': 2, '3+': 3}
education_encoding = {'Not Graduate': 0, 'Graduate': 1}
self_employed_encoding = {'No': 0, 'Yes': 1}
property_area_encoding = {'Rural': 0, 'Semiurban': 1, 'Urban': 2}

# Set page configuration
st.set_page_config(page_title="Loan Eligibility",
                   layout="wide",
                   page_icon="🏦")

# Sidebar for navigation 
st.sidebar.title("Navigation")

# Main content
st.title('Loan Eligibility Prediction using Machine Learning')

col1, col2, col3 = st.columns(3)

with col1:
    Gender = st.selectbox('Gender', ['Male', 'Female'])

with col2:
    Married = st.selectbox('Married', ['No', 'Yes'])

with col3:
    Dependents = st.selectbox('Dependents', ['0', '1', '2', '3+'])

with col1:
    Education = st.selectbox('Education', ['Not Graduate', 'Graduate'])

with col2:
    Self_Employed = st.selectbox('Self Employed', ['No', 'Yes'])

with col3:
    ApplicantIncome = st.number_input('ApplicantIncome', step=1, min_value=0)

with col1:
    CoapplicantIncome = st.number_input('CoapplicantIncome', step=1, min_value=0)

with col2:
    LoanAmount = st.number_input('LoanAmount', step=1, min_value=0)

with col3:
    Loan_Amount_Term = st.number_input('Loan_Amount_Term', step=1, min_value=0)

with col1:
    Credit_History = st.number_input('Credit_History', step=1, min_value=0, max_value=1)

with col2:
    Property_Area = st.selectbox('Property_Area', ['Rural', 'Semiurban', 'Urban'])
    
# When the predict button is clicked
if st.button('Predict Loan Status'):
    # Encode the categorical data to match model training preprocessing
    gender_encoded = gender_encoding[Gender]
    married_encoded = married_encoding[Married]
    dependents_encoded = dependents_encoding[Dependents]
    education_encoded = education_encoding[Education]
    self_employed_encoded = self_employed_encoding[Self_Employed]
    property_area_encoded = property_area_encoding[Property_Area]
    
    # Prepare user input for prediction, including encoded categorical variables
    user_input = [gender_encoded, married_encoded, dependents_encoded, education_encoded,
                  self_employed_encoded, ApplicantIncome, CoapplicantIncome, LoanAmount,
                  Loan_Amount_Term, Credit_History, property_area_encoded]

    # Predict loan status using the loaded model
    Loan_prediction = Loan_Status_model.predict([user_input])

    # Displaying the prediction result
    if Loan_prediction[0] == 1:
       st.success('Loan Approved.')
    else:
        st.error('Loan Not Approved.')
