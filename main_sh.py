import pygame
from pygame import mixer
import os
from audio_buttons import (
    create_add_track_btn,
    create_play_btn, 
    create_pause_btn, 
    create_stop_btn, 
    create_resume_btn, 
    create_progressbar,
)
from tkinter import (
    ttk, 
    ACTIVE, 
    Tk, 
    StringVar, 
    Listbox, 
    SINGLE, END, 
    Button, 
    mainloop,
    filedialog
)


class AudioPlayer:
    def __init__(self, window):
        self.window = window
        self.window.resizable(False, False)
        
        self.play_btn = create_play_btn(self.window, self.playsong)
        self.pause_btn = create_pause_btn(self.window, self.pausesong)
        self.stop_btn = create_stop_btn(self.window, self.stopsong)
        self.resume_btn = create_resume_btn(self.window, self.resumesong)
        self.add_track_btn = create_add_track_btn(self.window, self.add_track)
        self.progressbar = create_progressbar(self.window)


        mixer.init()


        self.playlist = Listbox(self.window, selectmode=SINGLE, bg="DodgerBlue2", fg="white", font=('arial', 15), width=40)
        self.playlist.grid(columnspan=5)


        os.chdir(r'music')
        songs = os.listdir()
        for s in songs:
            self.playlist.insert(END, s)


    def playsong(self):
        currentsong = self.playlist.get(ACTIVE)
        mixer.music.load(currentsong)
        self.songstatus.set("Playing")
        mixer.music.play()

        song = pygame.mixer.Sound(currentsong)
        song_length = song.get_length()
        progress_max = int(song_length)
        self.progressbar['maximum'] = progress_max

        def update_progress():
            current_time = int(mixer.music.get_pos() / 1000)
            self.progressbar['value'] = current_time
            if current_time < progress_max:
                self.window.after(1000, update_progress)

        update_progress()


    def pausesong(self):
        self.songstatus.set("Paused")
        mixer.music.pause()

    def stopsong(self):
        self.songstatus.set("Stopped")
        mixer.music.stop()
        self.progressbar['value'] = 0

    def resumesong(self):
        self.songstatus.set("Resuming")
        mixer.music.unpause()    

    def add_track(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
        if file_path:
            file_name = os.path.basename(file_path)
            self.playlist.insert(END, file_name)

if __name__ == '__main__':
    window = Tk()
    player = AudioPlayer(window)
    mainloop()
