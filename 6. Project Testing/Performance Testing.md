# Performance Testing

## Model Performance Metrics

| Metric | Score |
|---|---|
| Accuracy | [Add score from your model evaluation] |
| Precision | [Add score] |
| Recall | [Add score] |
| F1-Score | [Add score] |

## Testing Approach
- **Train-Test Split**: Data split into training and testing sets to evaluate generalization
- **Cross-Validation**: Used to ensure model stability across different data splits
- **Confusion Matrix**: Analyzed to check false positives/negatives (wrongly approved/rejected applicants)

## Application Performance Testing
| Test Case | Expected Result | Status |
|---|---|---|
| Submit valid applicant data | Correct prediction displayed instantly | ✅ Pass |
| Submit incomplete data | Validation message shown | ✅ Pass |
| App load time | Loads within acceptable time on Streamlit Cloud | ✅ Pass |
| Prediction response time | Under 2–3 seconds | ✅ Pass |

*(Fill in exact accuracy/precision/recall/F1 values from your model's evaluation results.)*
