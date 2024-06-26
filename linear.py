import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

from google.colab import files
uploaded = files.upload()

bas_beyin = pd.read_csv("bas_beyin.csv")
bas_beyin.head()

plt.figure(figsize=(6,6))
heatmap=sns.heatmap(bas_beyin.corr(),vmin=-1,vmax=1,annot= True)
heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=12);

X = bas_beyin['Bas_cevresi(cm^3)'].values  # Bağımsız Değişken
y= bas_beyin['Beyin_agirligi(gr)'].values  # Bağımlı Değişken
print(X.shape)                                 # X SHAPE  kaçtane olduğuna bakar
print(type(X))

uzunluk = len(X)
X = X.reshape((uzunluk,1))      # DİZİYİ 2BOYUTLU YAPIYORUZ            DİZİ TEK BOYUTLU İSE 2 BOYUTLU YAPIYORUZ
print(X.shape)
print(type(X))

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state=42)

y_pred = modelRegresyon.predict(X_test)


from sklearn.linear_model import LinearRegression
modelRegresyon = LinearRegression()
modelRegresyon.fit(X_train,y_train)           #FİT UYDUR DEMEK        MODELİ EĞİTMEYE YARAR

plt.scatter(X_train,y_train,color = "red")
plt.plot(X_train, modelRegresyon.predict(X_train), color = 'blue')
plt.title("Başın Çevre Uzunluğu  Ve Beyin Ağırlığı Eğitim Veri Seti")
plt.xlabel("Başın Çevre Uzunluğu cm^3")
plt.ylabel("Beyin Ağırlığı(gram)")
plt.show()


plt.scatter(X_test,y_test,color="green")
plt.plot(X_test,modelRegresyon.predict(X_test),color="blue")
plt.title("Başın Çevre Uzunluğu  Ve Beyin Ağırlığı Test Veri Seti")
plt.xlabel('Başın Çevre Uzunluğu (cm^3)')
plt.ylabel('Beyin Ağırlığı(gram)')
plt.show()

print('Eğim(Q1):', modelRegresyon.coef_)                                       # Bu, lineer regresyon modelinin eğim katsayısını temsil eder.
print('Kesen(Q0):', modelRegresyon.intercept_)                                 #Bu, lineer regresyon modelinin kesim noktası katsayısını temsil eder
print("y=%0.2f"%modelRegresyon.coef_+"x+%0.2f"%modelRegresyon.intercept_)    # Y = BX+C GİBİ

from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error
from sklearn.metrics import median_absolute_error, r2_score

print("R-Kare: ", r2_score(y_test, y_pred))
print("MAE: ", mean_absolute_error(y_test, y_pred))
print("MSE: ", mean_squared_error(y_test, y_pred))           # DOĞRULUK ORANLARINI ÖLÇMEYE YARAR
print("MedAE: ", median_absolute_error(y_test, y_pred))
print("EVS: ", explained_variance_score(y_test, y_pred))