# Data Flow Diagram (DFD)

## Level 0 — Context Diagram
Applicant → [Credit Card Approval Prediction System] → Approval/Rejection Result

## Level 1 — Detailed Flow

1. **Input**: Applicant submits data (income, employment status, family size, housing type, credit history length, etc.) via the Streamlit web interface.
2. **Preprocessing**: Raw input is cleaned, missing values handled, categorical features encoded.
3. **Feature Engineering**: Relevant features are selected/transformed to match model training format.
4. **Model Inference**: Preprocessed data is passed to the trained ML model (XGBoost / Decision Tree, loaded from the saved `.pkl` file).
5. **Prediction**: Model outputs Approved / Rejected along with confidence score.
6. **Output**: Result displayed to the applicant instantly on the Streamlit app.

```
[Applicant Input] → [Preprocessing] → [Feature Engineering] → [Trained Model (.pkl)] → [Prediction Output] → [Streamlit UI]
```
