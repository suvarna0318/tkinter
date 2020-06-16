from tkinter import *
from PIL import ImageTk,Image
root=Tk()


my_img1=ImageTk.PhotoImage(Image.open("img1.jpg"))
my_img2=ImageTk.PhotoImage(Image.open("img2.jpg"))
my_img3=ImageTk.PhotoImage(Image.open("img3.jpg"))
my_img4=ImageTk.PhotoImage(Image.open("img4.jpg"))

img_list=[my_img1,my_img2,my_img3,my_img4]
label=Label(root,image=img_list[0]).grid(row=0,column=0,columnspan=3)
def forward(image_num):
	root.destroy
	label=Label(root,image=img_list[image_num-1]).grid(row=0,column=0,columnspan=3)
	if image_num==5:
		btn_forward=Button(root,text=">>",state=DISABLED)
	btn_forward=Button(root,text=">>",command=lambda:forward(image_num+1)).grid(row=1,column=2)
	btn_back=Button(root,text="<<",command=lambda:back(image_num-1)).grid(row=1,column=0)

def back(image_num):
	root.destroy
	label=Label(root,image=img_list[image_num-1]).grid(row=0,column=0,columnspan=3)
	if image_num==1:
		btn_back=Button(root,text=">>",state=DISABLED)
	btn_forward=Button(root,text=">>",command=lambda:forward(image_num+1)).grid(row=1,column=2)
	btn_back=Button(root,text="<<",command=lambda:back(image_num-1)).grid(row=1,column=0)


btn_forward=Button(root,text=">>",command=lambda:forward(2)).grid(row=1,column=2)
btn_back=Button(root,text="<<",command=lambda:forward(1)).grid(row=1,column=0)


root.mainloop()