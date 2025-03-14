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

-------

# House Sales 2

This project visualizes house sale prices using the **Folium** library to create interactive maps.

## 📌 Project Description

Using Python, this project analyzes house sale prices and displays the top 5 most expensive houses on a map. Data is loaded from two different CSV files and visualized using **Folium**.

### 🔹 Technologies Used
- **Python** (Pandas, NumPy, Folium)
- **Jupyter Notebook / Google Colab**
- **CSV data files**

## 📂 File Contents
- `main2.py` → Processes the data and generates a **Folium map** displaying the most expensive houses.
- `house_prices_top5_map.html` → Map output (saved as an HTML file).

## 🚀 Installation and Execution
### 1️⃣ Install Required Libraries
```bash
pip install pandas numpy folium
```

### 2️⃣ Run the Project
```bash
python main2.py
```
After running the script, open **house_prices_top5_map.html** in a browser to view the interactive map.

## 📊 Data Sources
- `house_sales.csv` → House sale prices
- `uszips.csv` → Latitude and longitude data by ZIP code

## 🏗 Development Process
- Merges location data with house sale prices based on ZIP codes.
- Identifies the top 5 most expensive houses and marks them on the map.
- Creates an interactive map using **Folium** and saves it as an HTML file.

## 📚 What I Learned
- **Merging CSV files and data manipulation with Pandas.**
- **Creating interactive maps with Folium and using `MarkerCluster`.**
- **Using lambda functions for data grouping and sorting.**
- **Optimizing large dataset processing in Python.**
- **Saving maps in HTML format and displaying them in a browser.**

## 📞 Contact
If you have any questions about the project, feel free to open an **issue**!



