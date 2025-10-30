import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import joblib

# --- 1. LOAD ARTIFACTS AND CONFIG ---

# Use caching for resources to load them only once
@st.cache_resource
def load_artifacts():
    """
    Loads the saved model and preprocessing transformer.
    """
    # Load the Keras model
    # Note: You might need to provide custom_objects if your PReLU isn't standard
    model = tf.keras.models.load_model(
        'model.h5'
    )
    # Load the ColumnTransformer
    ct = joblib.load('column_transformer.joblib')
    
    return model, ct

# Load the model and transformer
model, ct = load_artifacts()

# Define the class mapping from your notebook (cell 56)
STAY_CLASSES = {
    0: '0-10',
    1: '11-20',
    2: '21-30',
    3: '31-40',
    4: '41-50',
    5: '51-60',
    6: '61-70',
    7: '71-80',
    8: '81-90',
    9: '91-100',
    10: 'More than 100 Days'
}

# Define the exact feature order from your training (cell 44)
FEATURE_ORDER = [
    'Hospital_code', 'Hospital_type_code', 'City_Code_Hospital', 
    'Hospital_region_code', 'Available Extra Rooms in Hospital', 'Department', 
    'Ward_Type', 'Ward_Facility_Code', 'Bed Grade', 'City_Code_Patient', 
    'Type of Admission', 'Severity of Illness', 'Visitors with Patient', 'Age', 
    'Admission_Deposit'
]

# --- 2. BUILD THE USER INTERFACE (UI) ---

st.set_page_config(page_title="Patient Stay Prediction", layout="wide")
st.title('🏥 Patient Stay Duration Predictor')
st.markdown("Enter the patient's details on the left to predict their length of stay.")

# Use a sidebar for inputs
st.sidebar.header("Enter Patient Admission Details")

# Create columns for a cleaner layout in the sidebar
col1, col2 = st.sidebar.columns(2)

# --- Column 1 Inputs ---
with col1:
    age = st.selectbox(
        'Age', 
        options=['31-40', '41-50', '51-60', '21-30', '71-80', '61-70', '11-20', '81-90', '0-10', '91-100'],
        index=0
    )
    severity_of_illness = st.selectbox(
        'Severity of Illness', 
        options=['Moderate', 'Minor', 'Extreme'],
        index=0
    )
    type_of_admission = st.selectbox(
        'Type of Admission', 
        options=['Trauma', 'Emergency', 'Urgent'],
        index=0
    )
    department = st.selectbox(
        'Department', 
        options=['gynecology', 'anesthesia', 'radiotherapy', 'TB & Chest disease', 'surgery'],
        index=0
    )
    bed_grade = st.selectbox(
        'Bed Grade', 
        options=[2, 3, 4, 1],
        index=0
    )
    hospital_code = st.selectbox(
        'Hospital Code', 
        options=[26, 23, 19, 6, 11, 28, 14, 27, 9, 12, 29, 32, 25, 10, 15, 21, 24, 3, 17, 1, 13, 5, 2, 30, 22, 31, 16, 8, 18, 20, 7, 4],
        index=0
    )
    hospital_type_code = st.selectbox(
        'Hospital Type Code', 
        options=['a', 'b', 'c', 'e', 'd', 'f', 'g'],
        index=0
    )
    
# --- Column 2 Inputs ---
with col2:
    admission_deposit = st.number_input(
        'Admission Deposit', 
        min_value=0.0, 
        max_value=12000.0, 
        value=4500.0, 
        step=100.0
    )
    visitors_with_patient = st.number_input(
        'Visitors with Patient', 
        min_value=0, 
        max_value=40, 
        value=2, 
        step=1
    )
    city_code_patient = st.selectbox(
        'City Code (Patient)', 
        options=[8, 2, 1, 7, 5, 4, 9, 15, 10, 6, 12, 3, 23, 14, 16, 13, 21, 20, 18, 19, 26, 25, 27, 11, 28, 22, 24, 30, 29, 33, 31, 37, 32, 34, 35, 36, 38],
        index=0
    )
    ward_type = st.selectbox(
        'Ward Type', 
        options=['R', 'Q', 'S', 'P', 'T', 'U'],
        index=0
    )
    ward_facility_code = st.selectbox(
        'Ward Facility Code', 
        options=['F', 'E', 'D', 'C', 'B', 'A'],
        index=0
    )
    city_code_hospital = st.selectbox(
        'City Code (Hospital)', 
        options=[1, 2, 6, 7, 3, 5, 9, 11, 4, 10, 13],
        index=0
    )
    hospital_region_code = st.selectbox(
        'Hospital Region Code', 
        options=['X', 'Y', 'Z'],
        index=0
    )

# This input is not in col1 or col2 to span the full sidebar width
available_extra_rooms = st.number_input(
    'Available Extra Rooms in Hospital', 
    min_value=0, 
    max_value=25, 
    value=3, 
    step=1
)


# --- 3. PREDICTION LOGIC ---

# Create a button to trigger the prediction
if st.sidebar.button('Predict Stay Duration', use_container_width=True):
    
    # 1. Collect inputs into a dictionary
    input_data = {
        'Hospital_code': hospital_code,
        'Hospital_type_code': hospital_type_code,
        'City_Code_Hospital': city_code_hospital,
        'Hospital_region_code': hospital_region_code,
        'Available Extra Rooms in Hospital': available_extra_rooms,
        'Department': department,
        'Ward_Type': ward_type,
        'Ward_Facility_Code': ward_facility_code,
        'Bed Grade': float(bed_grade), # Match training data type
        'City_Code_Patient': float(city_code_patient), # Match training data type
        'Type of Admission': type_of_admission,
        'Severity of Illness': severity_of_illness,
        'Visitors with Patient': visitors_with_patient,
        'Age': age,
        'Admission_Deposit': admission_deposit
    }
    
    # 2. Convert to DataFrame in the correct order
    input_df = pd.DataFrame([input_data])
    input_df = input_df[FEATURE_ORDER]

    # 3. Transform the data using the loaded ColumnTransformer
    # The 'ct' object already knows which columns to OneHotEncode, 
    # which to scale, and which to pass through.
    try:
        transformed_data = ct.transform(input_df)
        
        # 4. Make prediction
        prediction_proba = model.predict(transformed_data)
        
        # 5. Post-process the prediction
        prediction_index = np.argmax(prediction_proba, axis=-1)[0]
        prediction_label = STAY_CLASSES[prediction_index]

        # 6. Display the result
        st.success(f"**Predicted Stay Duration:** `{prediction_label}` days")

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")