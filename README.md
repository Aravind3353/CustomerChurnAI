# 📉 Customer Churn Prediction

This is a machine learning project to predict customer churn using real-world telecom data. It includes end-to-end steps from data cleaning and model training to a Streamlit-based prediction app.

## 🧠 Project Objective

To build a predictive model that identifies whether a customer is likely to churn (leave) based on their contract, usage, and service information.

## 📊 Dataset

- **Source**: [IBM Sample Telco Customer Churn Dataset](https://www.ibm.com/communities/analytics/watson-analytics-blog/guide-to-sample-datasets/)
- File used: `WA_Fn-UseC_-Telco-Customer-Churn.csv`
- Location: `data/` folder

## 🛠 Technologies Used

- **Python 3**
- **Pandas** & **NumPy** – Data wrangling
- **Matplotlib** & **Seaborn** – Visualization
- **Scikit-learn** – Model building (Logistic Regression, Random Forest)
- **XGBoost** – Gradient boosting model
- **Joblib** – Model serialization
- **Streamlit** – App interface

## 🚀 How to Run the Project Locally
To run this project, please follow the steps below to create your own Python environment:

**1. Clone the repository**
bash:

git clone https://github.com/Aravind3353/CustomerChurnAI.git
cd CustomerChurnAI

**2. Create a virtual environment**
Using venv (built-in with Python 3.6+):

bash:

python -m venv venv
source venv/bin/activate     # On Windows use: venv\Scripts\activate
Or using conda (if you prefer):

bash:

conda create --name myenv python=3.9
conda activate myenv

**3. Install the dependencies manually**
You can install the main libraries individually:

bash:

pip install streamlit pandas numpy scikit-learn pillow
💡 If you run into issues with pillow, try installing a version below 10.0:

bash:

pip install "pillow<10"

**4. Run the Streamlit app**
bash

streamlit run app.py
📁 Make sure you're in the correct directory where app.py is located.

**🛠 Recommended Python Version**
Python 3.8 to 3.10

Avoid Python 3.11+ if you experience dependency conflicts.
