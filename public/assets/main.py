import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
import pickle

# Load the dataset
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Preprocess the data
def preprocess_data(data):
    # Convert categorical variables to numerical variables
    data['category'] = data['category'].astype('category').cat.codes

    # Split the data into features and target
    X = data.drop('target', axis=1)
    y = data['target']

    return X, y

# Train a logistic regression model
def train_logistic_regression(X_train, y_train):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model

# Train a random forest model
def train_random_forest(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    matrix = confusion_matrix(y_test, y_pred)
    return accuracy, report, matrix

# Train and evaluate the models
def main():
    file_path = 'data.csv'
    data = load_data(file_path)
    X, y = preprocess_data(data)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train and evaluate logistic regression model
    model_lr = train_logistic_regression(X_train, y_train)
    accuracy_lr, report_lr, matrix_lr = evaluate_model(model_lr, X_test, y_test)
    print(f'Logistic Regression Model Accuracy: {accuracy_lr:.3f}')

    # Train and evaluate random forest model
    model_rf = train_random_forest(X_train, y_train)
    accuracy_rf, report_rf, matrix_rf = evaluate_model(model_rf, X_test, y_test)
    print(f'Random Forest Model Accuracy: {accuracy_rf:.3f}')

    # Save the models to a file
    with open('models.pkl', 'wb') as f:
        pickle.dump(model_lr, f)
        pickle.dump(model_rf, f)

if __name__ == '__main__':
    main()