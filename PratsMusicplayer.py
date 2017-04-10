import os
import pygame
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import tkMessageBox
#from Tkinter.tkFileDialog import askdirectory
from mutagen.id3 import ID3
import time
from pygame import mixer, sndarray


root=Tk()
root.minsize(300,300)
listofsongs=[]
realnames=[]
current=0
index=0
playpause=True
length=0
v=StringVar()
SongLabel=Label(root,textvariable=v,width=35)
directory=''

vol=1

def directoryChooser():
    global current
    global length
    global directory
    directory = tkFileDialog.askdirectory()
    os.chdir(directory)
    print directory
    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            realdir=os.path.realpath(files)
            audio=ID3(realdir)
            realnames.append(audio["TIT2"].text[0])
            listofsongs.append(files)
            print files
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    a=pygame.mixer.music.play()
    updatelabel()
    #length=a.get_length()
    
    
        
    
def play(event):
        global playpause
        global length
        pygame.init()
        pygame.mixer.init()
        print listofsongs[0]
        pygame.mixer.music.load(listofsongs[0])
        pygame.mixer.music.play()
        updatelabel()
        #autoPlay()
        
        

def stop(event):
        #mExit=tkMessageBox.askokcancel(title="Quit",message="Are you sure?")
        #if mExit ==True:
            global v
            pygame.mixer.music.stop()
            v.set("")
        #return


        
def next1(event):
        global current
        if current<len(listofsongs)-1:
            current+=1
            pygame.mixer.init()
            pygame.mixer.music.load(listofsongs[current])
            pygame.mixer.music.play()
            updatelabel()
            #autoPlay()
        else:
            current=0
            pygame.mixer.init()
            pygame.mixer.music.load(listofsongs[current])
            pygame.mixer.music.play()
            updatelabel()
            #autoPlay()


        
def autoPlay():
    global current
    global length
    
    while current<len(listofsongs)-1:
            time.sleep(length)
            current+=1
            pygame.mixer.init()
            t=pygame.mixer.music.load(listofsongs[current])
            #length=pygame.mixer.music.get_length()
            length=100
            pygame.mixer.music.play()
            
            updatelabel()
    
            
def prev(event):
        global current
        if current>0:
            current-=1
            pygame.mixer.init()
            pygame.mixer.music.load(listofsongs[current])
            pygame.mixer.music.play()
            updatelabel()
        else:
            current=len(listofsongs)-1
            pygame.mixer.init()
            pygame.mixer.music.load(listofsongs[current])
            pygame.mixer.music.play()
            updatelabel()
        #autoPlay()

def updatelabel():
    global current
    global songLabel
    global v
    v.set(realnames[current])


def volin(event):
    global vol
    if vol==1:      # Sound plays at full volume by default
        pygame.mixer.music.set_volume(vol)   # Now plays at 90% of full volume.
    else:
        vol+=0.1
        pygame.mixer.music.set_volume(vol)
    


def voldec(event):
    global vol
    if vol==0:      # Sound plays at full volume by default
        pygame.mixer.music.set_volume(vol)   # Now plays at 90% of full volume.
    else:
        vol-=0.1
        pygame.mixer.music.set_volume(vol)
    
directoryChooser()

label =Label(root,text='Music Player')
label.pack()



listbox=Listbox(root)
listbox.pack()

#listofsongs.reverse()
realnames.reverse()
for items in realnames:
    listbox.insert(0,items)
    #listbox.insert(0,'songs')
realnames.reverse()
#listofsongs.reverse()

Play= Button(root,text='Play')
Play.pack()
Play.bind("<Button-1>",play)
Play.place(relx=.4, rely=0.8, anchor="c")

nextbutton= Button(root,text='Next>>')
nextbutton.pack()
nextbutton.bind("<Button-1>",next1)
nextbutton.place(relx=.6, rely=0.8, anchor="c")
'''
Nfile= Button(root,text='File')
Nfile.pack()
Nfile.bind("<Button-1>",directoryChooser)
Nfile.place(relx=.5, rely=.5, anchor="c")
'''

previousbutton= Button(root,text='<<Prev')
previousbutton.pack()
previousbutton.bind("<Button-1>",prev)
previousbutton.place(relx=0.2, rely=0.8, anchor="c")

stopbutton= Button(root,text='Stop')
stopbutton.pack()
stopbutton.bind("<Button-1>",stop)
stopbutton.place(relx=0.8, rely=0.8, anchor="c")
#directoryChooser()

volup= Button(root,text='vol+')
volup.pack()
volup.bind("<Button-1>",volin)
volup.place(relx=0.8, rely=0.4, anchor="c")

voldown= Button(root,text='vol-')
voldown.pack()
voldown.bind("<Button-1>",voldec)
voldown.place(relx=0.8, rely=0.5, anchor="c")
SongLabel.pack()
#autoPlay()
root.mainloop()
