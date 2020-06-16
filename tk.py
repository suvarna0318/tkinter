from tkinter import *
import tkinter.font as font
root=Tk()
e=Entry(root)
e.grid(row=0,column=0,columnspan=4,sticky=E)
print(e.get())

def button_click(num):
	cur=e.get()
	e.delete(0,END)
	e.insert(0,str(cur)+str(num))
def clear_fun():
	e.delete(0,END)
def equal_fun():	
	global second_num
	second_num=e.get()
	e.delete(0,END)
	second_num=int(second_num)
	if math=="addition":
		e.insert(0,first_num+second_num)
	if math=="minus":
		e.insert(0,first_num-second_num)
	if math=="multiplication":
		e.insert(0,first_num*second_num)
	if math=="division":
		e.insert(0,first_num/second_num)	

def addition():
	global first_num
	first_num=e.get()
		
	global math
	first_num=int(first_num)
	math="addition"
	e.delete(0,END)
	
def minus():
	global first_num
	first_num=e.get()
		
	global math
	first_num=int(first_num)
	math="minus"
	e.delete(0,END)

def multiplication():
	global first_num
	first_num=e.get()
		
	global math
	first_num=int(first_num)
	math="multiplication"
	e.delete(0,END)

def division():
	global first_num
	first_num=e.get()
		
	global math
	first_num=int(first_num)
	math="division"
	e.delete(0,END)

	


btn9=Button(root,text="9",command=lambda:button_click(9)).grid(row=1,column=2,sticky=W+E)
btn8=Button(root,text="8",command=lambda:button_click(8)).grid(row=1,column=1,sticky=W+E)
btn7=Button(root,text="7",command=lambda:button_click(7)).grid(row=1,column=0,sticky=W+E)

btn6=Button(root,text="6",command=lambda:button_click(6)).grid(row=2,column=2,sticky=W+E)
btn5=Button(root,text="5",command=lambda:button_click(5)).grid(row=2,column=1,sticky=W+E)
btn4=Button(root,text="4",command=lambda:button_click(4)).grid(row=2,column=0,sticky=W+E)

btn3=Button(root,text="3",command=lambda:button_click(3)).grid(row=3,column=2,sticky=W+E)
btn2=Button(root,text="2",command=lambda:button_click(2)).grid(row=3,column=1,sticky=W+E)
btn1=Button(root,text="1",command=lambda:button_click(1)).grid(row=3,column=0,sticky=W+E)

btn0=Button(root,text="0",command=lambda:button_click(0)).grid(row=4,column=0,sticky=W+E)
btn_clear=Button(root,text="C",command=clear_fun).grid(row=4,column=1,sticky=W+E)
btn_equal=Button(root,text="=",command=equal_fun).grid(row=4,column=2,sticky=W+E)

btn_plus=Button(root,text="+",command=addition).grid(row=1,column=3,sticky=W+E)
btn_minus=Button(root,text="-",command=minus).grid(row=2,column=3,sticky=W+E)
btn_mul=Button(root,text="*",command=multiplication).grid(row=3,column=3,sticky=W+E)
btn_div=Button(root,text="/",command=division).grid(row=4,column=3,sticky=W+E)

root.mainloop()
 