import tkinter as tk
app = tk.Tk()
app.title('Registration Form')
app.geometry('400x250')
#

f_name = tk.Variable(app)
e_mail = tk.Variable(app)
u_name = tk.Variable(app)
pwd = tk.Variable(app)
age = tk.Variable(app)
mob = tk.Variable(app)

tk.Label(app, text='Full Name').place(x=20,y=30)
tk.Label(app, text='Email Id').place(x=20,y=60)
tk.Label(app, text='User Name').place(x=20,y=90)
tk.Label(app, text='Password').place(x=20,y=120)
tk.Label(app, text='Age').place(x=20,y=150)
tk.Label(app, text='Mobile').place(x=20,y=180)

tk.Entry(app,width=40,bg='#ffffff', textvariable=f_name).place(x=120,y=30)
tk.Entry(app,width=40,bg='#ffffff', textvariable=e_mail).place(x=120,y=60)
tk.Entry(app,width=40,bg='#ffffff', textvariable=u_name).place(x=120,y=90)
tk.Entry(app,width=40,bg='#ffffff', textvariable=pwd).place(x=120,y=120)
tk.Entry(app,width=40,bg='#ffffff', textvariable=age).place(x=120,y=150)
tk.Entry(app,width=40,bg='#ffffff', textvariable=mob).place(x=120,y=180)

from csv import writer
row =['Full Name', 'Email Id', 'User Name', 'Password', 'Age', 'Mobile']
f = open('data.csv','w')
writer_object=writer(f)
writer_object.writerow(row)
f.close()

def register():
    f = open('data.csv','a')
    data = [f_name.get(), e_mail.get(), u_name.get(), pwd.get(), age.get(), mob.get()]
    f.write(','.join(data)+'\n')
    f.close()
    print('Registered')
    f_name.set('')
    e_mail.set('')
    u_name.set('')
    pwd.set('')
    age.set('')
    mob.set('')


tk.Button(app, text='Submit', command=register).place(x=120,y=210)
##tk.Button(app, text='Wrong input', command=input)

#
app.mainloop()



















