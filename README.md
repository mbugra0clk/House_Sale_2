# House Sales 2

Bu proje, ev satış fiyatlarını görselleştirmek için **Folium** kütüphanesini kullanarak interaktif haritalar oluşturur.

## 📌 Proje Açıklaması

Python kullanarak ev satış fiyatlarını analiz eder ve en pahalı 5 evi haritada gösterir. Veriler iki farklı CSV dosyasından yüklenir ve **Folium** kütüphanesi ile görselleştirilir.

### 🔹 Kullanılan Teknolojiler
- **Python** (Pandas, NumPy, Folium)
- **Jupyter Notebook / Google Colab**
- **CSV veri dosyaları**

## 📂 Dosya İçeriği
- `main2.py` → Veriyi işler ve en pahalı evleri haritada gösteren **Folium haritası** oluşturur.
- `house_prices_top5_map.html` → Harita çıktısı (HTML dosyası olarak kaydedilir).

## 🚀 Kurulum ve Çalıştırma
### 1️⃣ Gerekli Kütüphaneleri Kurun
```bash
pip install pandas numpy folium
```

### 2️⃣ Projeyi Çalıştırın
```bash
python main2.py
```
Çalıştırdıktan sonra **house_prices_top5_map.html** dosyasını tarayıcıda açarak haritayı görüntüleyebilirsiniz.

## 📊 Veri Kaynakları
- `house_sales.csv` → Ev satış fiyatları
- `uszips.csv` → ZIP kodlarına göre enlem ve boylam bilgileri

## 🏗 Geliştirme Süreci
- ZIP kodlarına göre konum verisiyle ev satış fiyatlarını eşleştirir.
- En pahalı 5 evi belirleyerek haritada işaretler.
- **Folium** ile interaktif harita oluşturur ve HTML dosyası olarak kaydeder.

## 📚 Öğrendiklerim
- **Pandas ile CSV dosyalarının birleştirilmesi** ve veri manipülasyonu.
- **Folium** ile interaktif harita oluşturma ve `MarkerCluster` kullanımı.
- **Lambda fonksiyonları** ile veri gruplama ve sıralama işlemleri.
- **Python ile büyük veri setlerini işlerken optimizasyon teknikleri.**
- **HTML formatında harita kaydedip tarayıcıda görüntüleme.**

## 📞 İletişim
Eğer projeyle ilgili herhangi bir sorunuz varsa **issue** açarak bana ulaşabilirsiniz!

