
# Shutdown app using Tkinter GUI

from tkinter import *
import os

def restart():
    os.system("Shutdown /r /t 1")
def restart_time():              
    os.system("shutdown /r /t  20")
def logout():
    os.system("shutdown -1")
def shutdown():                                        
    os.system("shutdown /s /t 1")

st = Tk() 
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg = "Pink")

r_button = Button(st, text ="Re-Start", font =("Times New Roman", 20, "bold"), relief = RAISED, cursor = "plus", command = restart)
r_button.place(x=150,y=60,height=40,width=200)

rt_button = Button(st, text ="ReStart Time", font =("Times New Roman", 20, "bold"),relief = RAISED, cursor = "plus", command = restart_time)
rt_button.place(x=150,y=150,height=40,width=200)


lg_button = Button(st, text ="Logout", font =("Times New Roman", 20, "bold"),relief = RAISED, cursor = "plus", command= logout)
lg_button.place(x=150,y=240,height=40,width=200)


st_button = Button(st, text ="Shutdown", font =("Times New Roman", 20, "bold"),relief = RAISED, cursor = "plus", command = shutdown)
st_button.place(x=150,y=330,height=40,width=200)

st.mainloop()
