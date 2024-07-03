import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length,use_upper,use_lower, use_digits,use_special,exclude_simliar):
    similar_characters ='IL1O0'
    characters = ''
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters +=string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
        
    if exclude_simliar:
        characters =''.join([ch for ch in characters if ch not in similar_characters])          
    
    if not characters:
         messagebox.showerr("Invalid input", "please select at least one character type.")    
         
    password = ''.join(random.choice(characters) for i in range(length)) 
    return password 

def on_generate_click():
    try:
         length = int(length_entry.get())
         if length <=0:
             messagebox.showerror("Invalid Input", "length should be a positive integer.")
             return
         use_upper = upper_var.get()
         use_lower = lower_var.get()
         use_digits = digits_var.get()
         use_special =special_var.get()
         exclude_similar = similar_var.get()
         
         password = generate_password(length,use_upper,use_lower, use_digits,use_special,exclude_similar)
         if password:
             password_entry.delete(0,tk.END)
             password_entry.insert(0,password)
             update_password_strength(password)
    except  ValueError:
         messagebox.showerror("Invalid Input", "please enter a valid integer")  
         
def update_password_strength(password):
    length = len(password)      
    categories = sum([any(c.isupper() for c in password),
                      any(c.islower() for c in password),
                      any(c.isdigit()for c in password),
                      any(c in string.punctuation for c in password)])
    
    if length < 6 or categories <2:
        strength = "Weak"
        strength_label.config(fg ='red')
    elif length< 8 or categories <3:
        strength = "moderate"
        strength_label.config(fg="orange")
    else:
        strength = "strong"    
        strength_label.config(fg = 'green')
     
    strength_label.config(text= f"Password Strength:{strength}")   
    
def copy_to_clipboard():
    password = password_entry.get()    
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("success", "password copied to clipboard")
    else:
        messagebox.showwarning("No Password", "No password to copy")    


def save_to_file():
    password = password_entry.get()
    if password:
        with open("password.txt","a") as f:
            f.write(password + "\n")
        messagebox.showinfo("Success", "Password saved to password.txt")
    else:
        messagebox.showwarning("No Password", "No password to save")
        
        
            
root = tk.Tk()
root.title("password generator")
root.configure(bg = 'lightblue')


tk.Label(root,text ="enter the desired length of the password :", bg ='lightblue',fg='black').grid(row=0,column =0, padx=10 ,pady =10)
length_entry = tk.Entry(root,bg = 'white',fg ="black")
length_entry.grid(row= 0, column =1,padx=10, pady =10)

upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()
similar_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters",variable = upper_var, bg = "lightblue" , fg = "black").grid(row =2, column=0,columnspan =2,sticky="w",padx =10)
tk.Checkbutton(root, text="Include Lowercase Letters",variable = lower_var, bg = "lightblue" , fg = "black").grid(row =3, column=0,columnspan =2,sticky="w",padx =10)
tk.Checkbutton(root, text="Include Digits",variable = digits_var, bg = "lightblue" , fg = "black").grid(row =4, column=0,columnspan =2,sticky="w",padx =10)
tk.Checkbutton(root, text="Include Special Characters",variable = special_var, bg = "lightblue" , fg = "black").grid(row =5, column=0,columnspan =2,sticky="w",padx =10)
tk.Checkbutton(root, text="Exclude Similar Characters",variable = similar_var, bg = "lightblue" , fg = "black").grid(row =6, column=0,columnspan =2,sticky="w",padx =10)

generate_button = tk.Button(root,text= "generate Paaword" ,command = on_generate_click ,bg= 'green', fg= 'white')
generate_button.grid(row =7 , column =0, columnspan=2,pady=10 )

tk.Label(root, text ="Generated Password:",bg ='lightblue',fg ='black').grid(row =9 , column =0,padx=10,pady =10)
password_entry = tk.Entry(root,width= 30, bg= 'white', fg ='black')
password_entry.grid(row=9,column=1,padx= 10,pady=10)

copy_button = tk.Button(root,text ="Copy to clipboard", command= copy_to_clipboard ,bg= "blue" , fg = 'white')
copy_button.grid(row=10,column= 0, columnspan =2,pady=10)

save_button = tk.Button(root,text ="Save to file", command= save_to_file ,bg= "blue" , fg = 'white')
save_button.grid(row=11,column= 0, columnspan =2,pady=10)

strength_label = tk.Label(root,text ="Password Strength",bg= "lightblue" , fg = 'black')
strength_label.grid(row=12,column= 0, columnspan =2,pady=10)

root.mainloop()

