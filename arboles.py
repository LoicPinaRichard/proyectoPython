from calendar import c
from matplotlib.colors import cnames
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from io import StringIO
from IPython.display import Image, display
import pydotplus 

sns.set()

test_df=pd.read_csv(r'M01-Introducción_al_Machine_Learning\M1U1-Introducción_al_big_data_y_ML\titanic-test_b6547a1c-55fe-4409-8e04-67b6678214a4.csv')
train_df=pd.read_csv(r'M01-Introducción_al_Machine_Learning\M1U1-Introducción_al_big_data_y_ML\titanic-train_4adcc656-193c-46d5-a978-f254fe4f0c22_e73b185d-1cb9-4af4-a668-da1ed47b97f2.csv')
"""print(train_df.head(5))"""
"""Label enconder sirve para limpiar y crear una prediccion correcta"""
label_enconder= preprocessing.LabelEncoder()
encoder_sec= label_enconder.fit_transform(train_df['Sex'])
print(train_df['Sex'])
train_df['Age'] = train_df['Age'].fillna(train_df['Age'].median())
train_df['Embarked']= train_df['Embarked'].fillna('S')
train_predictors=train_df.drop(['PassengerId','Survived','Name','Ticket','Cabin'],axis=1)
"""axis columnas y filas donde se aplica"""
categoria_cols=[cname for cname in train_predictors.columns if 
                    train_predictors[cname].nunique()< 10 and
                    train_predictors[cname].dtype=='object'
                ]
numericals_cols=[cname for cname in train_predictors.columns if
                    train_predictors[cname].dtype in ['int64','float64']
                ]
my_cols= categoria_cols + numericals_cols
train_predictors = train_predictors[my_cols]

dummy_encoded_train_predictors=pd.get_dummies(train_predictors)
train_df['Pclass'].value_counts()

y_target=train_df['Survived'].values
x_features_one= dummy_encoded_train_predictors.values

"""print(dummy_encoded_train_predictors)"""
x_train,x_validation,y_train,y_validation=train_test_split(x_features_one,y_target,test_size=.25,random_state=1)
tree_one=tree.DecisionTreeClassifier()
tree_one=tree_one.fit(x_features_one,y_target)
tree_one_acucuracy=round(tree_one.score(x_features_one,y_target),4)
print(tree_one_acucuracy)

