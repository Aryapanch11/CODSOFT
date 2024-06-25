import tkinter as tk

def press(num):
    current = equation.get()
    equation.set(current+ str(num))
    
def equalpress():
    try:
        total = str(eval(equation.get()))  
        equation.set(total)
    except:
        equation.error("error")
 
def clear():
    equation.set("")  
    
    
root=tk.Tk() 
root.title("Calculator")   
root.configure(bg ="#f0f0f0")   
root.resizable(False,False)    

equation= tk.StringVar()  

entry = tk.Entry(root, textvariable = equation,font= ('Helvetica',18),bd =10,insertwidth =2,width =14,borderwidth =4)
entry.grid(row =0,column =0,columnspan =4)

button1 =tk.Button(root,text='1',padx=20,pady =20,command = lambda: press(1))
button1.grid(row=1,column =0)

button2 =tk.Button(root,text='2',padx=20,pady =20,command = lambda: press(2))
button2.grid(row=1,column =1)

button3 =tk.Button(root,text='3',padx=20,pady =20,command = lambda: press(3))
button3.grid(row=1,column =2)

button4 =tk.Button(root,text='4',padx=20,pady =20,command = lambda: press(4))
button4.grid(row=2,column =0)

button5 =tk.Button(root,text='5',padx=20,pady =20,command = lambda: press(5))
button5.grid(row=2,column =1)

button6 =tk.Button(root,text='6',padx=20,pady =20,command = lambda: press(6))
button6.grid(row=2,column =2)

button7 =tk.Button(root,text='7',padx=20,pady =20,command = lambda: press(7))
button7.grid(row=3,column =0)

button8 =tk.Button(root,text='8',padx=20,pady =20,command = lambda: press(8))
button8.grid(row=3,column =1)

button9 =tk.Button(root,text='9',padx=20,pady =20,command = lambda: press(9))
button9.grid(row=3,column =2)

button0 =tk.Button(root,text='0',padx=20,pady =20,command = lambda: press(0))
button0.grid(row=4,column =0)

button_add = tk.Button(root, text ='+',padx= 20, pady =20,command = lambda: press('+'))
button_add.grid(row =1,column =3)

button_subtract = tk.Button(root, text ='-',padx= 20, pady =20,command = lambda: press('-'))
button_subtract.grid(row =2,column =3)

button_multiply = tk.Button(root, text ='*',padx= 20, pady =20,command = lambda: press('*'))
button_multiply.grid(row=3,column =3)

button_divide = tk.Button(root, text ='/',padx= 20, pady =20,command = lambda: press('/'))
button_divide.grid(row =4,column =3)

button_equal= tk.Button(root, text ='=',padx= 20, pady =20,command =equalpress)
button_equal.grid(row =4,column =1)

button_clear = tk.Button(root, text ='C',padx= 20, pady =20,command =clear)
button_clear.grid(row =4,column =2)



root.mainloop()



        
        
    