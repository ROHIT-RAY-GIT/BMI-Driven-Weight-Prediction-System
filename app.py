import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import base64

# Load the models
with open('linear_regression_female_model.pkl', 'rb') as file:
    lr_female = pickle.load(file)

with open('linear_regression_male_model.pkl', 'rb') as file:
    lr_male = pickle.load(file)

# Function to read and encode the image file
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

# Set the background image using CSS
def set_background(image_base64):
    page_bg_img = f"""
    <style>
    .stApp {{
        background: url("data:image/png;base64,{image_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white;  /* Default text color */
    }}
    /* Main content styling */
    .css-1g8v9l0 {{
        background: rgba(255, 255, 255, 0.8); /* Slightly transparent for better readability */
        padding: 20px; /* Padding for content */
        border-radius: 10px; /* Rounded corners */
    }}
    /* Set text color to black for all text elements */
    h1, h2, h3, h4, h5, h6, p, span, div, label, subheader {{
        color: white; /* Ensuring all text is white */
    }}
    .stButton > button {{
        background-color: #4C4C6D; /* Button color */
        color: white; /* Text color for button */
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
    }}
    .stButton > button:hover {{
        background-color: #6A5ACD; /* Button hover color */
        color: white;
    }}
    .stSlider > div {{
        background-color: transparent;
    }}
    /* Set text color of the select box to white */
    .stSelectbox div {{
        color: white; /* Set the text color to white */
    }}
    /* Set text color of the subheaders to white */
    .stSubheader {{
        color: white; /* Set the text color of subheaders to white */
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Call the function with the uploaded background image
image_base64 = get_base64_image("img7.jpg")  # Path to your uploaded image
set_background(image_base64)


# Load and preprocess the data
df = pd.read_csv('weight-height.csv')
df['Weight'] = df['Weight'] * 0.454
df['Height'] = df['Height'] * 2.54

# Streamlit app layout
st.markdown("<h1 style='text-align: center;'>BMI-Driven Weight Prediction System</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>This Machine Learning Model estimates your weight based on your height.</h3>", unsafe_allow_html=True)

# User input
gender = st.selectbox("Select your Gender", options=["Male", "Female"])
height_input = st.number_input("Enter your height in feet and inches (e.g., 5.5 for 5 feet 5 inches):", format="%.2f")

# Convert height from feet and inches to cm
if height_input > 0:
    height_cm = height_input * 30.48  # 1 foot = 30.48 cm
else:
    height_cm = 0

# Predict weight based on gender
if st.button("Predict Weight"):
    if gender == "Male":
        predicted_weight = lr_male.predict([[height_cm]])[0]  # Access the scalar value directly
    else:
        predicted_weight = lr_female.predict([[height_cm]])[0]  # Access the scalar value directly

    # Display the predicted weight
    st.success(f"Your predicted weight is {predicted_weight:.2f} kg.")
    
    # Optimal weight range based on BMI
    optimal_weight_range = (18.5 * (height_cm / 100) ** 2, 25 * (height_cm / 100) ** 2)
    st.write(f"The optimal weight for your height considering BMI between 18.5 and 25 is from {optimal_weight_range[0]:.2f} kg to {optimal_weight_range[1]:.2f} kg.")

# Dataset preview
st.subheader("Dataset Preview")
st.write(df.head())

# Height and Weight Scatter Plot
st.subheader("Height vs Weight Scatter Plot")
plt.figure(figsize=(10, 5))
sns.scatterplot(x='Height', y='Weight', hue='Gender', data=df)
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
st.pyplot(plt)
