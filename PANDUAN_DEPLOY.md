# 🚀 Panduan Lengkap: Melihat Website & Deploy ke Vercel

Panduan step-by-step untuk pemula dari awal sampai website online!

## 📋 Daftar Isi
1. [Melihat Website di Komputer Anda](#1-melihat-website-di-komputer-anda)
2. [Persiapan Sebelum Deploy](#2-persiapan-sebelum-deploy)
3. [Deploy ke Vercel](#3-deploy-ke-vercel)
4. [Setelah Deploy](#4-setelah-deploy)

---

## 1. Melihat Website di Komputer Anda

### ✅ Website Sudah Berjalan!

Website Anda sudah berjalan di komputer lokal. Buka browser dan ketik:

```
http://localhost:8000
```

### 📱 Halaman yang Tersedia:

- **Homepage**: `http://localhost:8000/index.html`
- **Produk**: `http://localhost:8000/produk.html`
- **Cara Order**: `http://localhost:8000/cara-order.html`

### 🛑 Cara Menghentikan Server:

Jika ingin menghentikan server lokal:
1. Buka terminal/PowerShell yang menjalankan server
2. Tekan `Ctrl + C`
3. Ketik `Y` lalu Enter

### 🔄 Cara Menjalankan Lagi:

Jika server sudah dihentikan dan ingin menjalankan lagi:

```powershell
cd d:\organikpandarejo
python -m http.server 8000
```

---

## 2. Persiapan Sebelum Deploy

### ✏️ Update Informasi Website

Sebelum deploy, update informasi placeholder:

#### A. Nomor WhatsApp

Buka file `js/main.js`, cari baris 78:

```javascript
const whatsappNumber = '6281234567890'; // Ganti dengan nomor Anda
```

Ganti `6281234567890` dengan nomor WhatsApp Anda (format: 62812xxx)

#### B. Informasi Kontak di Footer

Buka semua file HTML (`index.html`, `produk.html`, `cara-order.html`), cari bagian footer dan update:

- Alamat lengkap desa
- Nomor telepon
- Email
- Nama universitas
- Nama kelompok KKN
- Periode KKN

#### C. Ganti Foto (Opsional)

Jika punya foto sendiri, ikuti panduan di `images/PANDUAN_FOTO.md`:

1. Siapkan foto dengan nama: `photo1.jpg`, `photo2.jpg`, dst
2. Copy ke folder yang sesuai:
   - Hero: `images/hero/photo1.jpg`
   - Produk: `images/products/photo1.jpg` sampai `photo12.jpg`
   - Galeri: `images/gallery/photo1.jpg` sampai `photo6.jpg`

> **Catatan**: Jika tidak punya foto, website akan otomatis menggunakan foto placeholder dari Unsplash.

---

## 3. Deploy ke Vercel

### 📦 Langkah 1: Buat Akun Vercel

1. Buka [vercel.com](https://vercel.com)
2. Klik **"Sign Up"**
3. Pilih **"Continue with GitHub"** (atau email)
4. Ikuti proses pendaftaran

### 📁 Langkah 2: Siapkan File untuk Upload

Pastikan folder `d:\organikpandarejo` berisi:
```
organikpandarejo/
├── index.html
├── produk.html
├── cara-order.html
├── README.md
├── css/
│   └── style.css
├── js/
│   └── main.js
└── images/
    ├── hero/
    ├── products/
    ├── gallery/
    └── PANDUAN_FOTO.md
```

### 🚀 Langkah 3: Deploy via Drag & Drop (Cara Termudah)

#### Opsi A: Upload Langsung (Tanpa GitHub)

1. Login ke [vercel.com](https://vercel.com)
2. Klik **"Add New..."** → **"Project"**
3. Scroll ke bawah, cari **"Deploy without Git Provider"**
4. Klik **"Browse"** atau drag folder `organikpandarejo`
5. Pilih folder `d:\organikpandarejo`
6. Klik **"Upload"**
7. Tunggu proses upload selesai
8. Klik **"Deploy"**
9. Tunggu 1-2 menit
10. **Selesai!** Website Anda sudah online!

#### Opsi B: Via GitHub (Lebih Profesional)

**Langkah B1: Install Git**
1. Download Git dari [git-scm.com](https://git-scm.com)
2. Install dengan setting default
3. Restart komputer

**Langkah B2: Buat Repository GitHub**
1. Buka [github.com](https://github.com)
2. Login atau buat akun baru
3. Klik tombol **"+"** di kanan atas → **"New repository"**
4. Isi:
   - Repository name: `organik-pandan-rejo`
   - Description: `Website Organik Pandan Rejo`
   - Pilih **Public**
5. Klik **"Create repository"**

**Langkah B3: Upload ke GitHub**

Buka PowerShell/Terminal di folder `d:\organikpandarejo`:

```powershell
# Inisialisasi Git
git init

# Tambahkan semua file
git add .

# Commit pertama
git commit -m "Initial commit: Organik Pandan Rejo website"

# Hubungkan dengan GitHub (ganti USERNAME dengan username GitHub Anda)
git remote add origin https://github.com/USERNAME/organik-pandan-rejo.git

# Push ke GitHub
git branch -M main
git push -u origin main
```

> **Catatan**: Ganti `USERNAME` dengan username GitHub Anda!

**Langkah B4: Deploy dari GitHub ke Vercel**

1. Login ke [vercel.com](https://vercel.com)
2. Klik **"Add New..."** → **"Project"**
3. Klik **"Import Git Repository"**
4. Pilih repository `organik-pandan-rejo`
5. Klik **"Import"**
6. Klik **"Deploy"** (biarkan setting default)
7. Tunggu 1-2 menit
8. **Selesai!** Website online!

---

## 4. Setelah Deploy

### ✅ Website Anda Sudah Online!

Vercel akan memberikan URL seperti:
```
https://organik-pandan-rejo.vercel.app
```

atau

```
https://organik-pandan-rejo-username.vercel.app
```

### 🌐 Custom Domain (Opsional)

Jika ingin domain sendiri (misal: `organikpandarejo.com`):

1. Beli domain di [Niagahoster](https://niagahoster.co.id), [Namecheap](https://namecheap.com), atau [GoDaddy](https://godaddy.com)
2. Di Vercel, buka project Anda
3. Klik tab **"Settings"** → **"Domains"**
4. Klik **"Add"**
5. Masukkan domain Anda
6. Ikuti instruksi untuk setting DNS

### 🔄 Update Website

**Jika Deploy via Drag & Drop:**
1. Edit file di komputer
2. Buka Vercel dashboard
3. Klik project Anda
4. Klik **"Deployments"**
5. Klik **"..."** → **"Redeploy"**
6. Upload folder yang sudah diupdate

**Jika Deploy via GitHub:**
1. Edit file di komputer
2. Buka PowerShell di folder project
3. Jalankan:
   ```powershell
   git add .
   git commit -m "Update website"
   git push
   ```
4. Vercel akan otomatis deploy ulang!

### 📊 Lihat Statistik Pengunjung

1. Login ke Vercel
2. Buka project Anda
3. Klik tab **"Analytics"**
4. Lihat jumlah pengunjung, page views, dll

### 🔧 Troubleshooting

**Masalah: Foto tidak muncul**
- Pastikan nama file foto sesuai (photo1.jpg, photo2.jpg, dst)
- Pastikan foto ada di folder yang benar
- Cek ukuran file tidak terlalu besar (max 2MB)

**Masalah: WhatsApp tidak berfungsi**
- Pastikan nomor WhatsApp sudah diupdate di `js/main.js`
- Format nomor: `62812xxx` (tanpa +, tanpa spasi)

**Masalah: Website tidak update**
- Clear cache browser (Ctrl + Shift + Delete)
- Tunggu 1-2 menit untuk propagasi
- Coba buka di incognito/private mode

---

## 📞 Bantuan Lebih Lanjut

### Video Tutorial:
- [Cara Deploy ke Vercel](https://www.youtube.com/results?search_query=cara+deploy+website+ke+vercel)
- [Git & GitHub untuk Pemula](https://www.youtube.com/results?search_query=git+github+tutorial+indonesia)

### Dokumentasi:
- [Vercel Documentation](https://vercel.com/docs)
- [GitHub Guides](https://guides.github.com)

---

## ✨ Selamat!

Website Anda sudah online dan bisa diakses dari mana saja! 🎉

**Bagikan link website Anda:**
- WhatsApp
- Instagram
- Facebook
- Poster/Brosur

**Tips Marketing:**
1. Buat QR Code dari link website (gunakan [qr-code-generator.com](https://www.qr-code-generator.com))
2. Cetak QR Code di kemasan produk
3. Share di grup WhatsApp
4. Posting di media sosial secara rutin

---

**Dibuat dengan 💚 untuk Organik Pandan Rejo**
