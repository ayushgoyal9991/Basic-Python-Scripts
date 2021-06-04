# -*- coding: utf-8 -*-
"""
Created on Sun May 30 12:01:56 2021

@author: Ayush
"""

from tkinter import *

root = Tk()
root.geometry('500x400')
root.resizable(0,0)
root.title('Website Blocker')

Label(root,text = 'Website Blocker',font='arial 20 bold').pack()

host_path = 'C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

Label(root,text="Enter Website: ",font='arial 13 bold').place(x=5,y=60)

Websites = Text(root,font = 'arial 13',height='2',width='40',wrap=WORD,padx=5,pady=5)
Websites.place(x=140,y=60)

def Blocker():
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))
    
    with open (host_path,'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                Label(root,text='Already Blocked',font='arial 12 bold').place(x=200,y=200)
                pass
            else:
                host_file.write(ip_address+" "+website+'\n')
                Label(root,text='Blocked',font='arial 12 bold').place(x=230,y=200)
                
button = Button(root,text='Block',font='arial 12 bold',pady=5,command=Blocker,width=6,bg='royal blue')
button.place(x=230,y=150)

root.mainloop()
