# Bleed & Crop Studio Pro - CorelDraw Plugin

Professional plugin untuk CorelDraw 2024 dengan fitur manajemen bleed, crop, safe area, dan export PDF berkualitas tinggi.

## ✨ Fitur Utama

- ✅ **Bleed Manager** - Atur bleed individual atau gabungan (L, T, R, B)
- ✅ **Crop Tools** - Auto crop dengan offset control
- ✅ **Safe Area** - Proteksi konten penting dari trimming
- ✅ **PDF Export** - Export dengan kualitas profesional (72-600 dpi)
- ✅ **Preset Manager** - Preset siap pakai untuk berbagai format (kartu bisnis, flyer, poster, packaging, dll)
- ✅ **Toolbar Integration** - Button toolbar untuk akses cepat
- ✅ **Modern UI Panel** - Interface intuitif dengan 4 tab utama

## 📋 Spesifikasi Teknis

- **Bahasa**: Python 3.8+
- **Kompatibel**: CorelDraw 2024
- **OS**: Windows 10+, macOS 10.14+, Linux
- **Ukuran**: ~2.5 MB
- **Lisensi**: MIT

## 🎯 Preset yang Tersedia

1. **Default** - 2mm semua sisi, safe area 5mm
2. **Business Card** - 2mm bleed, 3mm safe area
3. **Flyer A4** - 5mm bleed, 8mm safe area
4. **Poster A2** - 10mm bleed, 15mm safe area
5. **Packaging** - 3mm bleed, 5mm safe area
6. **Banner** - 2mm L/R, 5mm T/B, 10mm safe area
7. **Label** - 1mm bleed, 2mm safe area

## 📦 Instalasi

### Opsi 1: Installer (Recommended)
```bash
# Download dan jalankan installer
BleedCropStudio-1.0.0-Installer.exe
```

### Opsi 2: Manual Installation
```bash
# Clone repository
git clone https://github.com/azizahkusumawati332-sketch/coredraw-bleed-crop-plugin.git
cd coredraw-bleed-crop-plugin

# Install dependencies
pip install -r installer/requirements.txt

# Install plugin
python installer/setup.py install
```

## 🚀 Cara Penggunaan

### 1. Membuka Plugin
- Buka CorelDraw 2024
- Menu: **Tools** → **Bleed & Crop Studio Pro**
- Atau klik toolbar button "Bleed Settings"

### 2. Tab BLEED
- Pilih metode: Individual Sides atau Inside/Outside
- Atur nilai bleed untuk masing-masing sisi (mm)
- Atau gunakan preset yang tersedia
- Klik **Apply Settings** untuk diterapkan

### 3. Tab CROP
- Enable/disable auto crop
- Atur crop offset (mm)
- Klik **Preview Crop Area** untuk melihat area yang akan dicrop
- Sistem akan otomatis menghilangkan konten di luar area yang ditentukan

### 4. Tab SAFE AREA
- Tentukan jarak safe area dari tepi (mm)
- Klik **Show Safe Area Guides** untuk visualisasi
- Konten dalam safe area tidak akan tertrim

### 5. Tab EXPORT
- Pilih kualitas: Screen (72dpi), Medium (150dpi), High (300dpi), Print (600dpi)
- Pilih options:
  - Include bleed marks
  - Include crop marks
  - Include safe area guides
- Pilih color space: RGB, CMYK, Grayscale
- Klik **Export to PDF**

## 🔧 Pengaturan Lanjutan

### Menyimpan Preset Custom
1. Atur bleed values sesuai kebutuhan
2. Klik **Save Preset**
3. Masukkan nama preset
4. Preset akan tersimpan di `~/.coredraw-bleed-crop/presets.json`

### Konfigurasi Plugin
File config tersimpan di: `~/.coredraw-bleed-crop/config.json`

```json
{
  "version": "1.0.0",
  "default_bleed": {...},
  "auto_save_presets": true,
  "theme": "light"
}
```

## 📊 Konversi Unit

Plugin menggunakan millimeter (mm) sebagai default.
Konversi otomatis:
- 1 mm = 2.834645669 points
- 1 inch = 25.4 mm
- 1 cm = 10 mm

## 🐛 Troubleshooting

### Plugin tidak muncul di toolbar
- Restart CorelDraw
- Pastikan Python 3.8+ terinstall
- Cek log di `~/.coredraw-bleed-crop/plugin.log`

### Export PDF error
- Pastikan path folder writable
- Cek disk space minimal 100MB
- Pastikan CorelDraw tidak sedang proses lain

### Preset tidak tersimpan
- Cek folder `~/.coredraw-bleed-crop/` ada permission
- Jalankan aplikasi dengan admin privileges

## 📞 Support & Kontribusi

- **GitHub Issues**: [Report bugs](https://github.com/azizahkusumawati332-sketch/coredraw-bleed-crop-plugin/issues)
- **Pull Requests**: Welcome! Fork dan kontribusi kode
- **Discussion**: [Diskusi fitur baru](https://github.com/azizahkusumawati332-sketch/coredraw-bleed-crop-plugin/discussions)

## 📝 Changelog

### v1.0.0 (2024-04-02)
- ✨ Initial release
- ✅ Bleed manager (individual & combined)
- ✅ Crop tools dengan offset control
- ✅ Safe area protection
- ✅ PDF export (72-600 dpi)
- ✅ 7 preset profesional
- ✅ Modern UI panel dengan 4 tab
- ✅ Toolbar integration
- ✅ Installer ready untuk distribusi

## 📄 Lisensi

MIT License - Bebas untuk commercial dan personal use. See LICENSE file.

## 👨‍💻 Author

Developed by: **azizahkusumawati332-sketch**
Repository: https://github.com/azizahkusumawati332-sketch/coredraw-bleed-crop-plugin

---

**Made with ❤️ for CorelDraw professionals**