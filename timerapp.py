import tkinter as tk 

#gui section

#colors
label_color="#FFFFFF"
frame_color = "#2471A3"
btn_fg_color = "#FFFFFF"
start_btn_bg = "#0BB8E2"
stop_btn_bg = "#F34545"
reset_btn_bg = "#17B974"
#fonts
btn_font = "Courier 10 bold"

#window initialization
window = tk.Tk()
#title of the window
window.title("Timer")
#resizable and responsive window
window.rowconfigure(0, minsize=1, weight=0) #weight 0 means the elements are non resizable #Take a look at line 6 more closely. The minsize parameter of .rowconfigure() is set to 800 and weight is set to 1. The first argument is 0, which sets the height of the first row to 800 pixels and makes sure that the height of the row grows proportionally to the height of the window. There’s only one row in the application layout, so these settings apply to the entire window.
window.columnconfigure(0, minsize=1, weight=0) #Here, you use .columnconfigure() to set the width and weight attributes of the column with index 1 to 800 and 1, respectively:. Remember, row and column indices are zero-based, so these settings apply only to the second column. By configuring just the second column, the text box will expand and contract naturally when the window is resized, while the column containing the buttons will remain at a fixed width.
window.resizable(False, False) # the main window is non resizable
#border effects
border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

#main frame
frame_taskbar = tk.Frame(
    master=window,
    relief=tk.FLAT,
    bg = frame_color,
    borderwidth=2
)
#entry section frame
entry_frame = tk.Frame(
    master=frame_taskbar,
    relief = tk.SUNKEN,
    borderwidth=2
)

#label for hour
lbl_hr = tk.Label(master=entry_frame, text="00")
#label for minute
lbl_min = tk.Label(master=entry_frame, text="00")
#label for second
lbl_sec = tk.Label(master=entry_frame, text="00")
#label for colon between hour and minute
lbl_cln1 = tk.Label(master=entry_frame, text=" : ")
#label for colon between minute and second
lbl_cln2 = tk.Label(master=entry_frame, text=" : ")
#button for start
start_button = tk.Button(
    master = entry_frame,
    text="Start",
    bg = start_btn_bg,
    fg = btn_fg_color,
    font=(btn_font)
)
#button for stop
stop_button = tk.Button(
    master = entry_frame,
    text="Stop",
    bg = stop_btn_bg,
    fg = btn_fg_color,
    font=(btn_font)
)
#button for reset
reset_button = tk.Button(
    master = entry_frame,
    text="Reset",
    bg = reset_btn_bg,
    fg = btn_fg_color,
    font=(btn_font)
)
#geometry manager to set up entry frame
lbl_hr.grid(row=0, column=0, sticky="nwse")
lbl_cln1.grid(row=0, column=1, sticky="nwse")
lbl_min.grid(row=0, column=2, sticky="nwse")
lbl_cln2.grid(row=0, column=3, sticky="nwse")
lbl_sec.grid(row=0, column=4, sticky="nwse")
start_button.grid(row=1, column=0, sticky="nswe")
stop_button.grid(row=1, column=2, sticky="nswe")
reset_button.grid(row=1, column=4, sticky="nswe")
entry_frame.grid(row=0, column=0, sticky="nswe", padx=5, pady=7)
frame_taskbar.grid(row=0, column=0, sticky="nswe", padx=1, pady=1)


global count
count =0
class App():
    
    def reset(self):
        global count
        count=1
        lbl_hr["text"] = "00"
        lbl_min["text"] = "00"
        lbl_sec["text"] = "00"
        
    def start(self):
        global count
        count=0
        self.start_timer()
    
    def start_timer(self):
        global count
        self.timer()
    def stop(self):
        global count
        count=1
        
        
    def timer(self):
        global count
        if(count==0):
            
            h = int(lbl_hr["text"])
            m = int(lbl_min["text"])
            s = int(lbl_sec["text"])
            
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    h+=1
                    m = 0
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            
            lbl_hr["text"] = h
            lbl_min["text"] = m
            lbl_sec["text"] = s
            
            
            if(count==0):
                window.after(930,self.start_timer)
            
        
    def __init__(self):
        
        start_button["command"] = self.start 
        stop_button["command"] = self.stop 
        reset_button["command"] = self.reset           
        


    

# main function
if __name__ == "__main__":
    a = App()
    #without mainloop, nothing will be shown
    window.mainloop()
    