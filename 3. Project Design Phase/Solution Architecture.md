# Solution Architecture

```
┌─────────────────────┐
│   User (Applicant)   │
└──────────┬───────────┘
           │ Enters details
           ▼
┌─────────────────────────────┐
│   Streamlit Web Interface    │
└──────────┬───────────────────┘
           │ Input data
           ▼
┌─────────────────────────────┐
│   Data Preprocessing Layer   │
│  (cleaning, encoding, scaling)│
└──────────┬───────────────────┘
           │
           ▼
┌─────────────────────────────┐
│   Trained ML Model (.pkl)    │
│  XGBoost / Decision Tree     │
└──────────┬───────────────────┘
           │ Prediction
           ▼
┌─────────────────────────────┐
│   Result Displayed to User   │
│   (Approved / Rejected)      │
└─────────────────────────────┘
```

## Components
1. **Frontend/Deployment**: Streamlit Cloud — hosts the interactive web app
2. **Preprocessing Module**: Handles missing values, encoding of categorical variables, feature scaling
3. **Model Layer**: Pre-trained classification model, serialized and loaded at runtime
4. **Prediction Engine**: Generates and returns the approval decision instantly

## Live Deployment
🔗 https://creditcardapprovalprediction-hrzqcjzayrde7zffub5zxc.streamlit.app/
