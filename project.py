from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)

root.configure(backgroun = "gray87")

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img =ImageTk.PhotoImage(Image.open("exit.jpg"))

label_file_name = Label(root, text = "File name")
label_file_name.place(relx = 0.28, rely = 0.03, anchor = CENTER)

input_file_name = Entry(root)
input_file_name.place(relx = 0.46, rely = 0.03, anchor = CENTER)

my_text = Text(root, height = 35, width = 80)
my_text.place(relx = 0.5, rely = 0.55, anchor = CENTER)


name = ""
def openFile():
    global name
    my_text.delete(1.0, END)
    input_file_name.delete(0,END)
    html_file = filedialog.askopenfilename(title = "Open html File", filetypes =
                                           (("html Files", "*.html"),))
    print(html_file)
    name = os.path.basename(html_file)
    formated_name = name.split('.')[0]
    input_file_name.insert(END,formated_name)
    root.title(formated_name)
    html_file = open(name,'r')
    paragraph = html_file.read()
    my_text.insert(END,paragraph)
    text_file.close()

open_button = Button(root, image = open_img,text="OpenFile", command = openFile)
open_button.place(relx = 0.05, rely = 0.03, anchor = CENTER)

root.mainloop()
