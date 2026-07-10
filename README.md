# SmartBridge Credit Approval App

A Streamlit app for predicting credit approval using a trained Random Forest model.

## Files
- `app.py`: Streamlit application that loads `credit_model.pkl` and collects user input.
- `predict.py`: Training script that builds the model and saves `credit_model.pkl`.
- `credit_model.pkl`: Binary model artifact (ignored from git by default).
- `application_record.csv`, `credit_record.csv`: Dataset files used by `predict.py`.
- `requirements.txt`: Python dependencies.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Train and save the model:
   ```bash
   python predict.py
   ```
4. Run the Streamlit app locally:
   ```bash
   streamlit run app.py
   ```

## Deploy to Streamlit Cloud

1. Go to https://streamlit.io/cloud and sign in with GitHub.
2. Click **New app** and choose your repository:
   - Owner: `sumadhurivagga`
   - Repository: `Credit_Card_Approval_Prediction`
   - Branch: `main`
   - File path: `app.py`
3. Click **Deploy**.
4. After deployment completes, Streamlit will provide a live web app URL.

## Notes

- The model file `credit_model.pkl` is excluded from Git by `.gitignore` because binary files are better stored separately.
- If you want to publish the app to GitHub, commit the code and push using your own remote repository.
