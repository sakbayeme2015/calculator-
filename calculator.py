!/usr/bin/env python
# -*- coding: utf-8 -*-


from tkinter import *
import math
import random
import time;
import binascii

root = Tk()
root.geometry("1100x1200+0+0")
root.title("Calculator")

text_Input = StringVar()
operator = ""
operator2 = ""
binary = ""


Tops = Frame(root, width = 1100, height = 50, bg="green", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 1100, height = 700, bg="violet", relief=SUNKEN)
f1.pack(side=BOTTOM)

#======================================================Time=======================
localtime=time.asctime(time.localtime(time.time()))
#=============================================Info====================================
lblInfo = Label(Tops, font=('arial',10, 'bold'), text="CALCULATOR", bg="green", bd=10, anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops, font=('arial',10, 'bold'), text=localtime, bg="green", bd=10, anchor='w')
lblInfo.grid(row=0,column=1)
#================================Calculator=================================================================================================
def btnClick(numbers):
 global operator
 operator = operator + str(numbers)
 text_Input.set(operator)

def btnClick1(numbers):
 global operator
 operator = operator + str(numbers)
 text_Input.set(operator)

def btnClick2(numbers):
 global operator
 operator = operator + str(numbers)
 text_Input.set(operator)

def btnClick3(numbers):
 global operator
 operator = operator + str(numbers)
 text_Input.set(operator)

def btnclearDisplay():
 global operator
 operator = ""
 text_Input.set("")

def btnEqualDisplay():
 global operator
 sum = str(eval(operator))
 text_Input.set(sum)
 operator = ""

def btnhexsum():
 global operator
 sumhex = hex(eval(str(operator)))
 text_Input.set(sumhex)
 operator = ""

def btnSquareRoot():
 global operator
 sqrt = math.sqrt(eval(str(operator)))
 text_Input.set(sqrt)
 operator = ""

def btnacos():
 global operator
 cos = math.cos(eval(str(operator)))
 text_Input.set(cos)
 operator = ""

def btnsin():
 global operator
 sin = math.sin(eval(str(operator)))
 text_Input.set(sin)
 operator = ""

def btntan():
 global operator
 tan = math.tan(eval(str(operator)))
 text_Input.set(tan)
 operator = ""

def btnexp():
 global operator
 exp = math.expm1(eval(str(operator)))
 text_Input.set(exp)
 operator = ""
 
 def btnlog10():
 global operator
 log10 = math.log10(eval(str(operator)))
 text_Input.set(log10)
 operator = ""

def btnlog():
 global operator
 log = math.log(eval(str(operator)))
 text_Input.set(log)
 operator = ""

def btnpi():
 global operator
 pi = math.pi
 text_Input.set(pi)
 operator = ""

def btndecbin():
 global operator
 binary = bin(eval(str(operator)))
 text_Input.set(binary)
 operator = ""

def btnbindec():
 global operator
 binary2 = int(operator, 2)
 text_Input.set(binary2)
 operator = ""

def btndechex():
 global operator
 hexadecimal = hex(eval(str(operator)))
 text_Input.set(hexadecimal)
 operator = ""

def btnhexdec():
 global operator
 hexadecimal1 = int(operator, 16)
 text_Input.set(hexadecimal1)
 operator = ""

def btndecoctet():
 global operator
 octet = oct(eval(str(operator)))
 text_Input.set(octet)
 operator = ""

def btnoctetdec():
 global operator
 octet2 = int(operator, 8)
 text_Input.set(octet2)
 operator = ""

def btnbinhex():
 global operator
 hexa = hex(int(operator, 2))
 text_Input.set(hexa)
 operator = ""

def btnhexbin():
 global operator
 binh = bin(int(operator, 16))
 text_Input.set(binh)
 operator = ""

def btnbinoctet():
 global operator
 octet1 = oct(int(operator, 2))
 text_Input.set(octet1)
 operator = ""

def btnoctetbin():
 global operator
 bin2 = bin(int(operator, 8))
 text_Input.set(bin2)
 operator = ""

def btnoctethex():
 global operator
 hexe2 = hex(int(operator , 8))
 text_Input.set(hexe2)
 operator = ""

def btnhexoctet():
 global operator
 octet2 = oct(int(operator, 16))
 text_Input.set(octet2)
 operator = "" 
 
 txtDisplay = Entry(f1, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4 , bg="violet", justify='center')
txtDisplay.grid(columnspan=4)

