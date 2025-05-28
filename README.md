# Analisis Sentimen Bahasa Indonesia

Aplikasi web sederhana untuk analisis sentimen teks berbahasa Indonesia menggunakan model BERT multilingual.

## 🔍 Fitur
- Deteksi sentimen: **sangat negatif**, **negatif**, **netral**, **positif**, **sangat positif**
- Menampilkan tingkat kepercayaan (confidence) tiap label
- Tampilan UI simpel, bersih, dan responsif (HTML + CSS)

## 🚀 Cara Menjalankan

```bash
# 1. Clone repository
git clone https://github.com/Yudha13/simple-sentiment-analysis.git
cd simple-sentiment-analysis

# 2. aktifkan virtual enviroment
python3 -m venv .venv

# 3. Install dependencies
pip install -r requirements.txt

# 4. Jalankan aplikasi
python3 app.py

# 5. Buka browser ke:
http://localhost:5000
```

## 📁 Struktur Project

```
.
├── app.py
├── templates
│   └── index.html
├── static
│   └── style.css
├── requirements.txt
└── README.md
```

## 💡 Catatan

- Model yang digunakan: [`nlptown/bert-base-multilingual-uncased-sentiment`](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment)
- Model ini berbasis BERT dan dapat memahami berbagai bahasa, termasuk Bahasa Indonesia.
- Hasil analisis bukan 100% akurat — ini baseline, bukan production-ready.

