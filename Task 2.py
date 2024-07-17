#!/usr/bin/env python
# coding: utf-8

# Reason for Choosing Algorithms:
# RandomForestClassifier: It is robust, handles high-dimensional data well, and provides good accuracy with less tuning.
# SVM: Effective in high-dimensional spaces and versatile with different kernel functions.
# KNN: Simple and effective for smaller datasets and non-linear data.

# In[2]:


from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# Load the data
train_df = pd.read_excel("C:\\Users\\USER\\Downloads\\train.xlsx")
test_df = pd.read_excel("C:\\Users\\USER\\Downloads\\test.xlsx")

# Separate features and target for training
X_train = train_df.drop(columns=['target'])
y_train = train_df['target']

# Separate features for testing
X_test = test_df.copy()

# Initialize the models
rf_classifier = RandomForestClassifier(random_state=42)
svm_classifier = SVC(probability=True, random_state=42)
knn_classifier = KNeighborsClassifier()

# Train the models
rf_classifier.fit(X_train, y_train)
svm_classifier.fit(X_train, y_train)
knn_classifier.fit(X_train, y_train)

# Predict on the test data
rf_test_predictions = rf_classifier.predict(X_test)
svm_test_predictions = svm_classifier.predict(X_test)
knn_test_predictions = knn_classifier.predict(X_test)

# Calculate train accuracy
rf_train_accuracy = accuracy_score(y_train, rf_classifier.predict(X_train))
svm_train_accuracy = accuracy_score(y_train, svm_classifier.predict(X_train))
knn_train_accuracy = accuracy_score(y_train, knn_classifier.predict(X_train))

# Display the train accuracy and the test predictions
{
    "RandomForestClassifier": {
        "train_accuracy": rf_train_accuracy,
        "test_predictions": rf_test_predictions.tolist()
    },
    "SVM": {
        "train_accuracy": svm_train_accuracy,
        "test_predictions": svm_test_predictions.tolist()
    },
    "KNN": {
        "train_accuracy": knn_train_accuracy,
        "test_predictions": knn_test_predictions.tolist()
    }
}


# In[ ]:




