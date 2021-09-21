import os
import pickle
import shutil
import time
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import custom
import configparser
import re



root=Tk()
root.title('File Organizer')


my_notbook=ttk.Notebook(root)
frame1=Frame(my_notbook,width=1920,height=1080)
frame2=Frame(my_notbook)
frame3=Frame(my_notbook)
filelocation=""
files=''
image_foramt=list()
video_format=list()
audio_format=list()
document_format=list()
count=0

def goto_path():
    global filelocation
    filelocation =filedialog.askdirectory(initialdir='c:/', title='select path')
    path=Label(frame1,text=filelocation)
    path.grid(row=10,column=1)
    proccess_btn = Button(frame1, text="Manage my files")
    proccess_btn.bind("<Button-1>",proccess)
    proccess_btn.grid(row=12,column=0,columnspan=5)



def proccess(event):
    global filelocation,count
    files = os.listdir(filelocation)
    files_count=len(files)
    progress_bar = ttk.Progressbar(frame1, orient=HORIZONTAL, length=files_count, mode='determinate')
    progress_bar.grid(row=25,column=4)

    for file in files:
        exet = file.split('.')[-1].lower()
        print(exet)
        if exet in image_foramt:
            if "images" in files:
                replacement(file, filelocation, "images")

            else:
                os.mkdir(f'{filelocation}/images')
                files = os.listdir(filelocation)
                shutil.move(f'{filelocation}/{file}', f'{filelocation}/images/{file}')

        elif exet in video_format:
            if "videos" in files:
                replacement(file, filelocation, "videos")

            else:
                os.mkdir(f'{filelocation}/videos')
                files = os.listdir(filelocation)
                shutil.move(f'{filelocation}/{file}', f'{filelocation}/videos/{file}')

        elif exet in audio_format:
            if "audios" in files:
                replacement(file, filelocation, "audios")

            else:
                os.mkdir(f'{filelocation}/audios')
                files = os.listdir(filelocation)
                shutil.move(f'{filelocation}/{file}', f'{filelocation}/audios/{file}')

        elif exet in document_format:
            if "books" in files:
                replacement(file,filelocation,"books")

            else:
                os.mkdir(f'{filelocation}/books')
                files = os.listdir(filelocation)
                shutil.move(f'{filelocation}/{file}', f'{filelocation}/books/{file}')

        count=count+1
        count_label = Label(frame1, text=f'{count}/{files_count}')
        count_label.grid(row=18,column=1)
        print(f'{count}/{files_count}')
        progress_bar['value']+=1
        root.update_idletasks()
        progress_label = Label()
        progress_label.config(text=progress_bar)


    # progress_count = Label(frame1, text=f"{count}/{files_count}")
    # progress_count.grid(row=16,column=0)
    # print(progress_count)
    label_complete=Label(frame1,text="complete")
    label_complete.grid(row=18,column=0)
    print("complete")

def replacement(file,file_loc,folder):
    try:
        location=f'{file_loc}/{folder}'
        files = os.listdir(location)
        print(files)
        print("replacement")

        if file in files:
            # Path
            os.replace(location,f'{location}/{file}')


        else:
            print(filelocation)
            print(f'{location}/{file}')
            shutil.move(f'{file_loc}/{file}', f'{location}/{file}')
    except:
        print("Error")
        # renamed the file f.txt to d.txt

img_label=Label(frame1,text="Chose image format",padx=10)
video_label=Label(frame1,text="Chose video format",padx=10)
audio_label=Label(frame1,text="Chose mp3 format",padx=10)
document_label=Label(frame1,text="Chose document format",padx=10)

jpg=StringVar()
jpeg=StringVar()
png=StringVar()
tiff=StringVar()

mp4=StringVar()
mpeg=StringVar()
gif=StringVar()
avi=StringVar()

mp3=StringVar()

doc=StringVar()
pdf=StringVar()
docx=StringVar()
txt=StringVar()

var_format={"img":['jpg','jpeg','png','tiff'],
    "video":['mp4','mpeg','gif','avi'],
    "audio":['mp3'],
    "docu":['doc','pdf','docx','txt']
      }


