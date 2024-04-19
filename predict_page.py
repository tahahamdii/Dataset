import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_modell.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

def predict_energy_usage(model, input_data):
    # Convert input data to numpy array
    input_array = np.array(input_data).reshape(1, -1)
    # Make prediction using the loaded model
    prediction = model.predict(input_array)
    return prediction

# Load the model and extract the regressor
data = load_model()
regressor_loaded = data["model"]

# Streamlit app
st.title('Energy Usage Prediction')

# Input fields
lagging_reactive_power = st.number_input('Lagging Current Reactive Power (kVarh)', min_value=0.0, value=3.0)
leading_reactive_power = st.number_input('Leading Current Reactive Power (kVarh)', min_value=0.0, value=3.5)
co2 = st.number_input('CO2', min_value=0.0, value=0.1)
lagging_power_factor = st.number_input('Lagging Current Power Factor', min_value=0.0, value=70.0)
leading_power_factor = st.number_input('Leading Current Power Factor', min_value=0.0, value=99.0)
nsm = st.number_input('NSM', min_value=0, value=5000)
weekend_status = st.selectbox('Weekend Status', ['Weekday', 'Weekend'])
day_of_week = st.selectbox('Day of Week', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
load_type = st.selectbox('Load Type', ['Maximum Load', 'Medium Load'])

# Encode categorical features
weekend_encoded = 1 if weekend_status == 'Weekend' else 0
day_of_week_encoded = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].index(day_of_week)
load_type_encoded = ['Maximum Load', 'Medium Load'].index(load_type)

# Make prediction when button is clicked
if st.button('Predict'):
    input_data = [lagging_reactive_power, leading_reactive_power, co2, lagging_power_factor, leading_power_factor,
                  nsm, weekend_encoded, *([0]*day_of_week_encoded), *([0]*(6-day_of_week_encoded)), load_type_encoded]
    prediction = predict_energy_usage(regressor_loaded, input_data)
    st.success(f'Predicted Energy Usage: {prediction[0]}')
