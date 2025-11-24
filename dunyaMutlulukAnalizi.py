import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn  as sns



df=pd.read_csv("datas.csv")
#df_new=df.pivot_table(index="Region",aggfunc="mean",values=["Happiness Score"])
#plt.plot(df_new)
#plt.grid()
#plt.title("Kıtaların Ortalama Mutluluk Skorları")
#plt.xlabel("Kıtalar")
#plt.ylabel("Mutluluk Skor Ortalamaları")
#plt.show()

x=df["Happiness Score"].mean()
df.loc[df["Happiness Score"]>x,"Category"]="Mutlu"
df.loc[df["Happiness Score"]<x,"Category"]="Mutsuz"
df.loc[df["Happiness Score"]==x,"Category"]="Ortalama"

df_mutsuz_on_ulke=df.sort_values("Happiness Score",axis=0,ascending=True,inplace=False).head(10)
df_mutlu_on_ulke=df.sort_values("Happiness Score",axis=0,ascending=False,inplace=False).head(10)






country_mutlu=df_mutlu_on_ulke["Country"]
happines_score_mutlu=df_mutlu_on_ulke["Happiness Score"]

plt.barh(country_mutlu,happines_score_mutlu,color="green")
plt.xlabel("Mutluluk  Skor Ortalamaları",color="grey")
plt.ylabel("Ülkeler",color="grey")
plt.title("En Mutlu On Ülke",color="grey")
plt.show()

country_mutsuz=df_mutsuz_on_ulke["Country"]
happiness_score_mutsuz=df_mutsuz_on_ulke["Happiness Score"]

plt.barh(country_mutsuz,happiness_score_mutsuz,color="red")
plt.title("En Mutsuz On Ülke",color="grey")
plt.xlabel("Mutluluk Skor Ortalamaları",color="grey")
plt.ylabel("Ülkeler",color="grey")
plt.show()


x=df["Economy (GDP per Capita)"]
y=df["Happiness Score"]
plt.scatter(x,y,marker="*",color="pink")
plt.ylabel("Happines Score",color="grey")
plt.xlabel("GDP",color="grey")
plt.title("Ekonomik Durum ve Mutluluk İlişkisi",color="grey")
plt.show()


a=df["Freedom"]
b=df["Happiness Score"]
plt.scatter(a,b,marker="*",color="violet")
plt.xlabel("Özgürlük Oranı",color="grey")
plt.ylabel("Mutluluk Oranı",color="grey")
plt.title("Özgürlük Oranı ve Mutluluk Skoru İlişkisi",color="grey")
plt.show()


d=df.corr(numeric_only=True)
sns.heatmap(d,cmap="RdYlBu",annot=True)
plt.show()

#print(df.style.background_gradient())



print(df.to_string())

#print(df.to_string())


