import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error as rmse
from sklearn.metrics import mean_absolute_error as mae

df=pd.read_csv("datas.csv")

x=df[["Freedom","Economy (GDP per Capita)","Health (Life Expectancy)","Generosity"]]
y=df["Happiness Score"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)
y_tahmin=model.predict(x_test)

compare=pd.DataFrame({"g.happiness s.":y_test,"tahmin":y_tahmin})
print(compare)

#r2 ile performans ölçümü
score=r2_score(y_test,y_tahmin)
print("r2:",score)

#RMSE ile performans ölçümü
rmse=np.sqrt(rmse(y_test,y_tahmin))
print("rmse:",rmse)

#mae ile performans ölçümü
mae=mae(y_test,y_tahmin)
print("mae:",mae)





#print(df.to_string())