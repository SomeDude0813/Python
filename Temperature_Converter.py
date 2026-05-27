# input temperature

# output converted temperature

""" PATH
    learn how to make a terminal version of the temperatuer converter
    
    remake the temperature converter with tkinter as a gui
    
    
"""

import customtkinter as ctk



SIZE = "300x150" # Width x Height
TITLE = "Temperature Converter"

def only_numbers(char):
    # Returns True if the character is a digit or an empty string
    return char.isdigit() or char == ""

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.geometry(SIZE)
        
        # Valide the text as numbers | Validation command
        validatecmd = (self.register(only_numbers), '%S')
        
        # Set up widgets
        self.arrow_image = ctk.CTkLabel(self, width=50, height=50, text="🠖", font=("Courier New", 40)) # Arrow in the middle of the screen
        self.arrow_image.place( x=125, y=60 )
        
        self.temperature_entry = ctk.CTkEntry(self, width=50,height=50, validate="key", validatecommand=validatecmd) # The entry box for the temperature
        self.temperature_entry.place( x=50, y=60 ) 
        
        self.entry_type = ctk.CTkOptionMenu(self, values=["°F", "°C", "°K"], width=75) # The type of temperature that will be converted
        self.entry_type.place(x=40, y=25)
        
        self.converted_temperature = ctk.CTkLabel(self, width=50,height=50,text="0", fg_color="gray" ) # The output of the converted temperature
        self.converted_temperature.place(x=200, y=60)
        
        self.conversion_type = ctk.CTkOptionMenu(self, values=["°C", "°F", "°K"], width=75) # The type of temperature the entry will be converted to
        self.conversion_type.place(x=185, y=25)
#        ---------------------------------------------------------------------------------------------------------------------------------------------------------
        def on_entry(event): # Convert the temperature as the user types it
            entry_value = int(event.widget.get())
            if entry_value == "":
                return
            
            entry_type = self.entry_type.get()
            conversion_type = self.conversion_type.get()
            
            if entry_type == conversion_type: # Makes sure they dont have the same type selected for entry and conversion
                return
            
            # Calculate the converted temperature
            ''' Conversion Formula
            
                Celsius to Fahrenheit: °F = (°C * 1.8) + 32
                Fahrenheit to Celsius: °C = (°F - 32) ÷ 1.8
                Celsius to Kelvin: K = °C + 273.15
                Kelvin to Celsius: °C = K - 273.15
                Fahrenheit to Kelvin: K = (°F - 459.67) * 5/9
                Kelvin to Fahrenheight: °F = K * 9/5 - 459.67
            '''
            
            converted_value = 0
            
            match entry_type:
                case "°F":
                    if conversion_type == "°C":
                        converted_value = (entry_value - 32) + 1.8
                    elif conversion_type == "K":
                        converted_value = (entry_value - 459.67) * 5/9
                case "°C":
                    if conversion_type == "°F":
                        converted_value = ( entry_value * 1.8 ) + 32
                    elif conversion_type == "K":
                        converted_value = entry_value + 273.15
                        
                case "K":
                    if conversion_type == "°F":
                        converted_value = entry_value * 9/5 - 459.67
                    elif conversion_type == "°C":
                        converted_value = entry_value - 273.15
                    
            
            self.converted_temperature.configure(text=converted_value) # Update the text of the converted temperatue widget
        
        self.conversion_type.configure(command=on_entry)
        self.temperature_entry.bind("<KeyRelease>", on_entry) # On key release activate function
app = App()
app.mainloop()