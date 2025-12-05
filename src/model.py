import sklearn 

from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix

def train_model(model, X_train, y_train):
    """Fit any scikit-learn model and return it."""
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test, model_name="Model"):
    """Print evaluation metrics and return predictions."""
    y_pred = model.predict(X_test)
    metrics = {
        "classification_report": classification_report(y_test, y_pred, output_dict=True),
        "roc_auc": roc_auc_score(y_test, model.predict_proba(X_test)[:,1]),
        "confusion_matrix": confusion_matrix(y_test, y_pred).tolist()
    }
    
    print(f"{model_name} Evaluation:")
    print(classification_report(y_test, y_pred))
    print("ROC-AUC:", metrics["roc_auc"])
    
    return y_pred, metrics
