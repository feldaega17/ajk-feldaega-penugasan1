# ajk-feldaega-penugasan1

# Deployment FastAPI Health Check API via Railway

Teknologi yang Digunakan: 

Python 3.11

FastAPI untuk pembuatan REST API

Uvicorn sebagai ASGI server

Railway.app untuk deployment otomatis (CI/CD)

GitHub sebagai source control dan integrasi ke Railway

# Deskripsi Endpoint

Endpoint /health memberikan informasi status server:

```
{
  "nama": "Tunas Bimatara Chrisnanta Budiman",
  "nrp": "5025231999",
  "status": "UP",
  "timestamp": "<waktu saat ini>",
  "uptime": "<durasi uptime server>"
}
```
```
├── main.py               # FastAPI app
├── requirements.txt      # Daftar dependensi
├── Procfile              # Perintah run untuk Railway
```

# Langkah Deployment

1. Push kode ke GitHub

2. Login ke Railway dan hubungkan repo

3. Railway otomatis build & deploy

4. Akses API melalui URL yang diberikan Railway

# ✅ CI/CD Otomatis

Setiap commit baru ke branch main, Railway akan otomatis:

Build ulang

Redeploy aplikasi terbaru

