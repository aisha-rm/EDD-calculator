"""
Implement the left side widget for EDD calculation app
"""
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import ImageTk,Image

def main():
    #creating the entire GUI promgram
    program = edd_calc()
    
    #start the GUI event loop
    program.window.mainloop()
    
class edd_calc():
    def __init__(self):
        self.window = tk.Tk()
        self.pic_frame, self.calc_frame = self.create_frames()
        self.pic_photo = ImageTk.PhotoImage(Image.open("preg.png"))
        #self.pic_photo = PhotoImage(file = "pregg.ppm") #tk only opens pgm/ppm files
        #image source https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fillustrations%2Fpregnant&psig=AOvVaw3Ed_YWfg460hZNsUeAns-V&ust=1636306992268000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCKiZxMGrhPQCFQAAAAAdAAAAABAE
        self.pic_label = self.create_pic()
        
    def create_frames(self):
        pic_frame = tk.Frame(self.window, bg='pink')
        pic_frame.grid(row=1, column=1)
        
        calc_frame = tk.Frame(self.window, bg='purple', width=500)
        calc_frame.grid(row=1, column=2, sticky=tk.E + tk.W + tk.N + tk.S)
        
        return pic_frame, calc_frame
    
    def create_pic(self):
        pic_label = tk.Label(self.pic_frame, image = self.pic_photo)
        pic_label.grid(row=1, column=1)
        return pic_label
 
if __name__ == '__main__':
    main()        

