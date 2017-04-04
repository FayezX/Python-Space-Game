from Tkinter import *
from PIL import ImageTk, Image
import os
import tkFileDialog

#global data and results dir you need to use variables to connect with main system.
data_dir = ''
results_dir = ''

#select input directory
def Input():
    root = Tk()
    root.withdraw()
    data_dir = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory with the images to be analyzed.')
    data_dir=data_dir + '/*.png'

#select output directory
def Output():
    root = Tk()
    root.withdraw()
    results_dir = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory to  save the results of analysis.')
    results_dir=results_dir+ '/'

def gui_build():
    #creating the window
    root = Tk();

    #change root window
    root.title("SPD START UP");
    root.resizable(width=False,height = False);
    root.geometry("950x650");
    root.configure(bg = 'gray');

    lab= Label(root, text = 'Instruction:\n\n Step 1:Click input button and select input directory\n\n Step 2:Click output button and select output directory\n\n Step 3:click run for results')
    lab.config(width=200, height = 0);
    lab.config(font=("Courier", 25));
    lab.pack(side = "top",fill= NONE);
   
    #created click to run button
    run_button_input = Button(root, text = "Input Folder", width = 20,height = 0,command = Input);
    run_button_input.pack(side="left",padx=15,pady=15);
    
    #created click to run button
    run_button_output = Button(root, text = "Output Folder", width = 20,height = 0,command = Output);
    run_button_output.pack(side="right",padx=15,pady=15);
    
    #created click to run button
    run_button = Button(root, text = "Click to run", width = 20,height = 0,command = root.destroy);
    run_button.pack(side="bottom",padx=15,pady=15);
    
    #run it
    root.mainloop();

if __name__ == '__main__':
    gui_build();
