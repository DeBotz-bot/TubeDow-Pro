# Copyright (c) 2023 DeBotz. All rights reserved.

import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import yt_dlp
import os
import threading
import re
import requests
from io import BytesIO
import subprocess

# Configure CustomTkinter theme
ctk.set_appearance_mode("system")  # Use system theme
ctk.set_default_color_theme("blue")

class YouTubeDownloader(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Configuration
        self.title("YouTube Downloader Pro v1.0")
        self.geometry("800x900")
        self.configure(fg_color=("white", "#1a1a1a"))  #gantii warna font
        
        # Create main container with padding
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(padx=30, pady=30, fill="both", expand=True)

        # Application Header
        self.header_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        self.header_frame.pack(fill="x", pady=(0, 20))

        self.title_label = ctk.CTkLabel(
            self.header_frame,
            text="YouTube Downloader Pro",
            font=ctk.CTkFont(family="Helvetica", size=32, weight="bold"),
            text_color=("black", "white")
        )
        self.title_label.pack(pady=(0, 10))

        # Add copyright label at the bottom
        self.copyright_label = ctk.CTkLabel(
            self.container,
            text="© 2024 DeBotz. All rights reserved.",
            font=ctk.CTkFont(size=12),
            text_color=("gray50", "gray70")
        )
        self.copyright_label.pack(side="bottom", pady=(10, 0))

        # URL Input Section
        self.url_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        self.url_frame.pack(fill="x", pady=(0, 20))

        self.url_entry = ctk.CTkEntry(
            self.url_frame,
            placeholder_text="Paste YouTube URL here...",
            height=45,
            font=ctk.CTkFont(size=14),
            border_width=2,
            corner_radius=10
        )
        self.url_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.convert_btn = ctk.CTkButton(
            self.url_frame,
            text="Process",
            command=self.convert_video,
            height=45,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=("#2ecc71", "#27ae60"),
            hover_color=("#27ae60", "#219a52"),
            corner_radius=10
        )
        self.convert_btn.pack(side="right")

        # Preview Section
        self.preview_frame = ctk.CTkFrame(
            self.container,
            corner_radius=15,
            border_width=2,
            border_color=("gray75", "gray25"),
            fg_color=("gray95", "gray10")
        )
        self.preview_frame.pack(fill="x", pady=(0, 20))

        # Thumbnail
        self.thumbnail_label = ctk.CTkLabel(
            self.preview_frame,
            text="Enter a YouTube URL to start",
            font=ctk.CTkFont(size=14),
            corner_radius=10
        )
        self.thumbnail_label.pack(pady=20)

        # Video Information
        self.video_info_label = ctk.CTkLabel(
            self.preview_frame,
            text="",
            font=ctk.CTkFont(size=14),
            wraplength=700
        )
        self.video_info_label.pack(pady=10)

        # Download Options Frame
        self.options_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        self.options_frame.pack(fill="x", pady=(0, 20))

        # Format Selection
        self.format_var = tk.StringVar(value="video")
        
        # Format Radio Buttons Frame
        self.format_frame = ctk.CTkFrame(self.options_frame, fg_color="transparent")
        self.format_frame.pack(side="left", padx=(0, 20))
        
        self.video_radio = ctk.CTkRadioButton(
            self.format_frame,
            text="Video (MP4)",
            variable=self.format_var,
            value="video",
            command=self.update_format_options,
            font=ctk.CTkFont(size=14),
            border_width_checked=6,
            fg_color=("#2ecc71", "#27ae60"),
        )
        self.video_radio.pack(side="left", padx=(0, 10))
        
        self.audio_radio = ctk.CTkRadioButton(
            self.format_frame,
            text="Audio (MP3)",
            variable=self.format_var,
            value="audio",
            command=self.update_format_options,
            font=ctk.CTkFont(size=14),
            border_width_checked=6,
            fg_color=("#2ecc71", "#27ae60"),
        )
        self.audio_radio.pack(side="left")

        # Quality Selection Frame
        self.quality_frame = ctk.CTkFrame(self.options_frame, fg_color="transparent")
        self.quality_frame.pack(side="left", padx=(0, 10))

        # Resolution Selection (for video)
        self.resolution_var = tk.StringVar(value="")
        self.resolution_combo = ctk.CTkComboBox(
            self.quality_frame,
            values=[],
            variable=self.resolution_var,
            font=ctk.CTkFont(size=14),
            height=40,
            width=150,
            button_color=("#2980b9", "#2573a7"),
            button_hover_color=("#2573a7", "#1f618d"),
            corner_radius=10
        )
        self.resolution_combo.pack(side="left")

        # Audio Quality Selection (initially hidden)
        self.audio_quality_var = tk.StringVar(value="192")
        self.audio_quality_combo = ctk.CTkComboBox(
            self.quality_frame,
            values=["64", "128", "192", "256", "320"],
            variable=self.audio_quality_var,
            font=ctk.CTkFont(size=14),
            height=40,
            width=150,
            button_color=("#2980b9", "#2573a7"),
            button_hover_color=("#2573a7", "#1f618d"),
            corner_radius=10
        )
        self.audio_quality_combo.pack_forget()  # Initially hidden

        # Download Button
        self.download_btn = ctk.CTkButton(
            self.options_frame,
            text="Download",
            command=self.download_video,
            state="disabled",
            height=40,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=("#3498db", "#2980b9"),
            hover_color=("#2980b9", "#2573a7"),
            corner_radius=10
        )
        self.download_btn.pack(side="left", padx=(0, 10))

        # Open Folder Button
        self.open_folder_btn = ctk.CTkButton(
            self.options_frame,
            text="Open Folder",
            command=self.open_download_folder,
            state="disabled",
            height=40,
            font=ctk.CTkFont(size=14),
            fg_color=("#9b59b6", "#8e44ad"),
            hover_color=("#8e44ad", "#803d9f"),
            corner_radius=10
        )
        self.open_folder_btn.pack(side="left")

        # Progress Section
        self.progress_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        self.progress_frame.pack(fill="x")

        self.progress_bar = ctk.CTkProgressBar(
            self.progress_frame,
            width=700,
            height=15,
            corner_radius=10,
            progress_color=("#2ecc71", "#27ae60")
        )
        self.progress_bar.pack(pady=(0, 10))
        self.progress_bar.set(0)

        self.status_label = ctk.CTkLabel(
            self.progress_frame,
            text="",
            font=ctk.CTkFont(size=13),
            text_color=("gray50", "gray70")
        )
        self.status_label.pack()

        # Variables
        self.video_info = None
        self.thumbnail_url = None
        self.download_folder = ""

    def update_format_options(self):
        if self.format_var.get() == "video":
            self.audio_quality_combo.pack_forget()
            self.resolution_combo.pack(side="left")
        else:
            self.resolution_combo.pack_forget()
            self.audio_quality_combo.pack(side="left")

    def validate_youtube_url(self, url):
        youtube_regex = (
            r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
            r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
        )
        return re.match(youtube_regex, url) is not None

    def convert_video(self):
        url = self.url_entry.get()
        if not url or not self.validate_youtube_url(url):
            self.show_error("Please enter a valid YouTube URL")
            return

        self.convert_btn.configure(state="disabled")
        self.status_label.configure(
            text="Processing video...",
            text_color=("#2980b9", "#3498db")
        )
        threading.Thread(target=self.get_video_info, args=(url,), daemon=True).start()

    def get_video_info(self, url):
        try:
            ydl_opts = {'quiet': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
                self.after(0, self.update_video_info, info_dict)
        except Exception as e:
            self.after(0, self.show_error, str(e))

    def update_video_info(self, info_dict):
        title = info_dict.get('title', 'Unknown')
        duration = info_dict.get('duration', 'Unknown')
        views = info_dict.get('view_count', 'Unknown')
        uploader = info_dict.get('uploader', 'Unknown')
        
        self.thumbnail_url = info_dict.get('thumbnail', '')
        
        # Get available resolutions
        if self.format_var.get() == "video":
            resolutions = [
                f"{f['height']}p" for f in info_dict['formats']
                if f.get('vcodec') != 'none' and f.get('height') is not None
            ]
            resolutions = sorted(set(resolutions), key=lambda x: int(x.replace('p', '')))
            self.resolution_combo.configure(values=resolutions)
            self.resolution_var.set(resolutions[-1] if resolutions else "")

        # Format duration to minutes:seconds
        duration_str = f"{int(duration//60)}:{int(duration%60):02d}" if isinstance(duration, (int, float)) else duration
        
        # Format view count with commas
        views_str = f"{views:,}" if isinstance(views, (int, float)) else views

        info_text = f"Title: {title}\nUploader: {uploader}\nDuration: {duration_str}\nViews: {views_str}"
        self.video_info_label.configure(text=info_text)
        self.load_thumbnail(self.thumbnail_url)

        self.video_info = info_dict
        self.download_btn.configure(state="normal")
        self.convert_btn.configure(state="normal")
        self.status_label.configure(
            text="Video processed successfully",
            text_color=("#27ae60", "#2ecc71")
        )

    def load_thumbnail(self, url):
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            img = img.resize((480, 270), Image.LANCZOS)
            ctk_image = ctk.CTkImage(light_image=img, dark_image=img, size=(480, 270))
            self.thumbnail_label.configure(image=ctk_image, text="")
        except Exception as e:
            self.show_error(f"Failed to load thumbnail: {str(e)}")

    def download_video(self):
        save_path = tk.filedialog.askdirectory(title="Choose Download Location")
        if not save_path:
            return

        self.download_folder = save_path
        self.download_btn.configure(state="disabled")
        self.status_label.configure(
            text="Downloading...",
            text_color=("#2980b9", "#3498db")
        )
        self.progress_bar.set(0)
        threading.Thread(target=self.start_download, args=(save_path,), daemon=True).start()

    def start_download(self, save_path):
        try:
            if self.format_var.get() == "video":
                resolution = self.resolution_var.get().replace("p", "")
                ydl_opts = {
                    'format': f'bestvideo[height<={resolution}]+bestaudio/best',
                    'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
                    'progress_hooks': [self.progress_hook],
                    'postprocessors': [{
                        'key': 'FFmpegVideoRemuxer',
                        'preferedformat': 'mp4',
                    }],
                    'merge_output_format': 'mp4',
                    'postprocessor_args': [
                        '-c:v', 'copy',
                        '-c:a', 'aac',  # Convert audio to AAC codec
                        '-strict', 'experimental'
                    ],
                    'quiet': False
                }
            else:  # Audio format
                audio_quality = self.audio_quality_var.get()
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
                    'progress_hooks': [self.progress_hook],
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': audio_quality,
                    }],
                    'quiet': False
                }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.video_info['webpage_url']])
            self.after(0, self.download_complete)
        except Exception as e:
            self.after(0, self.show_error, str(e))

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            try:
                percent = d['downloaded_bytes'] / d['total_bytes'] * 100
                self.progress_bar.set(percent / 100)
                
                # Update status with download speed and ETA
                speed = d.get('speed', 0)
                eta = d.get('eta', 0)
                
                if speed and eta:
                    speed_mb = speed / 1024 / 1024  # Convert to MB/s
                    status_text = f"Downloading: {speed_mb:.1f} MB/s - {eta} seconds remaining"
                    self.status_label.configure(text=status_text)
            except:
                pass  # Handle cases where total_bytes might be unavailable

        elif d['status'] == 'finished':
            self.after(0, self.download_complete)

    def download_complete(self):
        self.status_label.configure(
            text="Download completed successfully!",
            text_color=("#27ae60", "#2ecc71")
        )
        self.download_btn.configure(state="normal")
        self.open_folder_btn.configure(state="normal")
        self.progress_bar.set(1)  # Set progress to 100%

    def open_download_folder(self):
        if self.download_folder:
            try:
                # Cross-platform folder opening
                if os.name == 'nt':  # Windows
                    os.startfile(os.path.abspath(self.download_folder))
                elif os.name == 'posix':  # macOS and Linux
                    if sys.platform == 'darwin':  # macOS
                        subprocess.Popen(['open', os.path.abspath(self.download_folder)])
                    else:  # Linux
                        subprocess.Popen(['xdg-open', os.path.abspath(self.download_folder)])
            except Exception as e:
                self.show_error(f"Failed to open folder: {str(e)}")

    def show_error(self, error_message):
        self.status_label.configure(
            text=f"Error: {error_message}",
            text_color=("#e74c3c", "#c0392b")
        )
        self.convert_btn.configure(state="normal")
        self.download_btn.configure(state="disabled")
        self.progress_bar.set(0)

# Tambahkan bagian main
if __name__ == "__main__":
    app = YouTubeDownloader()
    app.mainloop()