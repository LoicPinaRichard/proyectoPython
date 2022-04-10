import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset= pd.read_csv(r'C:\Users\loicp\OneDrive\Documentos\GitHub\Machine-Learning\M01-Introducción_al_Machine_Learning\M1U1-Introducción_al_big_data_y_ML\salarios_32849f3e-7f53-4139-b334-b8de8beb144a.csv')
print(dataset.head(5))
print(dataset.shape)
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values
print(x)
print(y)
"""no se como saca la x de xtrain"""
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=0)
print(x_train)
regressor= LinearRegression()
regressor.fit(x_train,y_train)
vis_train=plt
vis_train.scatter(x_train,y_train, color='blue')
vis_train.plot(x_train,regressor.predict(x_train), color='black')
vis_train.title("salario vs exp")
vis_train.xlabel('exp')
vis_train.ylabel('salario')
vis_train.show()

vis_train=plt
vis_train.scatter(x_test,y_test, color='red')
vis_train.plot(x_train,regressor.predict(x_train), color='black')
vis_train.title("salario vs exp")
vis_train.xlabel('exp')
vis_train.ylabel('salario')
vis_train.show()

regressor.score(x_test,y_test)