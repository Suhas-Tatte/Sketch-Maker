import cv2
import os
from tkinter import *
from PIL import Image
from pathlib import Path
from tkinter import filedialog

out=Tk()
out.title("Output Window")
out.filename=filedialog.askopenfilename(initialdir=r"C:\Users\User11\OneDrive\Desktop\images",
                                        title="Select an image",filetypes=(("all files","*.*"),("jpg files","*.jpg")))

a=Path(out.filename).stem

try:
    os.chdir(r"C:\Users\User11\OneDrive\Desktop\images")
    im = Image.open(a+".jpg")
    image = cv2.imread(a+".jpg")
    img_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(img_grey)
    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    invertedblur = cv2.bitwise_not(blur)
    sketch = cv2.divide(img_grey, invertedblur, scale=200)
    os.chdir(r"C:\Users\User11\OneDrive\Desktop\images\sketches")
    b = f"{a} sketch"
    cv2.imwrite(b + ".jpg", sketch)
    img=Image.open(b+'.jpg')
    img.show()

except IOError:
    errlable=Label(out,text="No such image file found",font=('Courier',44),fg='Red').pack()

quit=Button(out,text="Quit",command=out.quit).pack()

out.mainloop()