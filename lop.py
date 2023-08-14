import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('trained_model.sav', 'rb'))

#creating function
def loanpred(input_data):
    #changing input data to numpy array
    input_data_as_numpy= np.asarray(input_data)
    #reshape the array for one instance
    input_data_reshaped= input_data_as_numpy.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0] == 0):
        return 'Loan Rejected'
    else:
        return 'Loan Accepted'

st.title("Loan Outcome Prediction Form")
st.subheader("Enter details below")

with st.form("form1", ):
    gender = st.radio("Gender",('Male','Female'))
    married = st.radio("Married",('Yes','No'))
    depen = st.slider("No of Dependents", min_value = 0, max_value = 10)
    education = st.radio("Education",('Graduate','Not Graduate'))
    selfempl = st.radio("Self Employed",('Yes','No'))
    aincome = st.number_input('Applicant Income', min_value=0, max_value=91000, value=0, step=1)
    coaincome = st.number_input('Co-Applicant Income', min_value=0, max_value=45000, value=0, step=1)
    lamount = st.number_input('Loan Amount', min_value=0, max_value=800, value=0, step=1)
    lterm = st.number_input('Loan Term', min_value=0, max_value=500, value=0, step=1)
    chistory= st.number_input('Credit History', min_value=0, max_value=1, value=0, step=1)
    parea = st.radio("Property Area",('Rural','Urban'))
    submit =st.form_submit_button("Submit")
    if gender=='Male':
        gender=1
    else:
        gender=0
    if married=="Yes":
        married=1
    else:
        married=0
    if education=="Graduate":
        education=1
    else:
        education=0
    if selfempl=="Yes":
        selfempl=1
    else:
        selfempl=0
    if parea=="Urban":
        parea=1
    else:
        parea=0
                    

    outcome=''
    if submit:
        outcome= loanpred([gender,married,depen,education,selfempl,aincome,coaincome,lamount,lterm,chistory,parea])
        if outcome=='Loan Accepted':
            st.success(outcome)
        else:
            st.error(outcome)

