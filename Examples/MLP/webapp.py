import joblib
import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from keras.layers import PReLU 

# --- Define the Model Artifacts and Categorical Orderings ---

# 1. Custom object for Keras (needed for loading models with custom layers)
custom_objects = {'PReLU': PReLU}

# 2. Define the logical order for ordered categorical features (for sorting dropdowns)
AGE_ORDER = [
    '0-10', '11-20', '21-30', '31-40', '41-50', 
    '51-60', '61-70', '71-80', '81-90', '91-100'
]

SEVERITY_ORDER = [
    'Minor', 'Moderate', 'Major', 'Extreme'
]

BED_GRADE_ORDER = [1.0, 2.0, 3.0, 4.0] 

# 3. Stay label mapping (assuming this is your model's target mapping)
STAY_MAPPING = {
    '0-10': 0, '11-20': 1, '21-30': 2, '31-40': 3, '41-50': 4, 
    '51-60': 5, '61-70': 6, '71-80': 7, '81-90': 8, '91-100': 9, 'More than 100 Days': 10
}
# Reverse mapping for output
STAY_LABEL = {v: k for k, v in STAY_MAPPING.items()}


# --- Artifact Loading Function (Cached) ---

@st.cache_resource
def load_artifacts():
    """
    Loads the saved Keras model (using the .h5 fix) and preprocessing ColumnTransformer.
    """
    try:
        # Load the model using the .h5 format fix
        model = tf.keras.models.load_model(
            'model.h5', 
            custom_objects=custom_objects,
            compile=False # Load only for inference
        )
        # Load the ColumnTransformer
        ct = joblib.load('column_transformer.joblib')
        return model, ct
    except Exception as e:
        # Display the error directly in the app
        st.error(f"Error loading model artifacts: {e}")
        return None, None

model, ct = load_artifacts()

if model is not None and ct is not None:
    
    st.title("🏥 Patient Stay Duration Predictor")
    st.markdown("Enter patient and hospital details to predict the length of stay.")

    # --- UI LAYOUT AND INPUTS (Sorted where applicable) ---
    
    col1, col2 = st.columns(2)

    # Column 1 Inputs
    with col1:
        # SORTED CATEGORICAL INPUTS
        age = st.selectbox("Age", options=AGE_ORDER)
        severity = st.selectbox("Severity of Illness", options=SEVERITY_ORDER)
        bed_grade = st.selectbox("Bed Grade", options=BED_GRADE_ORDER)
        
        # UNSORTED CATEGORICAL INPUTS (Adjust options as per your training data)
        hospital_type_code = st.selectbox("Hospital Type Code", options=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
        hospital_region_code = st.selectbox("Hospital Region Code", options=['X', 'Y', 'Z'])
        ward_type = st.selectbox("Ward Type", options=['R', 'S', 'Q', 'P', 'T', 'U'])
        ward_facility_code = st.selectbox("Ward Facility Code", options=['F', 'E', 'D', 'C', 'B', 'A'])
        department = st.selectbox("Department", options=['radiotherapy', 'anesthesia', 'gynecology', 'TB & Chest disease', 'surgery'])



    # Column 2 Inputs
    with col2:
        # Unsorted Categorical Inputs
        admission_type = st.selectbox("Type of Admission", options=['Emergency', 'Trauma', 'Urgent'])
        
        # Numerical Inputs
        available_rooms = st.number_input("Available Extra Rooms in Hospital", min_value=1, value=3, step=1)
        admission_deposit = st.number_input("Admission Deposit", min_value=0.0, value=4000.0, step=0.1)

        # Codes (Adjust values as per your training data)
        hospital_code = st.number_input("Hospital Code", min_value=1, value=8, step=1)
        city_code_hospital = st.number_input("City Code Hospital", min_value=1, value=3, step=1)
        
        # Patient ID/City Codes - included for completeness
        patientid = st.number_input("Patient ID", min_value=1, value=31397, step=1)
        city_code_patient = st.number_input("City Code Patient", min_value=1.0, value=7.0, step=1.0)

        # Numerical Input
        visitors = st.number_input("Visitors with Patient", min_value=0, value=2, step=1)


    # --- Prediction Logic (Display in the same window) ---
    if st.button("Predict Stay"):
        
        # 1. Create a DataFrame from inputs
        input_data = pd.DataFrame({
            'Hospital_code': [hospital_code],
            'Hospital_type_code': [hospital_type_code],
            'City_Code_Hospital': [city_code_hospital],
            'Hospital_region_code': [hospital_region_code],
            'Available Extra Rooms in Hospital': [available_rooms],
            'Department': [department],
            'Ward_Type': [ward_type],
            'Ward_Facility_Code': [ward_facility_code],
            'Bed Grade': [bed_grade],
            'patientid': [patientid],
            'City_Code_Patient': [city_code_patient],
            'Type of Admission': [admission_type],
            'Severity of Illness': [severity],
            'Visitors with Patient': [visitors],
            'Age': [age],
            'Admission_Deposit': [admission_deposit]
        })

        # 2. Preprocess the input data
        try:
            processed_data = ct.transform(input_data)
        except Exception as e:
            st.error(f"Error during preprocessing: {e}. Please check input values.")

        # 3. Make Prediction
        with st.spinner("Calculating prediction..."):
            prediction_proba = model.predict(processed_data)
            
            # Get the index of the class with the highest probability
            predicted_class_index = np.argmax(prediction_proba, axis=1)[0]
            
            # Get the label
            predicted_stay_label = STAY_LABEL.get(predicted_class_index, "Unknown Stay Duration")

        # 4. Display Prediction (Combined Output)
        st.subheader("🎉 Prediction Result")
        st.success(f"The predicted length of stay is: **{predicted_stay_label}**")

        # Add a Bar Chart for Visualization
            
        
        # Sort by Stay Duration (for a cleaner-looking bar chart order)
        # Note: We create a list of stay labels that matches the index order (0 to 10)
        # to ensure the bar chart's x-axis is sequential.
        st.markdown("---")
        st.subheader("Probability Distribution")
        stay_order_list = [STAY_LABEL[i] for i in range(len(STAY_LABEL))]
        proba_df = pd.DataFrame(
            prediction_proba[0], 
            index=list(STAY_LABEL.values()), 
            columns=['Probability']
        )
        proba_df = proba_df.sort_values(by='Probability', ascending=False)       
        proba_df_display = proba_df.reindex(stay_order_list)

        st.bar_chart(proba_df_display, use_container_width=True)

        # Optional: Show all probabilities for transparency
        st.markdown("---")
        st.subheader("Detailed Class Probabilities:")
        
        # Create a DataFrame for display, sorted by probability (descending)

        st.dataframe(proba_df, use_container_width=True)


else:
    st.error("Model or Column Transformer could not be loaded. Please ensure 'model.h5' and 'column_transformer.joblib' are in the same directory.")