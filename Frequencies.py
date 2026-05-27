# Make an app that allows you to select a frequency and play it

import customtkinter as ctk
import winsound
import numpy
import sounddevice as sd
from customtkinter import *

def only_numbers(char):
    # Returns True if the character is a digit or an empty string
    return char.isdigit() or char == ""

ENABLED = False
Audio = None

# Set app appearance and theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Frequency Generator")
app.geometry( "300x200" )

# Valide the text as numbers | Validation command
vcmd = (app.register(only_numbers), '%S')

entry1 = ctk.CTkEntry(master=app, placeholder_text="Frequency", corner_radius=5, border_color="black", border_width=3, width=100, height=30,validate='key', validatecommand=vcmd)
entry1.pack( pady=40, padx=10 )

def generateSound():
    print("clicked")
    if ENABLED:
        print("disabled")
        Audio.Stop()
        Audio = None
    else:
        print("enabled")
        frequency = int(entry1.get())
        
        t = numpy.linspace(0, 1, int(44100 * 1), endpoint = False)
        audio_data = numpy.sin(2 * numpy.pi * frequency * t)
        
        Audio = sd.play(audio_data)
        #button_text = "Stop"
    
button_text = "Generate" # Defaults the text
button_var = ctk.StringVar(value=button_text)
button = ctk.CTkButton( master=app,textvariable=button_var, width=150, height=30, border_color="black", border_width=3, corner_radius=5, command=generateSound )
button.pack( pady=5, padx= 8 )

app.mainloop()
