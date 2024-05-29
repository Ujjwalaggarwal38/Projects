import tkinter as tk
from tkinter import filedialog,messagebox
def new_file():
    text.delete(1.0,tk.END)
    
def open_file():
    file_path=filedialog.askopenfilename(defaultextension='.txt',filetypes=[("Textfiles","*.txt")])
    if file_path:
        with open(file_path,'r') as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END,file.read())
            
def save_file():
    file_path=filedialog.asksaveasfilename(defaultextension='.txt',filetypes=[("Textfiles","*.txt")])
    if file_path:
        with open(file_path,'w') as file:
            file.write(text.get(1.0,tk.END))
            messagebox.showinfo("Info",'File Saved successfully')
                   
root=tk.TK()
root.title('Text Editor')
root.geomery('800*600')

menu=tk.Menu(root)
root=config(menu=menu)
file_menu=tk.Menu(menu)
menu.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label='NEW',command=new_file)
file_menu.add_command(label='OPEN',command=open_file)
file_menu.add_command(label='SAVE',command=save_file)
file_menu.add_separator()
file_menu.add_command(label='EXIT',command=root.quit)

text=tk.Text(root,wrap=tk.WORD,font=('Times New Roman',12),fg='Blue')
text.pack(expand=tk.YES,fill=tk.BOTH)

root.mainloop()




