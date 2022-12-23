

from times import *


# Initialize an object 'window' and set title
window = tk.Tk()

# Window title
window.title("Metro Timer")

# Window Size
window.geometry('1800x1000')

# Store size of window
width = window.winfo_screenwidth()
height = window.winfo_screenheight()


# Description 
desc = Label(window,
                 text="The four next departing metros going to Espoo",
                 font=("Comic Sans", 25))
desc.place(x=width/3,y=height/3)


# Place timesc
def setTimes():
   time1 = Label(window, text=times[0]).place(x=330, y=1000/(1+1))
   time2 = Label(window, text=times[1]).place(x=660, y=1000/(1+1))
   time3 = Label(window, text=times[2]).place(x=990, y=1000/(1+1))
   time4 = Label(window, text=times[3]).place(x=1320, y=1000/(1+1))
   # After 1000ms set times again
   window.after(1000, setTimes)


# Initial run to set times
setTimes()


# Main function to run the window
window.mainloop()
