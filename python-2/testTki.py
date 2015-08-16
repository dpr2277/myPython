# Tkinter root example
#/usr/bin/python

import Tkinter
#import Tkinter.Tkconstants

tk = Tkinter.Tk()
frame1 = Tkinter.Frame(tk)
frame1.pack()
label1 = Tkinter.Label(frame1, text="Hello, World")
label1.pack(side = "top")
txtbox1 = Tkinter.Entry(frame1,width=26,textvariable="Please type here!!!")#
txtbox1.pack()
#txtbox1.pack(side=LEFT)
btOk = Tkinter.Button(frame1,text="Ok",command=None)
btOk.pack(side = "left")
btExit = Tkinter.Button(frame1,text="Exit",command=tk.destroy)
btExit.pack(side = "right")

tk.mainloop()
