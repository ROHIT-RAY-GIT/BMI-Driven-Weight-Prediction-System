# 📊 BMI Driven Weight Prediction System

This project aims to predict the **weight** of individuals based on their **height** and **gender** using **Linear Regression** models. The dataset used for this project contains height and weight data, split by gender into male and female groups. Two separate models were created for **male** and **female** weight prediction, ensuring better accuracy for both groups.

## 🚀 Features
- Predicts weight using height and gender as input features.
- Separate models for **male** and **female** predictions to account for different body compositions.
- Calculates and displays **BMI (Body Mass Index)** based on the predicted weight and input height.
- Visualizes the data distribution and regression results using **Seaborn** and **Matplotlib**.
- User-friendly **Streamlit Dashboard** for quick predictions.

## 🗂️ Dataset
The dataset used in this project is a modified version of the **weight-height** dataset. The weight is converted from pounds to kilograms, and height is converted from inches to centimeters for accurate analysis. The dataset contains the following columns:
- **Height** (in cm)
- **Weight** (in kg)
- **Gender** (Male/Female)

## 🛠️ Technologies Used

- Python for the core logic
- Pandas for data preprocessing
- Scikit-learn for model building
- Matplotlib and Seaborn for data visualization
- Streamlit for creating the web application

## 📈 Model Training and Evaluation
The **Linear Regression** models were trained separately on male and female datasets using **Scikit-learn**. The model performance is evaluated using **Root Mean Squared Error (RMSE)** and **R² Score** on both the training and testing datasets.

### Model Performance:
- **Male Model:**
  - RMSE (Train): 4.5404
  - RMSE (Test): 4.5234
  - R² Score (Train): 0.7434
  - R² Score (Test): 0.7500
- **Female Model:**
  - RMSE (Train): 4.5680
  - RMSE (Test): 4.5001
  - R² Score (Train): 0.7214
  - R² Score (Test): 0.7235

## 🎨 Data Visualization
We performed exploratory data analysis (EDA) to visualize the height and weight distributions for both males and females. The following plots were used:
- **Regression plots** for height vs. weight by gender.
- **Box plots** showing the distribution of height and weight.
- **KDE (Kernel Density Estimation) plots** for visualizing the distribution of height and weight for each gender.
  
### Sample Visualizations:

![Height and Weight Distribution with Gender](https://github.com/user-attachments/assets/77db62b1-c04f-497a-86f1-0046ac6f50b0)
![Data Visualization](https://github.com/user-attachments/assets/3f49bdfd-1b30-4411-b60d-a474dd1a7dbc)

## 💡 Body Mass Index (BMI) Calculation
In addition to predicting weight, this project also calculates the BMI based on the following formula:

BMI = Weight (kg) / (Height (m))²
The BMI value is used to categorize individuals into underweight, normal weight, overweight, and obese categories.


## 💾 Model Saving
Both male and female models were saved as .pkl files for future use:

- linear_regression_male_model.pkl
- linear_regression_female_model.pkl
These models can be loaded for making new predictions without retraining.

## 📊 Streamlit Dashboard

I created an interactive **Streamlit Dashboard** for users to input their height and gender and get a predicted weight. The dashboard also provides a BMI calculation based on the height and predicted weight.
## Streamlit Dashboard

You can interact with the **Weight Prediction App** directly via the Streamlit dashboard:

[Click here to check out the Streamlit Dashboard!](https://share.streamlit.io/your-streamlit-app-link)

The app allows users to input their height and gender to predict their weight using Linear Regression models trained separately for males and females.

## ✨ Future Improvements
- Include more features like age or other physical characteristics to improve the accuracy.
- Implement more complex models (e.g., Polynomial Regression, Neural Networks) for better predictions.

