from tkinter import *
import sqlite3
from tkinter import messagebox

from pkg_resources import ensure_directory

root=Tk()
root.title('FACEBOOK')
root.iconbitmap('facebook.ico')
root.config(bg='#4267B2')

conn=sqlite3.connect('Facebook.db')
c=conn.cursor()
# c.execute("""CREATE TABLE User(
#     First_Name text,
#     Last_Name text,
#     Address text,
#     Age integer,
#     Password text,
#     Father_Name text,
#     City text,
#     Zip_Code
#     )""")
# print("Table created")
f_name_lable=Label(root,text='First Name',bg='#4267B2',fg='white',font=('Arial',10,'bold'))
f_name_lable.grid(row=0,column=0)

f_name=Entry(root,width=30)
f_name.grid(row=0,column=1)

l_name_lable=Label(root,text='Last Name',bg='#4267B2',fg='white',font=('Arial',10,'bold'))
l_name_lable.grid(row=1,column=0)

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)

address_lable=Label(root,text='Address',bg='#4267B2',fg='white',font=('Arial',10,'bold'))
address_lable.grid(row=2,column=0)

address=Entry(root,width=30,)
address.grid(row=2,column=1)

age_lable=Label(root,text='Age',bg='#4267B2',fg='white',font=('Arial',10,'bold'))
age_lable.grid(row=3,column=0)

age=Entry(root,width=30)
age.grid(row=3,column=1)

password_lable=Label(root,text='Password',bg='#4267B2',fg='white',font=('Arial',10,'bold'))
password_lable.grid(row=4,column=0)

password=Entry(root,width=30,show='*')
password.grid(row=4,column=1)

father_name_lable=Label(root,text='Father Name',bg='#4267B2',fg='white',font=('Arial',10,'bold'))
father_name_lable.grid(row=5,column=0)

father_name=Entry(root,width=30)
father_name.grid(row=5,column=1)

city_lable=Label(root,text='City',bg='#4267B2',fg='white',font=('Arial',10,'bold'))
city_lable.grid(row=6,column=0)

city=Entry(root,width=30)
city.grid(row=6,column=1)

zip_code_lable=Label(root,text='Zip Code',bg='#4267B2',fg='white',font=('Arial',10,'bold'))
zip_code_lable.grid(row=7,column=0)

zip_code=Entry(root,width=30)
zip_code.grid(row=7,column=1)

def submit():
    conn=sqlite3.connect('Facebook.db')
    c=conn.cursor()
    c.execute("INSERT INTO User VALUES(:f_name,:l_name,:address,:age,:password,:father_name,:city,:zip_code)",
    {'f_name':f_name.get(),
    'l_name':l_name.get(),
    'address':address.get(),
    'age':age.get(),
    'password':password.get(),
    'father_name':father_name.get(),
    'city':city.get(),
    'zip_code':zip_code.get()
    })
    messagebox.showinfo('Success','Data Inserted')
    conn.commit()
    conn.close()
    print('Data Inserted')
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    age.delete(0,END)
    password.delete(0,END)
    father_name.delete(0,END)
    city.delete(0,END)
    zip_code.delete(0,END)

submit_btn=Button(root,text="Submit",bg='#12AD2B',fg='white',font=('Arial',10,'bold'),command=submit)
submit_btn.grid(row=8,column=0,columnspan=2,padx=10,pady=10)


def query():
    conn=sqlite3.connect('Facebook.db')
    c=conn.cursor()
    c.execute("SELECT *,oid FROM User")
    records=c.fetchall()
    print(records)
    print_records=""
    for record in records:
        print_records+=str(record[8])+":-"+record[0]+" "+str(record[1])+",""\t"+str(record[4])+"\n"
    query_lable=Label(root,text=print_records)
    query_lable.grid(row=9,column=0,columnspan=2)
    conn.commit()
    conn.close()

query_btn=Button(root,text="Query",bg='#12AD2B',fg='white',font=('Arial',10,'bold'),command=query)
query_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10)

delete_box_label=Label(root,text='Enter OID ',bg='#4267B2',fg='white',font=('Arial',10,'bold'))
delete_box_label.grid(row=11,column=0)
delete_box=Entry(root,width=30)
delete_box.grid(row=11,column=1)
def delete():
    conn=sqlite3.connect('Facebook.db')
    c=conn.cursor()
    c.execute("DELETE FROM User WHERE oid="+delete_box.get())
    print('Data Deleted')
    delete_box.delete(0,END)
    conn.commit()
    conn.close()

delete_box_btn=Button(root,text="Delete",bg='#12AD2B',fg='white',font=('Arial',10,'bold'),command=delete)
delete_box_btn.grid(row=12,column=0,columnspan=2,padx=10,pady=10)

