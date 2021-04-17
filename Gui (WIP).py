from tkinter import *

class Gui(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg = "grey")
        master.attributes("-fullscreen", True)
        self.setUpGui()


    def setUpGui(self):
        # label
        self.display = Label(self, text = "{put city here}", anchor = "center", bg = "white",\
            height = 1, width = 15, font = ("Courier New", 45))
        self.display.grid(row  = 0, column = 0, columnspan = 4,\
            sticky = N + E + W + S)

        # configures the rows for use
        for row in range(6):
            Grid.rowconfigure(self, row, weight = 1)
        # configures the columns for use
        for col in range(4):
            Grid.columnconfigure(self, col, weight = 1)

        label = Label(self, bg = "white", borderwidth = 0,\
            highlightthickness = 1)
        
        self.pack(fill = BOTH, expand = 1)



############################MAIN##############################
window = Tk()

window.title("The Accurack")

p = Gui(window)

window.mainloop()