btn7=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial', 20, 'bold'),text="7",bg="violet", command=lambda: btnClick(7)).grid(row=2, column=0)
btn8=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial', 20, 'bold'),text="8",bg="violet", command=lambda: btnClick(8)).grid(row=2, column=1)
btn9=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial', 20, 'bold'),text="9",bg="violet", command=lambda: btnClick(9)).grid(row=2, column=2)
addition=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="violet",command=lambda: btnClick("+")).grid(row=2, column=3)
#=============================================================================================================================================
btn4=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="violet", command=lambda: btnClick(4)).grid(row=3, column=0)
btn5=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="violet", command=lambda: btnClick(5)).grid(row=3, column=1)
btn6=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="violet", command=lambda: btnClick(6)).grid(row=3, column=2)
subtraction=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="violet", command=lambda: btnClick("-")).grid(row=3, column=3)
#=================================================================================================================================================
btn1=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="violet", command=lambda: btnClick(1)).grid(row=4, column=0)
btn2=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="violet", command=lambda: btnClick(2)).grid(row=4, column=1)
btn3=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="violet", command=lambda: btnClick(3)).grid(row=4, column=2)
multiply=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="violet", command=lambda: btnClick("*")).grid(row=4,column=3)
#================================================================================================================================================
btn0=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="violet", command=lambda: btnClick(0)).grid(row=5, column=0)
btnclear=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="C",bg="violet", command=btnclearDisplay).grid(row=5, column=1)
btnEqual=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="violet", command=btnEqualDisplay).grid(row=5, column=2)
btnDivision=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="violet", command=lambda: btnClick("/")).grid(row=5, column=3)
#================================================================================================================================================
btndot=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text=".",bg="violet", command=lambda: btnClick(".")).grid(row=6, column=0)
btnsquareroot=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="√",bg="violet", command=btnSquareRoot).grid(row=6, column=1)
btnparenthese1=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="(",bg="violet", command=lambda: btnClick("(")).grid(row=6, column=2)
btnparenthese2=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text=")",bg="violet", command=lambda: btnClick(")")).grid(row=6, column=3)
#=========================================================================================================================================
btncos=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="cos",bg="violet", command=btnacos).grid(row=7, column=0)
btnsin=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="sin",bg="violet", command=btnsin).grid(row=7, column=1)
btntans=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="tan",bg="violet", command=btntan).grid(row=7, column=2)
btnexp=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="exp",bg="violet", command=btnexp).grid(row=7, column=3)
#===========================================================================================================================================
btnlog10=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="log10",bg="violet", command=btnlog10).grid(row=8, column=0)
btnlog=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="log",bg="violet",command=btnlog).grid(row=8, column=1)
btnpi=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="pi",bg="violet",command=btnpi).grid(row=8, column=2)
btnbin=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="dec>bin",bg="violet",command=btndecbin).grid(row=8, column=3)
#=========================================================================================================================================
btna=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="A",bg="violet", command=lambda: btnClick1("A")).grid(row=2, column=4)
btnb=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="B",bg="violet", command=lambda: btnClick1("B")).grid(row=3, column=4)
btnc=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="C",bg="violet", command=lambda: btnClick1("C")).grid(row=4, column=4)
btnd=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="D",bg="violet", command=lambda: btnClick1("D")).grid(row=5, column=4)
btne=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="E",bg="violet", command=lambda: btnClick1("E")).grid(row=6, column=4)
btnf=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="F",bg="violet", command=lambda: btnClick1("F")).grid(row=7, column=4)
btnhex=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="dec>hex",bg="violet", command=btndechex).grid(row=8, column=4)
#==================================================================================================================================================
btnoct=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="dec>oct",bg="violet", command=btndecoctet).grid(row=2, column=5)
btnbinsum=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="sumbin",bg="violet", command=btndecbin).grid(row=3, column=5)
btnhexsum=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="sumhex",bg="violet", command=btndechex).grid(row=4, column=5)
btnhex=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="x",bg="violet", command=lambda: btnClick1("x")).grid(row=5, column=5)
#==============================================================================================================================================
btnsumbin=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="bin>dec",bg="violet", command=btnbindec).grid(row=2, column=7)
btnsumhex=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="hex>dec",bg="violet", command=btnhexdec).grid(row=3, column=7)
btnoctdec=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="oct>dec",bg="violet", command=btnoctetdec).grid(row=4, column=7)
btnbinhex=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="bin>hex",bg="violet", command=btnbinhex).grid(row=5, column=7)
btnhexbin=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="hex>bin",bg="violet", command=btnhexbin).grid(row=6, column=5)
btnsumoct=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="sumoctet",bg="violet", command=btndecoctet).grid(row=7, column=5)
#===================================================================================================================================================
btnbinoctet=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="bin>oct",bg="violet", command=btnbinoctet).grid(row=8, column=5)
btnoctetbin=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="oct>bin",bg="violet", command=btnoctetbin).grid(row=6, column=7)
btnoctethex=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="oct>hex",bg="violet", command=btnoctethex).grid(row=7, column=7)
btnhexoctet=Button(f1,padx=16,pady=16,bd=8,fg="black",font=('arial',15,'bold'),text="hex>oct",bg="violet", command=btnhexoctet).grid(row=8, column=7)
#==================================================================================================================================================
root.mainloop()


 
