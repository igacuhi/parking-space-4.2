import streamlit as st 
import pandas as pd
import numpy as np

# Function to simulate a prediction based on input features
def predict_parking_occupancy(features):
    # Dummy prediction for demonstration purposes
    occupancy_prediction = np.random.randint(0, 2)  # Predict either 0 or 1 for vacant or occupied
    return occupancy_prediction

def main():
    st.title('Parking Data Analysis')

    # Load parking data
    parking_data = pd.read_csv("Parking Data.csv")

    # Prediction area
    st.sidebar.title("Predict Parking Occupancy")

    # Sidebar input features
    property_type = st.sidebar.selectbox("Property Type", ["Office", "Residential", "Commercial"])
    building_status = st.sidebar.selectbox("Building Status", ["Active", "Decommissioned"])
    building_state = st.sidebar.selectbox("Building State", ["New York", "California", "Texas"])

    features = {
        "Property Type": property_type,
        "Building Status": building_status,
        "Building State": building_state
    }

    if st.sidebar.button("Predict"):
        # Call prediction function
        prediction = predict_parking_occupancy(features)

        # Display prediction
        st.write("### Prediction:")
        if prediction == 0:
            st.write("Parking space is likely vacant.")
        else:
            st.write("Parking space is likely occupied.")

if __name__ == "__main__":
    main()
