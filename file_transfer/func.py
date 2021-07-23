# Required modules
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import tkinter as tk
import shutil
import os
import time
from datetime import datetime, timedelta

# Custom modules
import main
import gui

def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# this function get's the file path to pull from
def browse_from_button(self):
    folder_path = self.from_folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)

# this functions gets the file path to pull to
def browse_to_button(self):
    folder_path = self.to_folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)

# this is our main function that will process the files that need to be transfered.
def process_files(self):
    from_folder = self.from_folder_path.get()
    to_folder = self.to_folder_path.get()

    if from_folder == '':
        messagebox.showerror(title="Error", message="Please select the file path you would like to pull from.")
        return
    elif to_folder == '':
        messagebox.showerror(title="Error", message="Please select the file path you would like to place the files.")
        return
    elif from_folder == to_folder:
        messagebox.showerror(title="Error", message="'From' and 'To' file paths are the same.")
        return

    filesFrom = os.listdir(from_folder)
    filesTo = os.listdir(to_folder)

  

    timecheck = datetime.now() - timedelta(hours=24)
    timenow = datetime.now()
    
    

    for a in filesFrom:
        timestampA = os.path.getmtime(from_folder + '/' + a)
        timestampB = datetime.fromtimestamp(timestampA)
    # if statement for finding if modification time was less than(greater than) 24 hours ago
        if timestampB > timecheck:
             shutil.move(os.path.join(from_folder, a), to_folder)
        
            
        
    
    messagebox.showinfo(title="Success", message="Files were successfully processed!")

if __name__ == '__main__':
    pass
