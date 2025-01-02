import PyInstaller.__main__
import sys
import os

# Mendapatkan path absolute untuk icon dan splash image
current_dir = os.path.dirname(os.path.abspath(__file__))

PyInstaller.__main__.run([
    'app.py',  # Nama file utama aplikasi Anda  
    '--name=TubeDow Pro',  # Nama aplikasi
    '--windowed',  # Membuat aplikasi GUI tanpa console
    '--onefile',  # Membuat single executable
    '--clean',  # Membersihkan cache sebelum build
    '--add-data=assets;assets',   # Jika Anda memiliki folder assets
    # Daftar package yang diperlukan
    '--hidden-import=customtkinter',
    '--hidden-import=PIL',
    '--hidden-import=yt_dlp',
    '--hidden-import=requests',
    # Mengatur icon aplikasi (opsional)
    '--icon=assets/icon.ico',  # Uncomment jika Anda memiliki icon
])