from pyexpat import model

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# ==========================================
# 1. LOAD THE DATASETS
# ==========================================
print("Loading datasets...")
# Adjust file paths if they are extracted into a specific folder
app_df = pd.read_csv("application_record.csv")
credit_df = pd.read_csv("credit_record.csv")

print(f"Application Record Shape: {app_df.shape}")
print(f"Credit Record Shape: {credit_df.shape}")

# ==========================================
# 2. DEFINE TARGET VARIABLE FROM CREDIT RECORD
# ==========================================
print("\nProcessing credit records to create target labels...")

# STATUS meanings: 
# 0: 1-29 days past due 
# 1: 30-59 days past due 
# 2: 60-89 days overdue 
# 3: 90-119 days overdue 
# 4: 120-149 days overdue 
# 5: Overdue or bad debts, write-offs 
# C: paid off that month 
# X: No loan for the month

# Define "Bad" users as anyone who has been 30+ days past due (Status 1, 2, 3, 4, 5)
credit_df['IS_BAD'] = credit_df['STATUS'].isin(['1', '2', '3', '4', '5']).astype(int)

# Group by ID and see if a customer was EVER "bad"
target_df = credit_df.groupby('ID')['IS_BAD'].max().reset_index()

print("Target variable distribution:")
print(target_df['IS_BAD'].value_counts(normalize=True))

# ==========================================
# 3. MERGE THE DATASETS
# ==========================================
print("\nMerging datasets...")
# Merge data on 'ID'
df = pd.merge(app_df, target_df, on='ID', how='inner')
print(f"Merged Data Shape: {df.shape}")

# Drop the ID column as it's just an identifier
df = df.drop(columns=['ID'])

# ==========================================
# 4. DATA PREPROCESSING & CLEANING
# ==========================================
print("\nPreprocessing data...")

# Handle Days columns (convert negative days to positive years/values for readability)
df['AGE'] = -df['DAYS_BIRTH'] / 365.25
df = df.drop(columns=['DAYS_BIRTH'])

# DAYS_EMPLOYED: positive values typically mean unemployed, negative means employed.
df['UNEMPLOYED'] = (df['DAYS_EMPLOYED'] > 0).astype(int)
df['YEARS_EMPLOYED'] = df['DAYS_EMPLOYED'].apply(lambda x: 0 if x > 0 else -x / 365.25)
df = df.drop(columns=['DAYS_EMPLOYED'])

# Fill missing values in OCCUPATION_TYPE
df['OCCUPATION_TYPE'] = df['OCCUPATION_TYPE'].fillna('Unknown')

# Define Feature types
categorical_cols = [
    'CODE_GENDER', 'FLAG_OWN_CAR', 'FLAG_OWN_REALTY', 'NAME_INCOME_TYPE',
    'NAME_EDUCATION_TYPE', 'NAME_FAMILY_STATUS', 'NAME_HOUSING_TYPE', 'OCCUPATION_TYPE'
]

numerical_cols = [
    'CNT_CHILDREN', 'AMT_INCOME_TOTAL', 'AGE', 'YEARS_EMPLOYED', 'CNT_FAM_MEMBERS'
]

# Binary / Flag columns that don't need scaling or encoding
passthrough_cols = ['FLAG_MOBIL', 'FLAG_WORK_PHONE', 'FLAG_PHONE', 'FLAG_EMAIL', 'UNEMPLOYED']

# Features (X) and Target (y)
X = df.drop(columns=['IS_BAD'])
y = df['IS_BAD']

# ==========================================
# 5. MACHINE LEARNING PIPELINE
# ==========================================
# Create preprocessing steps for numerical and categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore', drop='first'), categorical_cols)
    ],
    remainder='passthrough'
)

# Bundle preprocessing and model into a single pipeline
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=50, max_depth=10, class_weight='balanced', random_state=42))
])

# ==========================================
# 6. TRAIN-TEST SPLIT & MODEL TRAINING
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(f"Training set size: {X_train.shape[0]}")
print(f"Testing set size: {X_test.shape[0]}")

print("\nTraining the Random Forest Model...")
model_pipeline.fit(X_train, y_train)
print("Model training completed successfully!")

# ==========================================
# 7. EVALUATION
# ==========================================
print("\n================ EVALUATION METRICS ================")
y_pred = model_pipeline.predict(X_test)

print(f"Accuracy Score: {accuracy_score(y_test, y_pred):.4f}\n")

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

import joblib

# Save the trained model pipeline to a file
joblib.dump(model_pipeline, 'credit_model.pkl', compress=3)
print("\nModel saved successfully as 'credit_model.pkl'!")