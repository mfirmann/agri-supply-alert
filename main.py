import requests
import datetime
import json
import os

# --- BAGIAN INI BACA DARI RAHASIA GITHUB ---
OWM_API_KEY = os.environ["OWM_API_KEY"]
SHEET_WEBHOOK_URL = os.environ["SHEET_WEBHOOK"]

# Daftar Lokasi
LOCATIONS = [
    {"name": "Lampung Barat", "lat": "-5.03", "lon": "104.09", "item": "Kopi Robusta"},
    {"name": "Brebes", "lat": "-6.87", "lon": "109.03", "item": "Bawang Merah"},
    {"name": "Boyolali", "lat": "-7.53", "lon": "110.59", "item": "Susu Sapi"}
]

def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={OWM_API_KEY}&units=metric"
    try:
        resp = requests.get(url)
        data = resp.json()
        total_rain = 0
        desc_list = []
        if 'list' in data:
            for i in range(min(8, len(data['list']))): # Cek 24 jam ke depan
                item = data['list'][i]
                if 'rain' in item and '3h' in item['rain']:
                    total_rain += item['rain']['3h']
                if 'weather' in item:
                    d = item['weather'][0]['main']
                    if d not in desc_list: desc_list.append(d)
            return total_rain, ", ".join(desc_list)
        return 0, "No Data"
    except Exception as e:
        print(f"Error API: {e}")
        return 0, "Error"

def check_risk(rain):
    # Status pakai angka biar mudah diurutkan di Dashboard
    if rain > 50: return "3 - BAHAYA", "STOP KIRIM / CEK GUDANG"
    elif rain > 10: return "2 - WASPADA", "PANTAU KETAT"
    else: return "1 - AMAN", "Lanjut Operasi"

if __name__ == "__main__":
    print(f"--- RUNNING JOB: {datetime.datetime.now()} ---")
    for loc in LOCATIONS:
        rain, desc = get_weather(loc['lat'], loc['lon'])
        status, rek = check_risk(rain)
        
        payload = {
            "timestamp": str(datetime.datetime.now()),
            "lokasi": loc['name'],
            "komoditas": loc['item'],
            "cuaca": desc,
            "hujan": round(rain, 2),
            "status": status,
            "rekomendasi": rek
        }
        
        try:
            # Kirim ke Google Sheet
            requests.post(SHEET_WEBHOOK_URL, json=payload)
            print(f"✅ Terkirim: {loc['name']} | Hujan: {rain}mm")
        except Exception as e:
            print(f"❌ Gagal: {loc['name']} - {e}")
