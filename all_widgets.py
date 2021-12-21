"""
Implement the widgets on the right frame for EDD calculation app. This builds on left_widget.py
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
        #image source https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fillustrations%2Fpregnant&psig=AOvVaw3Ed_YWfg460hZNsUeAns-V&ust=1636306992268000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCKiZxMGrhPQCFQAAAAAdAAAAABAE
        self.pic_label = self.create_pic()
        self.title = self.create_title()
        self.message = self.create_message()
        self.text_box = self.create_box()
        self.calc_button = self.create_button()
        
        
    def create_frames(self):
        pic_frame = tk.Frame(self.window, bg='pink')  #removed dimension of frame as the widget in this frame will now dictate the size
        pic_frame.grid(row=1, column=1)
        
        calc_frame = tk.Frame(self.window, bg='pink', width=500)
        calc_frame.grid(row=1, column=2, sticky=tk.E + tk.W + tk.N + tk.S)   #added sticky to stretch out this frame to meet the height of the left 
        
        return pic_frame, calc_frame
    
    def create_pic(self):
        pic_label = tk.Label(self.pic_frame, image = self.pic_photo)
        pic_label.grid(row=1, column=1)   #specifying location using grid layout
        return pic_label
    
    def create_title(self):
        title = ttk.Label(self.calc_frame, text = "EDD CALCULATOR",
                          background = "pink", font=('calibri', 34) ,justify = 'center'
                          )
        title.pack(side = tk.TOP, pady = 100)
        return title
    
    def create_message(self):
        message = tk.Message(self.calc_frame, text = "Please enter your Last Menstrual Period in the format below.\n(DD-MM-YYYY)")
        message.pack(side = tk.TOP, ipadx = 20, pady = 10 )
        message.config(bg='pink', font=('calibri', 12), width = 500, justify="center")
        return message
    
    def create_box(self):
        text_box = ttk.Entry(self.calc_frame )
        text_box.pack(side = tk.TOP, ipadx = 50)
        return text_box
        
    def create_button(self):
        calc_button = ttk.Button(self.calc_frame, text="Calculate  EDD")
        calc_button.pack(side = tk.TOP, pady = 10 )
        return calc_button
    
 
if __name__ == '__main__':
    main()        

