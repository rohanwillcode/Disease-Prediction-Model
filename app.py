import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved models
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# ===============================
# Diabetes Prediction Page
# ===============================
# ===============================
# Diabetes Prediction Page
# ===============================
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox("Gender", options=["Male", "Female"])

    with col2:
        Glucose = st.number_input('Glucose Level (mg/dL)', min_value=0.0, max_value=300.0)

    with col3:
        BloodPressure = st.number_input('Blood Pressure (mm Hg)', min_value=0.0, max_value=200.0)

    with col1:
        SkinThickness = st.number_input('Skin Thickness (mm)', min_value=0.0, max_value=100.0)

    with col2:
        Insulin = st.number_input('Insulin Level (mu U/ml)', min_value=0.0, max_value=900.0)

    with col3:
        BMI = st.number_input('BMI', min_value=0.0, max_value=70.0)

    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=3.0)

    with col2:
        Age = st.number_input('Age of the Person', min_value=1, max_value=120)

    # Conditional pregnancies input based on gender
    Pregnancies = 0
    if gender == "Female":
        with col3:
            Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20)

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is  likely to be diabetic'
        else:
            diab_diagnosis = 'The person is not likely to be  diabetic'
    st.success(diab_diagnosis)


# ===============================
# Heart Disease Prediction Page
# ===============================
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age', min_value=1, max_value=120)

    with col2:
        sex = st.selectbox('Sex (0 = Female, 1 = Male)', options=[0, 1])

    with col3:
        cp = st.selectbox('Chest Pain Type (0-3)', options=[0, 1, 2, 3])

    with col1:
        trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=80.0, max_value=200.0)

    with col2:
        chol = st.number_input('Serum Cholesterol (mg/dL)', min_value=100.0, max_value=600.0)

    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dL (1=True, 0=False)', options=[0, 1])

    with col1:
        restecg = st.selectbox('Resting ECG (0-2)', options=[0, 1, 2])

    with col2:
        thalach = st.number_input('Max Heart Rate Achieved', min_value=60.0, max_value=220.0)

    with col3:
        exang = st.selectbox('Exercise Induced Angina (1=True, 0=False)', options=[0, 1])

    with col1:
        oldpeak = st.number_input('ST depression', min_value=0.0, max_value=6.0)

    with col2:
        slope = st.selectbox('Slope of peak exercise ST segment (0-2)', options=[0, 1, 2])

    with col3:
        ca = st.selectbox('Number of major vessels (0-3)', options=[0, 1, 2, 3])

    with col1:
        thal = st.selectbox('Thalassemia (0 = normal; 1 = fixed defect; 2 = reversible)', options=[0, 1, 2])

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg,
                      thalach, exang, oldpeak, slope, ca, thal]
        heart_prediction = heart_disease_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person may have a heart disease'
        else:
            heart_diagnosis = 'The person may not have any heart disease'
    st.success(heart_diagnosis)

# ===============================
# Parkinson's Prediction Page
# ===============================
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    def num_input(label):
        return st.number_input(label, value=0.0)

    fo = num_input('MDVP:Fo(Hz)')
    fhi = num_input('MDVP:Fhi(Hz)')
    flo = num_input('MDVP:Flo(Hz)')
    Jitter_percent = num_input('MDVP:Jitter(%)')
    Jitter_Abs = num_input('MDVP:Jitter(Abs)')
    RAP = num_input('MDVP:RAP')
    PPQ = num_input('MDVP:PPQ')
    DDP = num_input('Jitter:DDP')
    Shimmer = num_input('MDVP:Shimmer')
    Shimmer_dB = num_input('MDVP:Shimmer(dB)')
    APQ3 = num_input('Shimmer:APQ3')
    APQ5 = num_input('Shimmer:APQ5')
    APQ = num_input('MDVP:APQ')
    DDA = num_input('Shimmer:DDA')
    NHR = num_input('NHR')
    HNR = num_input('HNR')
    RPDE = num_input('RPDE')
    DFA = num_input('DFA')
    spread1 = num_input('spread1')
    spread2 = num_input('spread2')
    D2 = num_input('D2')
    PPE = num_input('PPE')

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
                      Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR,
                      RPDE, DFA, spread1, spread2, D2, PPE]

        parkinsons_prediction = parkinsons_model.predict([user_input])
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
    st.success(parkinsons_diagnosis)

# ===============================
# Hide Streamlit elements
# ===============================
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
