import time 
import random
import tkinter as tk
from tkinter import messagebox


class DoomPet:
    def __init__(self,name):
        self.name=name
        self .__emotion="Hopeful"
        self .__time_in_blackhole= 0
        self .__dreams=[
              "you are the light that gives meaning to my darkness.",
              "You words  are  fill the void inside me.",
              "Has time stopped here, or were you just too late?",
              "I saw your reflection in a dream, like a streak of light."
              
              ]
    def talk(self):
        self .__emotion="Happy"
        self .__time_in_blackhole += 1
        return f"{self.name} replied: I m listenind..."
    
    def ignore(self):
        self .__emotion="lonely"
        self .__time_in_blackhole += 100
        return f"{self.name} is now silent...Time is speeding up."
    
    def dream(self):
        return  random.choice(self.__dreams)
    
    def status(self):
        return f"{self.name} 's state:Emotion = {self.__emotion},Time={self .__time_in_blackhole} black seconds."

pet=DoomPet("Noor")

def on_talk():
        msg=pet.talk()
        messagebox.showinfo("Talk", msg)
        update_status()

def on_ignore():
        msg=pet.ignore()
        messagebox.showinfo("Ignore", msg)
        update_status()

def on_dream():
        msg=pet.dream()
        messagebox.showinfo("Dream", msg)
        
def update_status():
        status_label.config(text=pet.status()) 

root = tk.Tk()

root.title("Doom Pet") 
root.geometry("400x300")  

status_label = tk.Label(root, text=pet.status(), wraplength=350, justify="left")
status_label.pack(pady=10)
talk_button = tk.Button(root, text="Talk", command=on_talk)
talk_button.pack(pady=5)

ignore_button = tk.Button(root, text="Ignore", command=on_ignore)
ignore_button.pack(pady=5)

dream_button = tk.Button(root, text="Dream", command=on_dream)
dream_button.pack(pady=5)

root.mainloop()   
     

