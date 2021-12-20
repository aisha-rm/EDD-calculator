"""
Implement a user interface for EDD calculation
"""
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

def main():
    #creating the entire GUI promgram
    program = edd_calc()
    
    #start the GUI event loop
    program.window.mainloop()
    
class edd_calc():
    def __init__(self):
        self.window = tk.Tk()
        self.pic_frame, self.calc_frame = self.create_frames()
        self.pic_photo = PhotoImage(file = "preg.png")
        
    def create_frames(self):
        pic_frame = tk.Frame(self.window, bg='pink', width=500, height=500)
        pic_frame.grid(row=1, column=1)
        
        calc_frame = tk.Frame(self.window, bg='purple', width=500, height=500)
        calc_frame.grid(row=1, column=2)
        
        return pic_frame, calc_frame
 
if __name__ == '__main__':
    main()        

