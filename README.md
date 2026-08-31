# 🚀 Spammer OTP WhatsApp

**OTP Spammer dengan 39 API WhatsApp**  
**nobody tools | nobody0x.com**

<p align="center">
  <img src="https://img.shields.io/badge/Version-3.1-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Android-brightgreen.svg" alt="Platform">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue.svg" alt="Python">
</p>

---

## 📌 Tentang

**Spammer OTP WhatsApp** adalah tools untuk spam OTP WhatsApp dengan **39 API** layanan Indonesia.

---

### ✨ Fitur

| Fitur | Deskripsi |
|-------|-----------|
| 🎯 **39 API** | Spammer OTP WhatsApp lengkap |
| 🖥️ **Multi-Platform** | Kompatibel Linux & Android (Termux) |
| ⚡ **Multi-Threading** | Dukungan 1-10 thread |
| 🔄 **Single / Infinite** | Mode sekali jalan atau loop terus |

---

## 🛠️ Instalasi

### 📱 Termux (Android)

```bash
# 1. Update & upgrade
pkg update && pkg upgrade

# 2. Setup penyimpanan (wajib)
termux-setup-storage

# 3. Install Python & Git
pkg install python git -y

# 4. Clone repositori
git clone https://github.com/nbdy0x/spam-otp.git
cd spam-otp

# 5. Install dependencies
pip install requests colorama

# 6. Jalankan
python main.py
```

### 💻 Linux / Windows

```bash
# 1. Clone repositori
git clone https://github.com/nbdy0x/spam-otp.git
cd spam-otp

# 2. Install dependencies
pip install requests colorama

# 3. Jalankan
python main.py
```

---

## 🎮 Cara Pakai

### Full CLI (baru) — tanpa menu, langsung jalan
```bash
# Single round (default 1 thread)
python main.py 085770274922
python main.py 085770274922 -t 5
python main.py +6285770274922 --threads 10

# Infinite loop (delay 60s)
python main.py 085770274922 -i
python main.py 085770274922 -t 5 -i

# Tanpa banner (untuk log/scan)
python main.py 085770274922 --no-banner -t 5

# Help
python main.py --help

# Untuk scanner/automation (wajib pakai workdir, jangan pakai cd)
# workdir: /path/to/spam-otp
# command: timeout 60 python3 main.py 085770274922 -t 5 --no-banner
```

| Flag | Deskripsi |
|------|-----------|
| `phone` (positional) | Nomor target `08xx` / `+62xx` / `62xx` |
| `-t, --threads 1-10` | Jumlah thread (default 1, clamp 1-10) |
| `-i, --infinite` | Loop terus delay 60s (tanpa ini = single round) |
| `--no-banner` | Tanpa clear/banner, log bersih |
| `-h, --help` | Bantuan |

### Menu Interaktif (tanpa argumen)
```bash
python main.py
```
```
[1] Single Round   → Jalankan sekali ke semua API
[2] Infinite Loop  → Loop terus menerus (delay 60 detik)
[3] Keluar
```

### Single Round (interaktif)
1. Pilih menu **1**
2. Pilih jumlah **thread** (1-10, default 1)
3. Masukkan **nomor target** (format `08xx` atau `+62xx`)
4. Tools akan mengirim OTP ke semua API secara parallel

### Infinite Loop (interaktif)
1. Pilih menu **2**
2. Masukkan **nomor target**
3. Tools akan mengirim OTP terus menerus setiap 60 detik
4. Tekan **Ctrl+C** untuk berhenti

### Test Run (tanpa menu)
```bash
python test_run.py
```
Menjalankan semua API ke nomor target yang sudah di-set di dalam file.

---

## ⚙️ Dependencies

- `requests` — HTTP requests
- `colorama` — Terminal colors

---

## 📁 Struktur File

| File | Fungsi |
|------|--------|
| `main.py` | Entry point (CLI + menu interaktif) — `phone [-t 1-10] [-i] [--no-banner]` |
| `main_engine.py` | Mesin utama (orchestrator) |
| `handlers.py` | 24 fungsi handler OTP spesifik |
| `targets.py` | 39 konfigurasi target API |
| `utils.py` | Fungsi utilitas |
| `useragents.py` | Daftar User-Agent |
| `license.py` | Banner & logging |
| `test_run.py` | Test runner otomatis |

---

## ⚠️ Disclaimer

Tools ini dibuat untuk **tujuan edukasi**. Penggunaan di luar itu adalah tanggung jawab pengguna sendiri.
