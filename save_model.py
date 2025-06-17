
import pandas as pd
import joblib
from xgboost import XGBClassifier

# Load cleaned data
df = pd.read_csv('data/cleaned_churn.csv')

# Split features and target
X = df.drop('Churn', axis=1)
y = df['Churn']

# Train XGBoost model
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X, y)

# Save model to 'models/' folder
joblib.dump(model, 'models/churn_model.pkl')

print("✅ Model saved as models/churn_model.pkl")
