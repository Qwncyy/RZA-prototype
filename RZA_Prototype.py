import tkinter as tk
from tkinter import *
from customtkinter import *
import customtkinter
import PIL
from PIL import Image, ImageTk
import os
from functools import partial
from Images import *   

class TabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.home_tab()
        self.animal_tab()
        


        self.ticket_tab = self.add("Tickets")
        self.hotel_tab = self.add("Hotels")
        self.educational_tab = self.add("Educational Visits")

    def animal_tab(self):
        self.animaltab = self.add("Animals")
        self.lions_image = customtkinter.CTkImage(Image.open("Images/lioness-cubs-shem-compion-786x500.png"), size = (400, 200))
        home_image = customtkinter.CTkLabel(self.animaltab, anchor = "se", image= self.lions_image, text = "" )
        home_image.pack(padx = 0, pady = 0)

        animal_text_box = customtkinter.CTkTextbox(master = self.animaltab, width=400)
        animal_text_box.pack(padx=50, pady=50)
        animal_text_box.insert("0.0", "Come see our vast range of animals wether it be lions, snow leopards or elephants, Riget Zoo Adventures provides a wide variety of weird and wonderful animals! ")



    def home_tab(self):
        self.hometab = self.add("Home")
        self.homeframe = customtkinter.CTkScrollableFrame(master=self.hometab, fg_color="white")
        self.homeframe.pack(fill ="both", expand = True)
        self.leopard_image = customtkinter.CTkImage(Image.open("Images/Leopard.png"), size = (400, 200))
        home_image = customtkinter.CTkLabel(self.homeframe, anchor = "se", image= self.leopard_image, text = "" )
        home_image.pack(padx = 0, pady = 0)


        introductory_text_box = customtkinter.CTkTextbox(master=self.homeframe , width = 400, fg_color="#000000" )
        introductory_text_box.pack(padx = 0, pady=0)
        introductory_text_box.insert("0.0", "Welcome to the Riget Zoo Adventures official page! Release your wild side at RZA by booking tickets for day passes,booking at one of our premium lodges or purchasing the renewing membership for free tickets! ")
  
        self.home_tickets_image = customtkinter.CTkImage(Image.open("Images/FamilyAtZoo.png"), size = (450 ,200) )
        ticket_on_home = customtkinter.CTkLabel(self.homeframe,anchor = "ne", image = self.home_tickets_image, text = "")
        ticket_on_home.pack(padx = 50, pady = 50,)
        ticket_on_home_button = customtkinter.CTkButton(self.homeframe, text= "View ticket types",)
        ticket_on_home_button.pack(padx=40, pady=40)
        animal_image_text_box = customtkinter.CTkTextbox(master=self.homeframe , width = 450, fg_color="#0F5132" )
        animal_image_text_box.pack(padx = 40, pady=40)
        animal_image_text_box.insert("0.0", "Day passes allow you to visit the zoo and see some of the attractions, there are different tickets  allowing for different experiences")



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.Startup()
        #self.background()
        #self.sidebar()

        self.tab_view = TabView(master=self, fg_color ="#0F5132")
        self.tab_view.pack(fill = "both", expand = True, padx=20, pady=10)


        customtkinter.set_default_color_theme("green")
        customtkinter.set_appearance_mode('dark')

        self.iconbitmap("Images/Riget zoo logo.ico")


    def Startup(self):
        #Setup the theme and colours

        #Size and title of the website
        self.title('Riget Zoo Adventures')
        self.geometry('450x600')
 
    
        

    

            

def main():
    home = App()
    

    home.mainloop()
main()


