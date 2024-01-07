import tkinter
import customtkinter as ct
from pytube import YouTube

ct.set_appearance_mode('System')
ct.set_default_color_theme('blue')

def startDownload():
    try:
        linkyt = link.get()
        ytpars = YouTube(linkyt,  on_progress_callback=on_progress)
        video = ytpars.streams.get_highest_resolution()
        video.download()
    except Exception as e:
        print(f'Error:', {e})
    

def startDownloadAuido():
    try:
        linkyt = link.get()
        ytpars = YouTube(linkyt, on_progress_callback=on_progress)
        audio = ytpars.streams.get_audio_only()
        audio.download()
    except Exception as e:
        print(f'Error:', {e})
    


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_ready = bytes_downloaded / total_size * 100
    per = str(int(percentage_ready))
    percentage.configure(text = per + '%')
    percentage.update()
    progresBar.set(float(percentage_ready) / 100)

app = ct.CTk()
app.geometry('800x600')
app.title('Download')

font = ct.CTkFont(family='helvitica', size= 25)

title = ct.CTkLabel(app, text='Посилання на відео', font=font)
title.pack(pady=20, padx = 10)

url = tkinter.StringVar()
link = ct.CTkEntry(app, width=350, height=40, textvariable=url)
link.pack()

percentage = ct.CTkLabel(app, text='0%')
percentage.pack()

progresBar = ct.CTkProgressBar(app, width=350)
progresBar.set(0)
progresBar.pack(pady= 10, padx= 10)

downloadvideo = ct.CTkButton(
app, 
width=350,
text='Завантажиит відео', 
height=40, 
font=font,
command=startDownload 
)
downloadvideo.pack(padx= 10, pady=20)

downloadaudio = ct.CTkButton(
app, 
width=350,
text='Завантажиит аудіо', 
height=40, 
font=font,
command=startDownloadAuido 
)
downloadaudio.pack(padx= 10, pady=0)

app.mainloop()