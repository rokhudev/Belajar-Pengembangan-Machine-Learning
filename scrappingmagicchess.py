# -*- coding: utf-8 -*-
"""scrappingmagicchess.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c_GEGgQDitNLKL48TAGruDT1DoO6ThUn
"""

!pip install google-play-scraper

import pandas as pd
from google_play_scraper import reviews_all, Sort

# Mengambil semua ulasan aplikasi Magic Chess dari Google Play Store
ulasan_aplikasi = reviews_all(
    'com.mobilechess.gp',     # ID aplikasi di Play Store
    lang='id',                # Bahasa Indonesia
    country='id',             # Wilayah Indonesia
    sort=Sort.MOST_RELEVANT   # Urutkan berdasarkan ulasan yang paling relevan
)

# Mengubah data ulasan menjadi DataFrame
data_ulasan = pd.DataFrame(ulasan_aplikasi)

# Menghitung total ulasan dan jumlah kolom yang tersedia
total_baris, total_kolom = data_ulasan.shape

# Menyimpan data ulasan ke dalam file CSV
data_ulasan.to_csv('ulasan_magicchess.csv', index=False)