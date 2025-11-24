import pandas as pd



df=pd.read_csv("datas.csv")

Q1=df["Happiness Score"].quantile(0.25)
Q3=df["Happiness Score"].quantile(0.5)
Q4=df["Happiness Score"].quantile(0.75)

IQR=Q4-Q1

lower_limit=Q1-1.5*IQR
upper_limit=Q4+1.5*IQR

print("lower_limit:",lower_limit)
print("upper_limit:",upper_limit)

print("Q1:",Q1)
print("Q3:",Q3)

print(df["Happiness Score"].max())
print(df["Happiness Score"].min())



#df_outlier=df.dropna()

#df["zscore"]>3 | df["zscore"]<-3

#outlier temizliği yapabileceğim bir veri seti değil.