edit_box_label=Label(root,text='Enter OID ',bg='#4267B2',fg='white',font=('Arial',10,'bold'))
edit_box_label.grid(row=13,column=0)
edit_box=Entry(root,width=30)
edit_box.grid(row=13,column=1)


def update():
    conn=sqlite3.connect('Facebook.db')
    c=conn.cursor()
    record_id=edit_box.get()
    c.execute("""Update User SET 
    First_Name=:f_name,
    Last_Name=:l_name,
    Address=:address,
    Age=:age,
    Password=:password,
    Father_Name=:father_name,
    City=:city,
    Zip_Code=:zip_code
    WHERE oid=:oid""",
    {
    'f_name':f_name.get(),
    'l_name':l_name.get(),
    'address':address.get(),
    'age':age.get(),
    'password':password.get(),
    'father_name':father_name.get(),
    'city':city.get(),
    'zip_code':zip_code.get(),
    'oid':record_id
    })
    conn.commit()
    conn.close()
    editor.destroy()



def edit():
    global editor
    editor=Toplevel()
    editor.title('Editor')
    editor.iconbitmap('facebook.ico')

    
    editor.config(bg='#4267B2')
    conn=sqlite3.connect('Facebook.db')
    c=conn.cursor()
    record_id=edit_box.get()
    c.execute("SELECT * FROM User WHERE oid="+record_id)
    records=c.fetchall()

    global f_name_editor
    global l_name_editor
    global address_editor
    global age_editor
    global password_editor
    global father_name_editor
    global city_editor
    global zip_code_editor

    f_name_editor=Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1)

    l_name_editor=Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1)

    address_editor=Entry(editor,width=30)
    address_editor.grid(row=2,column=1)

    age_editor=Entry(editor,width=30)
    age_editor.grid(row=3,column=1)

    password_editor=Entry(editor,width=30)
    password_editor.grid(row=4,column=1)

    father_name_editor=Entry(editor,width=30)
    father_name_editor.grid(row=5,column=1)

    city_editor=Entry(editor,width=30)
    city_editor.grid(row=6,column=1)

    zip_code_editor=Entry(editor,width=30)
    zip_code_editor.grid(row=7,column=1)

    f_name_editor_lable=Label(editor,text='First Name',bg='#4267B2',fg='white',font=('Arial',10,'bold'))
    f_name_editor_lable.grid(row=0,column=0)

    l_name_editor_lable=Label(editor,text='Last Name',bg='#4267B2',fg='white',font=('Arial',10,'bold'))
    l_name_editor_lable.grid(row=1,column=0)

    address_editor_lable=Label(editor,text='Address',bg='#4267B2',fg='white',font=('Arial',10,'bold'))
    address_editor_lable.grid(row=2,column=0)

    age_editor_lable=Label(editor,text='Age',bg='#4267B2',fg='white',font=('Arial',10,'bold'))
    age_editor_lable.grid(row=3,column=0)

    password_editor_lable=Label(editor,text='Password',bg='#4267B2',fg='white',font=('Arial',10,'bold'))
    password_editor_lable.grid(row=4,column=0)

    father_name_editor_lable=Label(editor,text='Father Name',bg='#4267B2',fg='white',font=('Arial',10,'bold'))
    father_name_editor_lable.grid(row=5,column=0)

    city_editor_lable=Label(editor,text='City',bg='#4267B2',fg='white',font=('Arial',10,'bold'))
    city_editor_lable.grid(row=6,column=0)

    zip_code_editor_lable=Label(editor,text='Zip Code',bg='#4267B2',fg='white',font=('Arial',10,'bold'))
    zip_code_editor_lable.grid(row=7,column=0)

    for record in records:
        f_name_editor.insert(0,record[1])
        l_name_editor.insert(0,record[2])
        address_editor.insert(0,record[3])
        age_editor.insert(0,record[4])
        password_editor.insert(0,record[5])
        father_name_editor.insert(0,record[6])
        city_editor.insert(0,record[7])
        zip_code_editor.insert(0,record[8])

    edit_btn=Button(editor,text="Update",bg='#12AD2B',fg='white',font=('Arial',10,'bold'),command=update)
    edit_btn.grid(row=8,column=0,columnspan=2,padx=10,pady=10,ipadx=100)


edit_box_btn=Button(root,text="Update",bg='#12AD2B',fg='white',font=('Arial',10,'bold'),command=edit)

edit_box_btn.grid(row=14,column=0,columnspan=2,padx=10,pady=10)

conn.commit()
conn.close()
root.mainloop()