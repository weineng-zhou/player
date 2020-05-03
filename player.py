# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:47:19 2020

@author: weineng.zhou
"""

import os
import tkinter
import pygame
from PIL import ImageTk, Image



# 音乐列表
currentroot = os.getcwd()
mp3_dir = './mp3'
mp3_list = os.listdir(mp3_dir)
keys = []
values = []
for i, e in enumerate(mp3_list):
   keys.append(i)
   values.append(e)
dic = dict(zip(keys, values))


# 初始化音乐播放器
app = tkinter.Tk()
app.iconbitmap('image/music.ico')
app.minsize(1000, 300)
app.maxsize(1000, 400)
app.title('音乐播放器')
# app.tk_setPalette(background='#848c8f', foreground='#000000', activeBackground='#ffffff', activeForeground='#000000')            

# 播放器背景图片
canvas = tkinter.Canvas(app, width=1000,height=400,bd=0, highlightthickness=0)
imgpath = 'image/猫咪.jpg'
img = Image.open(imgpath)
img = img.resize((1000, 400), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)
canvas.create_image(500, 200, image=photo)
canvas.pack()

# 初始化Pygame.mixer
pygame.mixer.init()

i = 0
pos = 200
stopflag = True
flag_pic = True

def rolltext(widget):
   global pos
   global stopflag
   source_str = dic[i][dic[i].rfind('\\')+1:-4] + ' '
   textwidth = 200
   str_len = len(source_str)
   if str_len - pos < 200:
      show_str.set(source_str[pos:pos+textwidth] + source_str[0:200 - str_len + pos])
   else:
      show_str.set(source_str[pos:pos+textwidth])
   pos += 1
   if pos > str_len:
      pos = 0
   if stopflag:
      widget.after(400, rolltext, widget)

def play():
   global stopflag
   stopflag = True
   rolltext(lab_text)
   pygame.mixer.init()
   pygame.mixer.music.load('mp3/' + dic[i])
   pygame.mixer.music.play()

def stop():
   global stopflag
   stopflag = False
   pygame.mixer.music.pause() 

def lastone():
    global i
    global stopflag
    stopflag = True
    rolltext(lab_text)
    if i > 0:
       i = i - 1
    else:
       i = 0
    pygame.mixer.music.load('mp3/' + dic[i])
    pygame.mixer.music.play()

def nextone():
    global i
    global stopflag
    stopflag = True
    rolltext(lab_text)
    i = i + 1
    pygame.mixer.music.load('mp3/' + dic[i])
    pygame.mixer.music.play()


def click():
   global flag_pic
   flag_pic = not flag_pic
   if flag_pic:
      btn_stop['image'] = img_stop
      stop()
   else:
      btn_stop['image'] = img_play
      play()
   app.update()
   
   
# 标签 初始化显示文本
show_str = tkinter.StringVar(app)
show_str.set('')
lab_text = tkinter.Label(app, fg = '#ffffff', bg='#00b8e5', font = ('微软雅黑', 25), textvariable=show_str)
# lab_text.place(x=300, y=50, width=400, height=60)
lab_text.pack(padx=0, pady=0)

# 按钮
img_lastone = tkinter.PhotoImage(file='image/lastone.png') 
img_play = tkinter.PhotoImage(file='image/play.png') 
img_stop = tkinter.PhotoImage(file='image/stop.png') 
img_nextone = tkinter.PhotoImage(file='image/nextone.png') 

# 上一首
btn_last = tkinter.Button(app, image = img_lastone, bg = '#00b8e5', activebackground='#00bc57', 
                          font = ('微软雅黑', 20), fg = '#ffffff', bd = 0.5, 
                          command = lambda :lastone())  # .place(x = 140, y = 160, width = 200, height = 80)
btn_last.pack(padx=0, pady=0)

# 播放
btn_stop = tkinter.Button(app, image = img_stop, bg = '#00b8e5', activebackground='#00bc57',
                          font = ('微软雅黑', 20), fg = '#000000', bd = 0.5, command = lambda :click())
btn_stop.pack(padx=0, pady=0)

# 下一首
btn_next = tkinter.Button(app, image = img_nextone, bg = '#00b8e5', activebackground='#00bc57', 
                          font = ('微软雅黑', 20), fg = '#ffffff', bd = 0.5,
                          command = lambda :nextone())  # .place(x = 640, y = 160, width = 200, height = 80)
btn_next.pack(padx=0, pady=0)


# 放置标签
canvas.create_window(500, 100, width=413, height=70, window=lab_text)
# 放置按钮
canvas.create_window(187, 200, width=213, height=91, window=btn_last)
canvas.create_window(500, 200, width=213, height=91, window=btn_stop)
canvas.create_window(813, 200, width=213, height=91, window=btn_next)

app.mainloop()