#image_types
jpg_f=Checkbutton(frame1,text="jpg",variable=jpg,onvalue="jpg",offvalue="Off")
jpeg_f=Checkbutton(frame1,text="jpeg",variable=jpeg,onvalue="jpeg",offvalue="Off")
png_f=Checkbutton(frame1,text="png",variable=png,onvalue="png",offvalue="Off")
tif_f=Checkbutton(frame1,text="tif",variable=tiff,onvalue="tif",offvalue="Off")
label0=Label(frame1,text=jpg.get())
label0.grid(row=10,column=0)

#video types
mp4_f=Checkbutton(frame1,text="mp4",variable=mp4,onvalue="mp4",offvalue="Off")
mpeg_f=Checkbutton(frame1,text="mpeg",variable=mpeg,onvalue="mpeg",offvalue="Off")
avi_f=Checkbutton(frame1,text="mpeg",variable=avi,onvalue="avi",offvalue="Off")
gif_f=Checkbutton(frame1,text="gif",variable=gif,onvalue="gif",offvalue="Off")

#audio types
mp3_f=Checkbutton(frame1,text="mp3",variable=mp3,onvalue="mp3",offvalue="Off")

#document types
doc_f=Checkbutton(frame1,text="doc",variable=doc,onvalue="doc",offvalue="Off")
pdf_f=Checkbutton(frame1,text="pdf",variable=pdf,onvalue="pdf",offvalue="Off")
docx_f=Checkbutton(frame1,text="docx",variable=docx,onvalue="docx",offvalue="Off")
txt_f=Checkbutton(frame1,text="txt",variable=txt,onvalue="txt",offvalue="Off")
var=[jpg,jpeg,png,tiff,mp4,mpeg,avi,gif,mp3,doc,docx,pdf,txt]


img_label.grid(row=0,column=0)
video_label.grid(row=0,column=1)
audio_label.grid(row=0,column=2)
document_label.grid(row=0,column=3)


jpg_f.grid(row=1,column=0)
jpg_f.deselect()
jpeg_f.grid(row=2,column=0)
jpeg_f.deselect()
png_f.grid(row=3,column=0)
png_f.deselect()
tif_f.grid(row=4,column=0)
tif_f.deselect()

mp4_f.grid(row=1,column=1)
mp4_f.deselect()
mpeg_f.grid(row=2,column=1)
mpeg_f.deselect()
avi_f.grid(row=3,column=1)
avi_f.deselect()
gif_f.grid(row=4,column=1)
gif_f.deselect()

mp3_f.grid(row=1,column=2)
mp3_f.deselect()

doc_f.grid(row=1,column=3)
doc_f.deselect()
pdf_f.grid(row=2,column=3)
pdf_f.deselect()
docx_f.grid(row=3,column=3)
docx_f.deselect()
txt_f.grid(row=4,column=3)
txt_f.deselect()
def select():
    # label0 = Label(root, text=jpg.get())
    # label0.grid(row=10, column=0)
    print(var_format["img"])
    for p in var:
        print(p.get())
        if p.get() in var_format["img"]:
            image_foramt.append(p.get())
        elif p.get() in var_format["video"]:
            video_format.append(p.get())
        elif p.get() in var_format["audio"]:
            audio_format.append(p.get())
        if p.get() in var_format["docu"]:
            document_format.append(p.get())
        path_btn.grid(row=8, column=0, columnspan=5)

select_btn=Button(frame1,text="Select",command=select)
path_btn=Button(frame1,text="path", command=goto_path)
select_btn.grid(row=7,column=0,columnspan=5,ipadx=100,pady=10,padx=10)
my_menue=Menu(root)
root.config(menu=my_menue)

def command():
    label=Label(text='Menu tab select')
    label.pack()

custom_file_with_extension = dict()
customize_dict=dict()

def save_list():
    with open('Customize_list.pkl', 'ab+') as file:
        pickle.dump(customize_dict,file)

objs=[]
with open('Customize_list.pkl','rb') as f:
    while 1:
        try:
            objs.append(pickle.load(f))

        except EOFError:
            break


def remove_list():
    pass



