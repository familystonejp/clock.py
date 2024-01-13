import tkinter
import datetime
import time
from datetime import timedelta
import threading

root = tkinter.Tk()
root.title('countdown')
root.geometry('1920x1080')
root.attributes('-fullscreen',True)

def countdown():
    while True:
        dt1 = datetime.datetime.now()
        cd = dt1.strftime("%H:%M:%S")
        ##print(cd) 
        canvas.delete("all")
        canvas.create_text(960, 540, text=cd, font=('Arial Black',200),fill='white')
        time.sleep(1)

canvas = tkinter.Canvas(master=None, width=1920, height=1080,background = 'black')
### キャンバス表示
canvas.pack()
### スレッド作成
thread = threading.Thread(target=countdown, daemon=True) 
### スレッド開始
thread.start()
root.mainloop()
