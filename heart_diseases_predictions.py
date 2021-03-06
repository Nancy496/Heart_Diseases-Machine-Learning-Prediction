# -*- coding: utf-8 -*-
"""Heart_Diseases Predictions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RXqMak66YL1OmLCUgcAN63c0qx-X9F9X
"""

#import pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

# import the metrics class
from sklearn import metrics
from sklearn.model_selection import train_test_split

# import the class
from sklearn.linear_model import LogisticRegression
# load dataset
df = pd.read_csv("/content/heart_Diseases.csv", sep=',', na_values=".")
df.shape

df

# target and features
y = df.target 
x = df.drop(columns=['target'])

x.head()

y.head()

#4: Split into training and test set 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=42)

#5: Create and fit your model using KNeighbors classification for five neighbors (sklearn)
# KNN model fit
knn = KNeighborsClassifier(n_neighbors=5) 
knn.fit(x_train, y_train)

# Predict on dataset which model has not seen before 
predictions = knn.predict(x_test)
#predictions

#6: Calculate the model accuracy of the model accuracy
accuracy_score = metrics.accuracy_score(y_test, predictions)
print('Accuracy Score = ', round(accuracy_score,2))

confusion_matrix = pd.crosstab(y_test, predictions,rownames=['Actual'], colnames=['Predicted'])
print (confusion_matrix)
TN = confusion_matrix.iloc[0,0]
FN = confusion_matrix.iloc[0,1]
TP = confusion_matrix.iloc[1,1]
FP = confusion_matrix.iloc[1,0]

#8: Print the TN, FN, TP, FP values
print('True Negative =',TN)
print('False Negative =',FN)
print('True Positive =',TP)
print('False Positive =',FP)

# 9: Print the model precision value
# Precision is the ratio of  tp / (tp + fp)
myprecision = TP / (TP + FP)
print('Precision = ', round(myprecision,2))

#10: # Recall = the ratio tp / (tp + fn) 
myrecall = TP / (TP + FN)
print('Recall = ', round(myrecall,2))

#11: Visualize the confusion matrix with a Heatmap 
ax = plt.axes()
ax.set_title('Confusion Matrix with Heatmap')
sns.heatmap(confusion_matrix, annot=True)

#This is a list of rll, how often is the classifier correct?
#(TP+TN)/total = (100+50)/165 = 0.91
#Misclassificaates that are often computed from a 
#confusion matrix for a binary classifier:

#Accuracy: Overation Rate: Overall, how often is it wrong?
#(FP+FN)/total = (10+5)/165 = 0.09
#equivalent to 1 minus Accuracy
#also known as "Error Rate"
#True Positive Rate: When it's actually yes, how often does it predict yes?
#TP/actual yes = 100/105 = 0.95
#also known as "Sensitivity" or "Recall"
#False Positive Rate: When it's actually no, how often does it predict yes?
#FP/actual no = 10/60 = 0.17
#True Negative Rate: When it's actually no, how often does it predict no?
#TN/actual no = 50/60 = 0.83
#equivalent to 1 minus False Positive Rate
#also known as "Specificity"
#Precision: When it predicts yes, how often is it correct?
#TP/predicted yes = 100/110 = 0.91
#Prevalence: How often does the yes condition actually occur in our sample?
#actual yes/total = 105/165 = 0.64