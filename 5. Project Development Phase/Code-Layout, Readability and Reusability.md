# Code Layout, Readability and Reusability

## Repository Structure
```
├── 1. Brainstorming & Ideation/
├── 2. Requirement Analysis/
├── 3. Project Design Phase/
├── 4. Project Planning Phase/
├── 5. Project Development Phase/
├── 6. Project Testing/
├── 7. Project Documentation/
├── 8. Project Demonstration/
├── app.py                # Streamlit application
├── credit_card_model.pkl # Trained ML model
├── predict.py            # Prediction logic
├── requirements.txt
└── README.md
```

## Coding Standards Followed
- Meaningful variable and function names (e.g. `preprocess_input()`, `predict_approval()`)
- Modular design — preprocessing, model loading, and prediction logic kept in separate functions
- Comments added for key logic blocks
- Consistent PEP8-style formatting

## Reusability
- Preprocessing pipeline can be reused for retraining with new data
- Model loading and prediction functions are decoupled from the UI layer, making it easy to swap models or reuse logic in another interface (e.g. API)
