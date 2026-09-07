# Dashboard Profil (Streamlit)

Dashboard profil pribadi berisi foto, biodata, pengalaman kerja, sertifikasi/pelatihan, dan kemampuan (skill).

## 📁 Struktur Folder

```
portfolio-dashboard/
├── app.py               # Kode utama aplikasi
├── requirements.txt     # Daftar library yang dibutuhkan
├── assets/
│   └── foto.jpg          # Letakkan foto profil kamu di sini
└── README.md
```

## 🚀 Menjalankan di Komputer Sendiri (Lokal)

1. Pastikan Python sudah terinstall (versi 3.9 atau lebih baru).
2. Buka terminal, masuk ke folder project ini, lalu jalankan:

   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan aplikasi:

   ```bash
   streamlit run app.py
   ```

4. Browser akan otomatis terbuka di `http://localhost:8501`.

## ✏️ Cara Mengisi Data Kamu

Semua data (nama, foto, pengalaman, sertifikasi, skill) ada di bagian atas file `app.py`, di dalam variabel:

- `PROFILE` → nama, peran, lokasi, email, linkedin, github, tentang saya
- `EXPERIENCE` → daftar pengalaman kerja
- `CERTIFICATIONS` → daftar sertifikasi/pelatihan
- `SKILLS_TEKNIS` → skill teknis + level (0-100)
- `SOFT_SKILLS` → daftar soft skill

Tinggal edit teks di dalam variabel tersebut, tidak perlu mengubah kode lainnya.

Untuk foto profil, simpan file foto dengan nama `foto.jpg` di dalam folder `assets/`
(atau ubah path di `PROFILE["foto"]` jika nama filenya berbeda).

## ☁️ Upload ke GitHub

1. Buat repository baru di GitHub, misalnya bernama `portfolio-dashboard`.
2. Di terminal, jalankan di dalam folder project ini:

   ```bash
   git init
   git add .
   git commit -m "Initial commit: dashboard profil"
   git branch -M main
   git remote add origin https://github.com/USERNAME-KAMU/portfolio-dashboard.git
   git push -u origin main
   ```

   Ganti `USERNAME-KAMU` dengan username GitHub kamu.

## 🌐 Deploy Gratis ke Streamlit Community Cloud

1. Buka [https://share.streamlit.io](https://share.streamlit.io) dan login menggunakan akun GitHub kamu.
2. Klik **"New app"**.
3. Pilih repository `portfolio-dashboard`, branch `main`, dan file utama `app.py`.
4. Klik **"Deploy"**.
5. Tunggu beberapa saat, dan dashboard kamu akan mendapat link publik yang bisa dibagikan.

Setiap kali kamu melakukan `git push` perubahan baru ke GitHub, Streamlit Cloud akan otomatis
memperbarui tampilan dashboard kamu.
