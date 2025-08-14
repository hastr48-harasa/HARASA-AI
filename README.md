# HARASA-AI
Indonesian Dictionary for Food Science, Technology, and Engineer

# Harasa AI - Kamus Cerdas Teknologi Pangan 📖🔬

Selamat datang di Harasa AI, sebuah aplikasi web yang berfungsi sebagai kamus cerdas untuk semua hal yang berkaitan dengan dunia pangan. Dapatkan penjelasan ahli mengenai berbagai istilah dalam ilmu pangan, teknologi pangan, rekayasa pangan, hingga bumbu dan rempah dari seluruh dunia.

Aplikasi ini didukung oleh AI yang berperan sebagai seorang profesor ahli, memberikan definisi yang akurat, padat, dan mudah dimengerti.

![Tangkapan Layar Aplikasi Harasa AI](https://placehold.co/600x400/1a2233/e0e0e0?text=Harasa+AI)

---

## ✨ Fitur Utama

- **Halaman Pembuka Elegan:** Pengalaman pengguna dimulai dengan halaman selamat datang yang menarik.
- **Pencarian Istilah Interaktif:** Masukkan istilah apa pun yang berkaitan dengan pangan.
- **Definisi dari Profesor AI:** Dapatkan penjelasan ahli yang singkat dan padat
- **Antarmuka Modern:** Tampilan dengan tema gelap yang nyaman di mata dan responsif di berbagai perangkat.

---

## 🛠️ Teknologi yang Digunakan

- **Backend:** Python, Flask
- **AI:** Groq API dengan model Llama 3.1
- **Frontend:** HTML, CSS
- **Deployment:** Didesain untuk mudah di-deploy ke platform seperti Render.

---

## 🚀 Cara Menjalankan (Setup Lokal)

Untuk menjalankan proyek ini di komputer Anda, ikuti langkah-langkah berikut:

1.  **Clone Repositori**
    ```bash
    git clone [https://github.com/nama-anda/nama-repositori-anda.git](https://github.com/nama-anda/nama-repositori-anda.git)
    cd nama-repositori-anda
    ```

2.  **Buat Virtual Environment (Sangat Direkomendasikan)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Di Windows, gunakan: venv\Scripts\activate
    ```

3.  **Install Dependensi**
    Pastikan Anda sudah memiliki file `requirements.txt`. Lalu jalankan:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Buat File `.env`**
    Buat sebuah file baru bernama `.env` di direktori utama proyek. Isi file tersebut dengan API Key Groq Anda:
    ```
    GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
    ```

5.  **Jalankan Aplikasi**
    ```bash
    python app.py
    ```
    Buka browser Anda dan akses `http://127.0.0.1:5000`.

---

## 💡 Credits & Inspirasi

Proyek ini dikembangkan oleh Humaam Abdullah. Konsep awal untuk membangun aplikasi web dengan Flask dan AI terinspirasi dan diadaptasi dari deaafrizal/python_flask_1

---

## 📜 Lisensi

Proyek ini dilisensikan di bawah **Lisensi MIT**. Lihat file `LICENSE` untuk detail lebih lanjut.


