from tkinter import *


class converter:

  def __init__(self):

    # Set up GUI Frame
    self.temp_frame = Frame(padx=10, pady=10)
    self.temp_frame.grid()

    
    self.temp_heading = Label(self.temp_frame,
                              text="Temperature Converter",
                              font=("Arial", "16", "bold")
                             )
    self.temp_heading.grid(row=0)

    
    instuctions = "Please enter a tempertaure below and then press one of the buttons to convert it from centigrade to fahrenheit"
    self.temp_instructions = Label(self.temp_frame,
                                   text=instuctions,
                                   wrap=250,
                                   width=40,
                                   justify="left"
                                  )
    self.temp_instructions.grid(row=1)


    self.temp_entry = Entry(self.temp_frame,
                           font=("Arial", "14")
                           )
    self.temp_entry.grid(row=2, padx=10, pady=10)


    error = "Please enter a number"
    self.temp_error = Label(self.temp_frame, text=error,
                           fg="#9C0000")
    self.temp_error.grid(row=3)

    # Conversion, help and history / export buttons
    self.button_frame = Frame(self.temp_frame)
    self.button_frame.grid(row=4)

    self.to_celsius_button = Button(self.button_frame,
                                   text= "To Degrees C",
                                   bg="#990099",
                                   fg="#FFFFFF"
                                   )
    self.to_celsius_button.grid(row=0, column=0)
    
    self.to_farenheit_button = Button(self.button_frame,
                                   text= "To Farenheit",
                                   bg="#009900",
                                   fg="#FFFFFF"
                                   )
    self.to_farenheit_button.grid(row=0, column=1)






# Main Routine
if __name__ == "__main__":
  root = Tk()
  root.title("Temperature Converter")
  converter()
  root.mainloop()
