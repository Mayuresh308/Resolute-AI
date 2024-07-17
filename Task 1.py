#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas scikit-learn


# In[2]:


import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Load the data
train_df = pd.read_excel("C:\\Users\\USER\\Downloads\\train.xlsx")
test_df = pd.read_excel("C:\\Users\\USER\\Downloads\\test.xlsx")

# Separate features and target
X_train = train_df.drop(columns=['target'])

# Apply K-Means clustering
kmeans = KMeans(n_clusters=5, random_state=42)  # Assuming 5 clusters
kmeans.fit(X_train)

# Function to predict the cluster of a given data point
def predict_cluster(data_point):
    cluster = kmeans.predict(np.array(data_point).reshape(1, -1))
    return cluster[0]

# Function to explain why a data point belongs to a specific cluster
def explain_cluster_assignment(data_point, kmeans):
    distances = kmeans.transform(np.array(data_point).reshape(1, -1))
    closest_cluster = np.argmin(distances)
    explanation = {
        "data_point": data_point,
        "assigned_cluster": closest_cluster,
        "distances_to_centroids": distances[0].tolist()
    }
    return explanation

# Example explanation for the first data point in the test set
test_data_point = test_df.iloc[0].tolist()
explanation = explain_cluster_assignment(test_data_point, kmeans)

# Display the explanation
print(explanation)


# In[ ]:




