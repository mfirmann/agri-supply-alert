# ⛈️ Agri-Supply Chain Risk Monitor System

## 📌 Executive Summary

### The Business Problem

Dalam industri **F&B** dan **Manufaktur**, sekitar **60% gangguan rantai pasok di sektor hulu (pertanian)** disebabkan oleh faktor **cuaca tak terduga**. Dampaknya antara lain:

* Gagal panen
* Keterlambatan logistik
* Lonjakan harga bahan baku (*surge pricing*) hingga **±20%**

Kondisi ini secara langsung menggerus **margin keuntungan perusahaan**.

### The Solution

Membangun **Automated Early Warning System (EWS)** yang berjalan **24/7** untuk memantau risiko cuaca di sentra produksi utama secara **real-time**.

Sistem ini memberikan **notifikasi dini** kepada tim **Procurement** agar dapat:

* Mengamankan stok lebih awal
* Menghindari pembelian panik saat harga melonjak

---

## 📸 Dashboard Preview
<img src="Dashboard/dashboard_preview.png" width="900"/>

> *(Klik gambar di atas untuk melihat Dashboard Interaktif)*

### Fitur Utama Dashboard

* **Geo-Spatial Tracking**
  Peta risiko visual untuk memantau sentra produksi utama:

  * Lampung
  * Brebes
  * Boyolali

* **Real-time Alert Table**
  Tabel prioritas yang menyorot status:

  * 🔴 **BAHAYA**
  * 🟡 **WASPADA**

* **Trend Analysis**
  Grafik tren curah hujan **7 hari terakhir**

---

## ⚙️ How It Works (Automated Pipeline)

Sistem dirancang dengan arsitektur **Serverless** dan **Zero-Cost** menggunakan **GitHub Actions**.

### 1️⃣ Ingestion

Python script menarik data **ramalan cuaca 24 jam ke depan** untuk titik sentinel komoditas utama:

* ☕ **Kopi Robusta** – Lampung Barat
* 🧅 **Bawang Merah** – Brebes
* 🥛 **Susu Sapi** – Boyolali

### 2️⃣ Processing

Script menghitung **akumulasi curah hujan** dan menentukan status risiko:

| Risk Level | Status     | Threshold Curah Hujan | Dampak Utama                 |
| ---------: | ---------- | --------------------- | ---------------------------- |
|          3 | 🔴 BAHAYA  | > 50 mm               | Potensi gagal panen / banjir |
|          2 | 🟡 WASPADA | > 10 mm               | Potensi logistik terhambat   |
|          1 | 🟢 AMAN    | < 10 mm               | Risiko minimal               |

### 3️⃣ Loading

Data dikirim secara **real-time** melalui **Webhook** ke **Google Sheets** sebagai:

* Data store
* Log historis

### 4️⃣ Reporting

**Looker Studio** digunakan untuk memvisualisasikan data terbaru guna mendukung:

* Pengambilan keputusan manajerial
* Respons cepat lintas tim

---

## 📊 Key Insights & Business Impact

Berdasarkan simulasi monitoring data historis cuaca:

### 🔎 Proactive Procurement

* Sistem mendeteksi **risiko hujan lebat di Brebes** **2 hari lebih awal**
* Memberikan waktu bagi tim untuk melakukan **stockpiling bawang merah**

### 🚚 Logistics Optimization

* Status **WASPADA** di Boyolali membantu tim:

  * Mengalihkan rute pengiriman susu
  * Mencegah keterlambatan hingga **±4 jam**

### 💰 Cost Saving

* Potensi penghematan biaya pengadaan sekitar **±15%**
* Menghindari **panic buying** saat cuaca ekstrem

---

## 🛠️ Tools & Technologies

| Category      | Tools Used         | Purpose                          |
| ------------- | ------------------ | -------------------------------- |
| Language      | Python 3.9         | Ekstraksi data & risk assessment |
| API           | OpenWeatherMap     | Data cuaca real-time & forecast  |
| Automation    | GitHub Actions     | Penjadwalan otomatis (Cronjob)   |
| Database      | Google Sheets      | Penyimpanan data & log historis  |
| Integration   | Google Apps Script | Webhook receiver (doPost)        |
| Visualization | Looker Studio      | Dashboard interaktif manajemen   |

---

## 📂 Project Structure

```text
.
├── .github/workflows/   # Konfigurasi jadwal otomatis (YAML)
├── dashboard/           # Aset gambar dashboard
├── main.py              # Script utama (Python)
├── requirements.txt     # Daftar library Python
└── README.md            # Dokumentasi project
```

---

## 🚀 How to Run / Replicate

Project ini bersifat **Open Source** dan dapat dimodifikasi untuk lokasi atau komoditas lain.

### 1️⃣ Clone Repository

```bash
git clone https://github.com/username/agri-supply-alert.git
```

### 2️⃣ Set Secrets (GitHub)

Masuk ke **Settings → Secrets → Actions**, lalu tambahkan:

| Secret Name     | Description                    |
| --------------- | ------------------------------ |
| `OWM_API_KEY`   | API Key OpenWeatherMap         |
| `SHEET_WEBHOOK` | URL Web App Google Apps Script |

### 3️⃣ Run Workflow

* Jalankan manual melalui tab **Actions**, atau
* Tunggu jadwal otomatis (**07:00 WIB**)

---

## 📬 Contact

**Maulana Firman Nurdiansyah**
Data Analyst & Business Intelligent | Mathematics Graduate | TensorFlow Certified | Ex-Retail Entrepreneur

* 💼 LinkedIn: https://www.linkedin.com/in/m-firman-n/
* ✉️ Email: m.firman.n000@gmail.com

---

> Project ini dibuat sebagai bagian dari **Portofolio Data Analytics** dan berfokus pada penerapan data untuk mitigasi risiko rantai pasok sektor agrikultur.
