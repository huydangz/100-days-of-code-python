from tkinter import *
from tkinter import filedialog
from gtts import gTTS
from tika import parser
import os

TITLE_FONT = "Cambria"
TITLE_COLOR = "#00ADB5"
WORD_FONT = "Verdana"
WORD_COLOR = "#EEEEEE"
BACKGROUND_COLOR = "#222831"
BTN_BACKGROUND_COLOR = "#393E46"


def open_pdf():
    pdf_file = filedialog.askopenfilename(
        initialdir="/",
        title="Select PDF",
        filetypes=(("pdf files", "*.pdf"), ("all files", "*.*"))
    )

    # PDF file to raw text
    raw = parser.from_file(pdf_file)
    raw_content = raw['content']
    print(raw_content)

    # Raw text to mp3 audio file
    tts = gTTS(text=raw_content, lang='en')
    tts.save('pdf-audio.mp3')
    play_btn.config(fg=TITLE_COLOR)


def play_audio():
    os.startfile('pdf-audio.mp3')


root = Tk()
root.title('PDF Text to Speech')
root.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
title_label = Label(text="PDF Text to Speech", font=(TITLE_FONT, 54, "bold"), fg=TITLE_COLOR, bg=BACKGROUND_COLOR)
title_label.grid(column=0, row=0, pady=40)
open_btn = Button(text="1. Select PDF", font=(WORD_FONT, 35), width=15, fg=WORD_COLOR, bg=BTN_BACKGROUND_COLOR,
                  command=open_pdf)
play_btn = Button(text="2. Play Audio", font=(WORD_FONT, 35), width=15, fg=WORD_COLOR, bg=BTN_BACKGROUND_COLOR,
                  command=play_audio)
open_btn.grid(column=0, row=1, pady=5)
play_btn.grid(column=0, row=2, pady=5)
root.mainloop()
