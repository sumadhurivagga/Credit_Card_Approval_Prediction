# Coding & Solution

## Development Approach
1. **Data Preprocessing**: Handled missing values, encoded categorical variables (Label/One-Hot Encoding), scaled numerical features
2. **Model Training**: Trained multiple classification models (Logistic Regression, Decision Tree, XGBoost) using Scikit-Learn and XGBoost libraries
3. **Model Selection**: Compared models on accuracy, precision, recall, and F1-score; selected the best-performing one
4. **Model Serialization**: Saved the final trained model as a `.pkl` file using pickle
5. **App Development**: Built an interactive UI using Streamlit where users input applicant details and get an instant prediction
6. **Deployment**: Deployed the app on Streamlit Cloud for public access

## Key Solution Highlights
- End-to-end pipeline from raw data to live prediction
- Real-time inference with sub-second response
- Simple, guided input form for non-technical users
