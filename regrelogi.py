from random import random
from sre_constants import IN_LOC_IGNORE
from django.forms import inlineformset_factory
import matplotlib
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns 

diabetes= pd.read_csv(r"M01-Introducción_al_Machine_Learning\M1U1-Introducción_al_big_data_y_ML\diabetes_e5df1a05-5634-44ce-91df-7bc6143aa93e.csv")
"""print(diabetes.head(5))"""
"""print(diabetes.shape)"""
loadCols=['Pregnancies','Insulin','BMI','Age','Glucose','BloodPressure','DiabetesPedigreeFunction']
x= diabetes[loadCols]
"""print(x)"""
y=diabetes.Outcome
"""print(y)"""
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
logi=LogisticRegression()
logi.fit(x_train,y_train)
y_pred=logi.predict(x_test)
"""Tiene diabetes?"""
"""print(y_pred)"""

