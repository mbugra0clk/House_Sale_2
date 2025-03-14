import pandas as pd
import numpy as np
import warnings
import folium
from folium.plugins import MarkerCluster
warnings.filterwarnings('ignore')


uszips_df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/house_sales/uszips.csv")

house_sales_df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/house_sales/house_sales.csv")

uszips_df.rename(columns={"zip": "ZipCode"}, inplace=True)

merged_df = house_sales_df.merge(uszips_df[['ZipCode', 'lat', 'lng']], on="ZipCode", how="left")


#tüm verileri görünütlenmiyor. çok fazla veri olduğu için.
''' 
# Haritanın merkezini belirle.
center_lat = merged_df["lat"].mean()
center_lng = merged_df["lng"].mean()


# Haritayı oluşturma.
m = folium.Map(location=[center_lat, center_lng], zoom_start=3)

marker_cluster = MarkerCluster().add_to(m)

for _, row in merged_df.iterrows():
    folium.Marker(
        location=[row["lat"], row["lng"]],
        popup=f"Fiyat: ${row['SalePrice']:,.0f}"
    ).add_to(marker_cluster)

m.save("house_prices_map_1.0.html")

print("Harita 'house_prices_map.html' olarak kaydedildi. Tarayıcıda açarak görüntüleyebilirsiniz.")
'''


# burada kümeliyorum.
center_lat = merged_df["lat"].mean()
center_lng = merged_df["lng"].mean()

m = folium.Map(location=[center_lat, center_lng], zoom_start=3)

marker_cluster = MarkerCluster().add_to(m)

top_houses = merged_df.groupby("ZipCode").apply(lambda x: x.nlargest(5, "SalePrice")).reset_index(drop=True)

# 📌 Her ev için haritaya marker ekleyin
for _, row in top_houses.iterrows():
    if pd.notna(row["lat"]) and pd.notna(row["lng"]):  # Koordinatlar boş değilse
        popup_text = f"<b>Top 5 Expensive Houses</b><br>Price: ${row['SalePrice']:,.0f}"
        
        folium.Marker(
            location=[row["lat"], row["lng"]],
            popup=popup_text,
            icon=folium.Icon(color="red", icon="home")
        ).add_to(marker_cluster)

m.save("house_prices_top5_map.html")

print("Harita 'house_prices_top5_map.html' olarak kaydedildi. Tarayıcıda açarak görüntüleyebilirsiniz.")
