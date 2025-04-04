# Import library
from google_play_scraper import reviews, Sort
import pandas as pd
from datetime import datetime

# Mencatat waktu mulai
start_time = datetime.now()
print(f"Scraping dimulai pada: {start_time}")

# Mengambil 30000 ulasan aplikasi game clash of clans (coc)
scrapreview = reviews(
    'com.supercell.clashofclans',
    lang='id',
    country='id',
    sort=Sort.MOST_RELEVANT,
    count=30000,
)

# Menyimpan hasil scrap ke dalam file csv
data = pd.DataFrame(scrapreview[0])
data.to_csv('./data/ulasan_game_coc.csv', index=False)

# Mencatat waktu selesai
end_time = datetime.now()
print(f"Scraping selesai pada: {end_time}")

# Menampilkan durasi scraping
duration = end_time - start_time
print(f"Durasi scraping: {duration}")