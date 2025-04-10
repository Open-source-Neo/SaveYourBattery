#!/usr/bin/python3

import tkinter as tk
import psutil
import subprocess
import time
from tkinter import simpledialog

root = tk.Tk()
root.geometry("300x200")
#Define the size of the window 

root.title("Battery Limiter")
#Define the title of the window

label = tk.Label(root, text="Battery Limiter", font =('Ubuntu',18))
label.pack(padx=20, pady=20)
#create a label

def send_notification(title, message):
    subprocess.run(['notify-send', title, message])

def input():
    #my_i=simpledialog.askstring("input","Do you want to change the value? (1 for yes, 0 for no)",parent=root)
    #choice=my_i
    #if choice == '1' :

    my_i=simpledialog.askinteger("input","Enter the lowest battery percentage",parent=root)
    value=my_i
    return value
    
def choice():
    my_i=simpledialog.askinteger("input","Enter the lowest and highest battery percentage",parent=root)
    
#voglio aggiungere una funzione che permette una scelta di modificare i valori.
    
def battery_notification():

            battery = psutil.sensors_battery()
            if battery.percent <= int_min:
                send_notification("Too low", f"Battery level is at {battery.percent}%.")

            
            if battery.percent >= int_max:
                send_notification("Too high", f"Battery level is at {battery.percent}%.")
            root.after(10000, battery_notification)
#I need to find a way to cicle this operation without blocking the GUI

button = tk.Button(root, text="Exit", command=quit)
button.pack()
int_min=input()
int_max=input()
battery_notification()




root.mainloop()








