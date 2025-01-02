# YouTube Downloader Pro

**YouTube Downloader Pro** adalah aplikasi desktop yang memudahkan Anda untuk mengunduh video dan audio dari YouTube. Dibangun menggunakan Python dan **CustomTkinter**, aplikasi ini menawarkan antarmuka pengguna yang modern, intuitif, dan responsif.

## Fitur

- **Unduh Video:** Mendukung format MP4 dengan berbagai resolusi.
- **Unduh Audio:** Mendukung format MP3 dengan berbagai tingkat kualitas.
- **Pratinjau Video:** Lihat thumbnail video dan informasi sebelum mengunduh.
- **Lokasi Penyimpanan:** Pilih folder tujuan untuk menyimpan file yang diunduh.
- **Progres Unduhan:** Tampilkan kecepatan unduhan dan estimasi waktu selesai.

## Persyaratan

Pastikan perangkat Anda memiliki:

- **Python 3.6** atau versi yang lebih baru.
- Paket Python berikut:
  - `tkinter`
  - `customtkinter`
  - `Pillow`
  - `yt-dlp`
  - `requests`

## Instalasi

Ikuti langkah-langkah berikut untuk menginstal aplikasi:

1. **Clone repositori:**
   ```bash
   git clone https://github.com/DeBotz-bot/TubeDow-Pro.git
   ```

```bash
 cd TubeDow-Pro
```

2. **Instal dependensi:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install FFmpeg (Wajib untuk pemrosesan media)**
  
## Panduan Instalasi FFmpeg

### Windows

#### Langkah 1: Unduh FFmpeg
1. Kunjungi [website resmi FFmpeg](https://www.ffmpeg.org/download.html)
2. Klik "Windows Builds" di bawah "Get packages & executable files"
3. Unduh FFmpeg dari salah satu build yang tersedia
4. Ekstrak file ZIP yang diunduh ke lokasi permanen (contoh: `C:\Program Files\ffmpeg`)

#### Langkah 2: Pengaturan Environment Variable
1. Salin path ke folder bin dalam folder FFmpeg yang diekstrak
   - Contoh: `C:\Program Files\ffmpeg\bin`
2. Buka System Properties
   - Klik kanan pada This PC → Properties
3. Klik "Advanced system settings"
4. Klik "Environment Variables"
5. Di bagian "System Variables", cari dan pilih "Path"
6. Klik "Edit"
7. Klik "New"
8. Tempel path folder bin FFmpeg
9. Klik "OK" di semua jendela

#### Langkah 3: Verifikasi Instalasi
1. Buka Command Prompt
2. Ketik: `ffmpeg -version`
3. Jika Anda melihat informasi versi FFmpeg, instalasi berhasil

### Ubuntu/Debian
```bash
sudo apt update
sudo apt install ffmpeg
```

## Cara Penggunaan

4. **Jalankan aplikasi:**
```bash
python app.py
```
## Penggunaan

1. Buka aplikasi **YouTube Downloader Pro**.
2. Masukkan URL video YouTube ke kolom yang tersedia.
3. Klik tombol **Process** untuk memproses video.
4. Pilih format unduhan (Video atau Audio) dan kualitas yang diinginkan.
5. Klik tombol **Download** untuk memulai unduhan.
6. Gunakan tombol **Open Folder** untuk membuka lokasi tempat file disimpan.

## Penyelesaian Masalah

### Masalah Umum

1. **Video tidak ada suaranya**
   - Pastikan FFmpeg sudah terinstal dengan benar
   - Periksa FFmpeg sudah ada di system PATH
   - Coba jalankan `ffmpeg -version` di terminal

2. **Unduhan gagal**
   - Periksa koneksi internet
   - Pastikan URL YouTube valid
   - Pastikan ruang disk mencukupi
   - Periksa izin penulisan di folder tujuan

3. **FFmpeg tidak ditemukan**
   - Ikuti panduan instalasi FFmpeg di atas
   - Restart aplikasi setelah menginstal FFmpeg
   - Pastikan system PATH sudah termasuk FFmpeg

## Cara Berkontribusi

1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b fitur/FiturKeren`)
3. Commit perubahan Anda (`git commit -m 'Menambahkan FiturKeren'`)
4. Push ke branch (`git push origin fitur/FiturKeren`)
5. Buat Pull Request

## Lisensi

Didistribusikan di bawah Lisensi MIT. Lihat `LICENSE` untuk informasi lebih lanjut.

## Kredit

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) untuk fungsi unduh YouTube
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) untuk elemen UI modern
- [FFmpeg](https://ffmpeg.org/) untuk pemrosesan media

## Dukungan

Untuk mendapatkan bantuan, silakan buat issue di repository atau hubungi [deokatube@gmail.com]

---
Built with ❤️ by DeBotz