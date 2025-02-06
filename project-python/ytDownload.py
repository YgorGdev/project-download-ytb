import flet as ft
import yt_dlp
import os
import subprocess

def download_video(url, page, open_folder_button):
    if not url:
        page.snack_bar = ft.SnackBar(ft.Text("Por favor, insira uma URL válida."))
        page.snack_bar.open = True
        page.update()
        return
    
    page.controls[2].value = "Baixando..."
    page.update()
    
    ydl_opts = {'format': 'best', 'outtmpl': f"%(title)s.%(ext)s"}
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = os.path.abspath(f"{info['title']}.{info['ext']}")
        page.controls[2].value = "Download concluído!"
        open_folder_button.visible = True
        open_folder_button.data = os.path.dirname(file_path)
    except Exception as e:
        page.controls[2].value = "Erro no download."
    
    page.update()

def open_folder(e):
    folder_path = e.control.data
    if folder_path:
        subprocess.Popen(f'explorer "{folder_path}"' if os.name == 'nt' else ['xdg-open', folder_path])

def main(page: ft.Page):
    page.title = "YouTube Video Downloader"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#1e1e2e"
    
    title = ft.Text("YouTube Downloader", size=30, color="white", weight=ft.FontWeight.BOLD)
    url_input = ft.TextField(hint_text="Insira a URL do vídeo", width=400, bgcolor="#2e2e3e", color="white")
    status_text = ft.Text("", color="white")
    download_button = ft.ElevatedButton("Baixar", on_click=lambda _: download_video(url_input.value, page, open_folder_button), bgcolor="#ff5555", color="white")
    open_folder_button = ft.ElevatedButton("Abrir Pasta", on_click=open_folder, visible=False, bgcolor="#ff5555", color="white")
    
    page.add(title, url_input, status_text, download_button, open_folder_button)
    
ft.app(target=main)