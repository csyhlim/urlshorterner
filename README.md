# URL Shortener

![CI](https://github.com/csyhlim/urlshorterner/actions/workflows/ci.yml/badge.svg)

![Coverage](https://img.shields.io/badge/coverage-97%25-brightgreen)

## Deskripsi Aplikasi

Aplikasi ini adalah URL Shortener sederhana berbasis Flask yang digunakan untuk mempersingkat URL panjang menjadi URL yang lebih pendek dan mudah dibagikan.

Aplikasi memiliki fitur utama:

* Shorten URL (memperpendek link)
* Redirect URL (mengalihkan ke link asli)
* List URL (menampilkan semua URL yang tersimpan)

Aplikasi ini juga mengimplementasikan automated testing dan Continuous Integration menggunakan GitHub Actions.

---

## Cara Menjalankan Aplikasi

### 1. Clone repository

```bash
git clone https://github.com/csyhlim/urlshorterner.git
cd urlshorterner
```

### 2. Buat virtual environment

```bash
python -m venv venv
```

### 3. Aktifkan virtual environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Jalankan aplikasi

```bash
python app.py
```

Aplikasi akan berjalan di:

```
http://127.0.0.1:5000/
```

---

## Cara Menjalankan Test

Untuk menjalankan semua test:

```bash
pytest
```

Untuk melihat test coverage:

```bash
pytest --cov=.
```

---

## Strategi Pengujian

Aplikasi ini menggunakan dua jenis pengujian:

### 1. Unit Testing

Unit test digunakan untuk menguji logika bisnis utama pada aplikasi, seperti:

* Validasi URL
* Generate short code
* Pengambilan data URL

Jumlah unit test yang dibuat ≥ 15 test case.

---

### 2. Integration Testing

Integration test digunakan untuk menguji endpoint API secara langsung, seperti:

* Endpoint POST /shorten
* Endpoint GET /<code> (redirect)
* Endpoint GET /urls
* Handling error (invalid URL, not found)

Jumlah integration test ≥ 5 test case.

---

### 3. Test Coverage

Pengujian menghasilkan coverage lebih dari 60% (target minimal), dengan hasil aktual mencapai sekitar 90%+.

---

## Continuous Integration (CI)

Project ini menggunakan GitHub Actions untuk menjalankan:

* Install dependencies
* Menjalankan semua test
* Menghasilkan test coverage

Pipeline akan berjalan otomatis setiap:

* Push
* Pull Request

---

## Teknologi yang Digunakan

* Python
* Flask
* pytest
* GitHub Actions

---

## Pengembangan Selanjutnya

Aplikasi ini dapat dikembangkan lebih lanjut dengan fitur:

* Custom alias URL
* Expiry link
* Database (MySQL / PostgreSQL)
* UI yang lebih interaktif
