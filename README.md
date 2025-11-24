Dünya Mutluluk Analizi
1.	İş Anlama (Business Understanding)
Bu proje, ülkelerin mutluluk düzeylerini etkileyen faktörleri anlamayı ve  ülkeler arasındaki mutluluk skorlarını etkileyen faktörleri değerlendirmeyi ve görselleştirmeyi amaçlamaktadır. Hedef değişken “Happiness Score” olarak belirlenmiştir. Projenin başarı kriteri model tahmin doğruluk oranının yüksek olmasıdır.

2.	Veri Anlama (Data Understanding)
Veri seti, Dünya Mutluluk Raporu’ndan alınmıştır ve ülke bazında ekonomik göstergeler, özgürlük, yaşam desteği ve sosyal destek gibi değişkenleri içermektedir. Veri setinde boş (NaN) değer bulunmamaktadır. Veri setinde outlier değerlerin tespiti için z-score ve IQR yöntemi kullanılmış fakat her iki yöntemde de veri setinde outlier değer bulunamamıştır.

3.	Veri Hazırlama (Data Preparation)
Aykırı değerler z-score ve IQR yöntemleri ile tespit edilememiştir. Tüm değerler belirlenen alt ve üst limitler araasında kalmaktadır.

4.	Modelleme ve Değerlendirme (Modeling and Evaluation)
Multiple Linear Regression modeli kullanılmıştır. Hedef değişken "Happiness Score" olduğu için bağımlı değişken regresyon modelleri ile tahmin edilmiştir. Model performansları MAE, RMSE ve R² skorları ile değerlendirilmiştir.

5.	Dağıtım (Deployment)
Multiple Linear Regression modeli R² = 0.72, MAE = 0.5 olarak bulunmuştur. Random Forest Regressor modeli daha geniş ve aralarında daha karmaşık bir ilişki olan veri setleri için daha uygun olduğundan kullanılmamıştır. Model sonuçları iş hedefleri ile uyumludur ve ülkelerin mutluluk düzeylerini tahmin etmek için yeterlidir.
<img width="454" height="641" alt="image" src="https://github.com/user-attachments/assets/3a77c4f2-5169-4456-aed5-3746fae400e0" />
