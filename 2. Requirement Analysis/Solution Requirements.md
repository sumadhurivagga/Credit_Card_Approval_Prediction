# Solution Requirements

## Functional Requirements
- FR1: System shall accept applicant details as input (income, age, employment, family size, housing, credit history, etc.)
- FR2: System shall preprocess and validate input data
- FR3: System shall predict credit card approval status using a trained ML model
- FR4: System shall display the prediction result (Approved/Rejected) to the user in real time
- FR5: System shall be accessible via a web browser (deployed app)

## Non-Functional Requirements
- NFR1: Prediction response time should be under 2–3 seconds
- NFR2: System should have an intuitive, easy-to-use UI
- NFR3: Model should maintain consistent accuracy on unseen data
- NFR4: Application should be deployed and publicly accessible (Streamlit Cloud)
- NFR5: Codebase should be modular and reusable

## Technical Requirements
- Python 3.x environment
- Trained and serialized ML model (.pkl)
- Streamlit for front-end/deployment
- GitHub for version control
