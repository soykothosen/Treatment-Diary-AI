import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Step 1: Create Expanded Dataset
data = {
    "Disease": ["Flu", "Flu", "Hypertension", "Hypertension", "Diabetes", "Diabetes", "Migraine", "Migraine", 
                "Hypertension", "Flu", "Migraine", "Diabetes"],
    "Medicine": ["Paracetamol", "Ibuprofen", "Amlodipine", "Losartan", "Metformin", "Gliclazide", 
                 "Sumatriptan", "Ergotamine", "Losartan", "Aspirin", "Ibuprofen", "Metformin"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Encode Categorical Variables
df['Disease_Encoded'] = df['Disease'].astype('category').cat.codes
df['Medicine_Encoded'] = df['Medicine'].astype('category').cat.codes

# Features and Labels
X = df[['Disease_Encoded']]
y = df['Medicine_Encoded']

# Step 2: Split Data without Stratification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train Random Forest Model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Step 4: Make Predictions
y_pred = rf_model.predict(X_test)

# Step 5: Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Step 6: Predict Medicines for New Diseases
new_diseases = ["Flu", "Diabetes"]
new_diseases_encoded = [df['Disease'].astype('category').cat.categories.get_loc(d) for d in new_diseases]

# Create a DataFrame for Predictions with Correct Column Names
new_diseases_df = pd.DataFrame(new_diseases_encoded, columns=["Disease_Encoded"])
predictions = rf_model.predict(new_diseases_df)

# Decode Predictions to Medicine Names
medicine_predictions = [df['Medicine'].astype('category').cat.categories[p] for p in predictions]
for disease, medicine in zip(new_diseases, medicine_predictions):
    print(f"Disease: {disease}, Predicted Medicine: {medicine}")
