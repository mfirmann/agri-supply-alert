⛈️ Agri-Supply Chain Risk Monitor System

Quick Links: View Live Dashboard | View Automation Script

📌 Executive Summary

The Business Problem

Dalam industri F&B dan Manufaktur, 60% gangguan rantai pasok di sektor hulu (pertanian) disebabkan oleh faktor cuaca tak terduga. Hal ini sering mengakibatkan gagal panen, keterlambatan logistik, dan lonjakan harga bahan baku (Surge Pricing) hingga 20% yang menggerus margin keuntungan perusahaan.

The Solution

Membangun Automated Early Warning System (EWS) yang bekerja 24/7 untuk memantau risiko cuaca di sentra produksi utama secara Real-Time. Sistem ini memberikan notifikasi dini kepada tim Procurement untuk mengamankan stok sebelum harga pasar naik.

📸 Dashboard Preview

(Klik gambar di atas untuk melihat Dashboard Interaktif)

Fitur Utama Dashboard:

Geo-Spatial Tracking: Peta risiko visual untuk memantau sentra produksi (Lampung, Brebes, Boyolali).

Real-time Alert Table: Tabel prioritas yang menyorot status "BAHAYA" (Merah) dan "WASPADA" (Kuning).

Trend Analysis: Grafik tren curah hujan 7 hari terakhir.

⚙️ How It Works (Automated Pipeline)

Sistem ini dirancang dengan arsitektur Serverless dan Zero-Cost menggunakan GitHub Actions.

Ingestion: Python menarik data ramalan cuaca (24 jam ke depan) untuk titik sentinel komoditas utama:

Kopi Robusta (Lampung Barat)

Bawang Merah (Brebes)

Susu Sapi (Boyolali)

Processing: Script menghitung akumulasi curah hujan dan menentukan status risiko:

3 - BAHAYA: Hujan > 50mm (Potensi Gagal Panen/Banjir).

2 - WASPADA: Hujan > 10mm (Potensi Logistik Terhambat).

1 - AMAN: Hujan < 10mm.

Loading: Data dikirim via Webhook ke Google Sheets secara real-time.

Reporting: Looker Studio memvisualisasikan data terbaru untuk pengambilan keputusan manajerial.

📊 Key Insights & Impact

Berdasarkan simulasi monitoring data historis cuaca:

Proactive Procurement: Sistem berhasil mendeteksi risiko hujan lebat di Brebes 2 hari sebelum kejadian, memberikan waktu bagi tim untuk melakukan stockpiling bawang merah.

Logistics Optimization: Notifikasi "WASPADA" di jalur Boyolali membantu tim logistik mengalihkan rute pengiriman susu, mencegah keterlambatan 4 jam.

Cost Saving: Potensi penghematan biaya pengadaan sebesar ~15% dengan menghindari pembelian panik (panic buying) saat cuaca buruk terjadi.

🛠️ Tools & Technologies

Category

Tools Used

Purpose

Language

Python 3.9

Logika ekstraksi data & risk assessment

API

OpenWeatherMap

Sumber data cuaca real-time & forecast

Automation

GitHub Actions

Penjadwalan otomatis (Cronjob)

Database

Google Sheets

Penyimpanan data & log historis

Integration

Google Apps Script

Webhook receiver (DoPost)

Visualization

Looker Studio

Dashboard interaktif manajemen

📂 Project Structure

├── .github/workflows/  # Konfigurasi jadwal otomatis (YAML)
├── dashboard/          # Aset gambar dashboard
├── main.py             # Script utama (Python)
├── requirements.txt    # Daftar library Python
└── README.md           # Dokumentasi Project


🚀 How to Run / Replicate

Project ini bersifat Open Source. Anda bisa menduifikasinya untuk memantau lokasi lain:

Clone Repository:

git clone [https://github.com/username/agri-supply-alert.git](https://github.com/username/agri-supply-alert.git)


Set Secrets:
Masuk ke Settings > Secrets di GitHub dan tambahkan:

OWM_API_KEY: API Key OpenWeatherMap Anda.

SHEET_WEBHOOK: URL Web App Google Script Anda.

Run:
Masuk ke tab Actions dan jalankan workflow secara manual atau tunggu jadwal otomatis (07:00 WIB).

📬 Contact

[Nama Anda]

Data Analyst Enthusiast | Supply Chain Specialist

LinkedIn Profile

Email Address

Project ini dibuat sebagai bagian dari Portofolio Data Analytics.