j = 0
def customize_add():
    global j

    c_filename=file_name.get()
    c_file_ext=extensions.get().split(" ")
    custom_file_with_extension[c_filename]=c_file_ext
    customize_dict.update(custom_file_with_extension)
    file_name.delete(0,END)
    extensions.delete(0,END)
    label_file=Label(frame2,text="file name")
    label_file.grid(row=3,column=0)
    label_file_extension = Label(frame2,text="extension")
    label_file_extension.grid(row=3, column=1)

    for i in range(len(customize_dict.keys())):
        file_l=Label(frame2,text=list(customize_dict.keys())[i])
        file_l.grid(row=i+4,column=0)
        extensions_l=Label(frame2,text=list(customize_dict.values())[i])
        extensions_l.grid(row=i+4,column=1)




# CUSTOMIZE TAB UI
file_name_label=Label(frame2,text="Enter File name")
file_name=Entry(frame2)
file_name_label.grid(row=0,column=0)
file_name.grid(row=1,column=0,padx=10,ipadx=10)
extensions_label=Label(frame2,text="Enter Extensions")
extensions=Entry(frame2)
extensions_label.grid(row=0,column=1)
extensions.grid(row=1,column=1,ipadx=50,padx=30,pady=30,ipady=30)
button_add=Button(frame2,text="Add",command=customize_add)
button_add.grid(row=1,column=2,padx=2,ipadx=2)

save = Button(frame2, text='save list', command=save_list)
save.grid(row=len(customize_dict.keys()) + 4, column=2)
# clear = Button(frame2, text='clear list', command=remove_list)
# clear.grid(row=len(customize_dict.keys()) + 5, column=2)
save = Button(frame2, text='save list', command=save_list)
save.grid(row=len(customize_dict.keys()) + 4, column=2)

def my_file_process(event):
    global filelocation, count
    files = os.listdir(filelocation)
    files_count = len(files)
    progress_bar = ttk.Progressbar(frame3, orient=HORIZONTAL, length=files_count, mode='determinate')
    progress_bar.grid(row=25, column=4)

    for file in files:
        exet = file.split('.')[-1].lower()
        for custom_file in all_files.keys():
            if exet in all_files[custom_file]:
                if custom_file in files:
                    replacement(file, filelocation, custom_file)
                    print("replacement")


                else:
                    print("create file")
                    os.mkdir(f'{filelocation}/{custom_file}')
                    files = os.listdir(filelocation)
                    shutil.move(f'{filelocation}/{file}', f'{filelocation}/{custom_file}/{file}')


        count = count + 1
        count_label = Label(frame3, text=f'{count}/{files_count}')
        count_label.grid(row=3,column=1)
        # print()
        progress_bar['value'] += 1
        root.update_idletasks()
        progress_label = Label()
        progress_label.config(text=progress_bar)
        # time.sleep(0.5)



def my_files_path():
    global filelocation
    filelocation = filedialog.askdirectory(initialdir='c:/', title='select path')
    path = Label(frame3, text=filelocation)
    path.grid(row=1, column=2)
    proccess_btn = Button(frame3, text="Manage my files")
    proccess_btn.bind("<Button-1>",my_file_process)
    proccess_btn.grid(row=2, column=2, columnspan=5)


#My file UI
all_files=dict()
for i in range(len(objs)):
    all_files.update(objs[i])
global check

for i in range(len(all_files)):

    Label(frame3,text=str(list(all_files.keys())[i])).grid(row=i,column=0,pady=2)
    Label(frame3,text=str(list(all_files.values())[i])).grid(row=i,column=1,pady=5,padx=10,ipady=5)

    # check=Checkbutton(frame3, text=str(list(all_files.keys())[i]), variable=list(all_files.keys())[i], onvalue=str(list(all_files.keys())[i])+'on', offvalue=str(list(all_files.keys())[i])+'off').grid(row=0,column=i)



print(all_files)

btn_my_files_select=Button(frame3,text="select path",command=my_files_path)
btn_my_files_select.grid(row=0,column=2,padx=5,ipady=5,ipadx=5,columnspan=5)









#Create menue tabs
file_menu=Menu(my_menue)
my_menue.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="new", command=command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

about_menu=Menu(my_menue)
my_menue.add_cascade(label="About",menu=about_menu)
about_menu.add_command(label="Version 0.1")
about_menu.add_command(label="Made by- Dilshan Madhuranga")

my_notbook.add(frame1,text="Quick")
my_notbook.add(frame2,text="Customize")
my_notbook.add(frame3,text="My files")
my_notbook.pack(pady=20)
root.mainloop()


print(filelocation)




