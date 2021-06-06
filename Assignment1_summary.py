import tkinter as tk
import csv
import operator
app = tk.Tk()
app.title('Summary')
app.geometry('300x250')

f = open('data.csv','r')
r = f.read()
f.close()
print(r)

r1 = r.split('\n')[:-1]
r1.pop(1)
cols = r1[0].split(',')
r2 = list(map(lambda x:x.split(','),r1[1:]))
d = dict(zip(cols,zip(*r2)))
print(d)

user = len(d['User Name'])

age = (sum(list(map(lambda x: int(x),d['Age']))))/len(d['Age'])

email = list(map(lambda x:x.split('@')[1], d['Email Id']))
email_1 = {i:email.count(i) for i in email}
email_2 = sorted(email_1.items(), key=operator.itemgetter(1))
email_2.reverse()
email_3 = dict(email_2)

tk.Label(app, text='Total users : ').place(x=20,y=30)
tk.Label(app, text=user).place(x=100, y=30)
tk.Label(app, text='Average age : ').place(x=20,y=60)
tk.Label(app, text=age).place(x=100, y=60)
tk.Label(app, text='Common email domains :').place(x=20,y=90)

a=115
for key, value in list(email_3.items())[0:5]:
    tk.Label(app, text=key).place(x=100, y=a)
    tk.Label(app, text=value).place(x=180, y=a)
    a+=20

app.mainloop()




















