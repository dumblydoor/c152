#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 17:37:35 2023

@author: aquilavijayanayagam
"""

from tkinter import*
import random
root=Tk()
root.title("profits")
root.geometry("400x400")



label=Label(root)
 
array1d=['jhon','james','bob']
print(array1d[0])

array2d=[['jhon','A'],['james','B'],['bob','E']]
print(array2d[0][1])

array3d=[[['jhon','A','horrible'],['james','B','bad'],['bob','E','amazing']]]
print(array3d[0][0][2])

def report():
    label["text"]= array3d[0][1][0]+"got grade"+array3d[0][1][1]+"and is doing"+array3d[0][1][2]
btn=Button(root,text="show report",command=report)
btn.place(relx=0.5,rely=0.5, anchor=CENTER)

label.place(relx=0.5,rely=0.6, anchor=CENTER)



root.mainloop
