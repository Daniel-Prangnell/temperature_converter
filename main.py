class converter:

  def __init__(self):

    # Set up GUI Frame
    self.temp_frame = Frame()
    self.temp_frame.grid()

    self.temp_heading = label(self.temp_frame, text="Temperature Converter")
                             



# Main Routine
if __name__ == "__main__":
  root = Tk()
  root.title("Temperature Converter")
  Converter()
  root.mainloop()