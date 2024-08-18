
from tkinter import *
import string
import pyperclip
import random
root = Tk()
root.config(bg='black')
root.geometry("500x400")   
passstr = StringVar()
passlen = IntVar()
passlen.set(0)
def generate():
 p1 = string.ascii_lowercase  
 p2 = string.ascii_uppercase  
 p3 = string.digits  
 p4 = string.punctuation  
 all_characters = p1 + p2 +  p3 + p4  
 password = ""
 for x in range(passlen.get()):
  password = password + random.choice(all_characters)
  passstr.set(password)
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)
Label(root, text="Password Generator Application", font=('new times roman', 20, 'bold'), bg='gray20', fg='red').pack(pady=30)
Label(root, text="Enter password length",font=('Italic', 20, 'bold')).pack(pady=5)
Entry(root, width=30, bd=5,font=('calibre',10, 'bold') ,textvariable=passlen).pack(pady=7)
Button(root, text="Generate Password",font=('arial', 13, 'bold'), command=generate).pack(pady=5)
Entry(root,width=30, bd=5,font=('calibre',10, 'bold'), textvariable=passstr).pack(pady=10)
Button(root, text="Copy to clipboard",font=('arial', 13, 'bold'),  command=copytoclipboard).pack()
Label(root, text="THANKU FOR USING", font=('Italic', 20, 'bold'), bg='gray20', fg='green').pack(pady=20)
root.mainloop()