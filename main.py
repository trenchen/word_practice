from tkinter import *
from gtts import gTTS
from pygame import mixer
import os


winWidth = 500
winHeight = 500

project_dir = './'

current_word=0
words=[]
home_button=[]
load_file_object=[]
new_label=0

mixer.init()

def show_word():
    new_label['text'] = words[current_word]

def next_word():
    global current_word
    new_label['text'] = '***'
    current_word=current_word+1
    print(current_word)

def read_word():
    global current_word
    if(current_word >= len(words)):
        current_word = 0
        
    tts = gTTS(words[current_word])
    tts.save('temp.mp3')
    mixer.music.load('temp.mp3')
    mixer.music.play()
    while mixer.music.get_busy() == True:
            continue
    mixer.music.unload()
    os.remove('temp.mp3')

def show_home():
    #destory now
    for thing in load_file_object:
        thing.destroy()
    for widget in home_button:
        widget.pack(side='top', fill='x', pady=5)

def load_file(choseFile):
    global words
    global current_word
    global new_label
    current_word=0
    #load words
    f=open(project_dir+choseFile, 'r')
    words = f.read().splitlines()
    f.close()
    print(words)
    #clean screen
    print(home_button)
    for widget in home_button:
        widget.pack_forget()
    #create new screen
    new_label = Label(window, text='****')
    new_label.pack(side='top', fill='x', pady=5)
    load_file_object.append(new_label)
    print(type(new_label))
    
    button = Button(window, text='show', bg='yellow', command=show_word)
    button.pack(side='top', fill='x', pady=5)
    load_file_object.append(button)
    
    button = Button(window, text='read word', bg='yellow', command=read_word)
    button.pack(side='top', fill='x', pady=5)
    load_file_object.append(button)
    
    button = Button(window, text='next', bg='yellow', command=next_word)
    button.pack(side='top', fill='x', pady=5)
    load_file_object.append(button)
    
    button = Button(window, text='go back', bg='yellow', command=show_home)
    button.pack(side='top', fill='x', pady=5)
    load_file_object.append(button)
    



def home_page():
    for _,_,files in os.walk(project_dir):
        for file in files:
            if '.txt' in file:
                print(file)
                button = Button(window, text=file, bg='yellow', command=lambda chfile=file : load_file(chfile))
                button.pack(side='top', fill='x', pady=5)
                home_button.append(button)


window = Tk()
window.title("words practice")
window.minsize(width=winWidth, height=winHeight)
window.resizable(width=False, height=False)
home_page()
window.mainloop()
