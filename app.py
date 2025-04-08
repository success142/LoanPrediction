import numpy as np
import streamlit as st 
import pickle
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def load_model():
    with open('LoanModel.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
model = data['model']

def show_predict_page():
    st.title('Loan Prediction')
    st.write('SELECT THE NEEDED INFORMATION BELOW')

    education = ['Graduate', 'Not Graduate']
    self_employed = ['No', 'Yes']
    no_of_dependents = [0, 1, 2, 3, 4, 5]

    income_annum = st.slider('Annual Income', min_value=0, max_value=1000000000, value=1000, key='income')
    loan_amount = st.slider('Loan Amount', min_value=0, max_value=1000000000, value=1000, key='loan')
    loan_term = st.slider('Loan Term (months)', min_value=1, max_value=360, value=12, key='term')
    cibil_score = st.slider('CIBIL Score', min_value=300, max_value=900, value=600, key='cibil')
    residential_assets_value = st.slider('Residential Asset Value', min_value=0, max_value=1000000000, value=1000, key='res')
    commercial_assets_value = st.slider('Commercial Asset Value', min_value=0, max_value=1000000000, value=1000, key='com')
    luxury_assets_value = st.slider('Luxury Asset Value', min_value=0, max_value=1000000000, value=1000, key='lux')
    bank_asset_value = st.slider('Bank Asset Value', min_value=0, max_value=1000000000, value=1000, key='bank')

    EDUCATION = st.selectbox('Education', education)
    SELF_EMPLOYED = st.selectbox('Self Employed', self_employed)
    DEPENDENTS = st.selectbox('Number of Dependents', no_of_dependents)

    ok = st.button("Predict Loan Status")
    if ok:
        # Convert categorical inputs
        education_val = 1 if EDUCATION == 'Graduate' else 0
        self_employed_val = 1 if SELF_EMPLOYED == 'Yes' else 0

        # Prepare input
        X = np.array([[education_val, self_employed_val, DEPENDENTS,
                       income_annum, loan_amount, loan_term, cibil_score,
                       residential_assets_value, commercial_assets_value,
                       luxury_assets_value, bank_asset_value]])

        # Predict
        LOAN_PREDICT_STATUS = model.predict(X)
        st.subheader(f'The Loan Status is: **{LOAN_PREDICT_STATUS}**')

show_predict_page()
