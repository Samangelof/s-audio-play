from tkinter import Button, ttk


def create_play_btn(window, playsong):
    play_btn = Button(window, text="play", command=playsong)
    play_btn.config(
        font=('arial', 20), 
        bg="DodgerBlue2", 
        fg="white", 
        padx=11, 
        pady=7, 
        cursor="hand1")
    play_btn.grid(row=1, column=0)
    return play_btn

def create_pause_btn(window, pausesong):
    pause_btn = Button(window, text="Pause", command=pausesong)
    pause_btn.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7, cursor="hand1")
    pause_btn.grid(row=1, column=1)
    return pause_btn

def create_stop_btn(window, stopsong):
    stop_btn = Button(window, text="Stop", command=stopsong)
    stop_btn.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7, cursor="hand1")
    stop_btn.grid(row=1, column=2)
    return stop_btn

def create_resume_btn(window, resumesong):
    resume_btn = Button(window, text="Resume", command=resumesong)
    resume_btn.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=12, pady=7, cursor="hand1")
    resume_btn.grid(row=1, column=3)
    return resume_btn

def create_progressbar(window):
    progressbar = ttk.Progressbar(window, orient='horizontal', mode='determinate')
    progressbar.grid(row=2, column=0, columnspan=4, pady=10)
    return progressbar


def create_add_track_btn(window, add_track):
    add_track_btn = Button(window, text="Добавить трек", command=add_track)
    add_track_btn.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=11, pady=7, cursor="hand1")
    add_track_btn.grid(row=1, column=4)


