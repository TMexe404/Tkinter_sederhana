from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import threading
import multiprocessing
import sqlite3
import shutil
import pyttsx3
import tkinter
import os

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('akun.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL);')
print("oke")

print("oke1")
db.commit()
db.close()

LARGE_FONT = ("Verdana", 12)



def Login():

    with sqlite3.connect('akun.db') as db:
         c = db.cursor()

    # Find user If there is any take proper action
    find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
    c.execute(find_user, [(Username.get()), (Password.get())])
    result = c.fetchall()
    if result:
        print("anda berhasil => ",result)
        del_login_home()

    else:
        messagebox.showinfo("Ooop!!!", 'Username Not Found.')
        print('Oops!', 'Username Not Found.')

def loginUi():
    global Username
    global Password
    global Li
    Li = Tk()
    Li.title("TUGAS IMK")
    Li.call('wm', 'iconphoto', Li._w, PhotoImage(file='iconT.png'))
    Li.geometry("300x300")
    Li.configure(background='#4d79ff')
    Username = StringVar()
    Password = StringVar()
    label = Label(Li, text="FORM LOGIN ", bg='#4d79ff', fg='#ccd9ff', font=("Times New Roman", 12, "bold"))
    label.place(x=90, y=1)
    label1 = Label(Li, text="Username ",bg='#4d79ff', fg='#ccd9ff', font=("Times New Roman", 12, "bold"))
    label1.place(x=10,y=50)
    entry1 = Entry(Li, textvariable=Username, bg='#1a53ff', fg='#ccd9ff',font=("Times New Roman", 12, "bold"))
    entry1.place(x=90,y=55)

    label2 = Label(Li, text="Password ", bg='#4d79ff', fg='#ccd9ff', font=("Times New Roman", 12, "bold"))
    label2.place(x=10, y=100)
    entry2 = Entry(Li, textvariable=Password, bg='#1a53ff',show='*', fg='#ccd9ff',font=("Times New Roman", 12, "bold"))
    entry2.place(x=90, y=105)

    tombol1 = Button(Li, text="Sign In", command=Login, bg='#668cff', fg='#ccd9ff',)
    tombol1.place(x=70, y=150)
    tombol2 = Button(Li, text="Sign Up", command=del_login, bg='#668cff', fg='#ccd9ff',)
    tombol2.place(x=150, y=150)

    Li.mainloop()

def del_login_home():
    print("delete login to home")
    Li.destroy()

    t1= threading.Thread(target=suara)
    t1.start()

    home()

def del_login():
    print("delete login")
    Li.destroy()
    registerUi()

def register():
    print(n_username.get(), "", n_password.get())
    with sqlite3.connect('akun.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM user WHERE username = ?')
    c.execute(find_user, [(n_username.get())])
    if c.fetchall():
        messagebox.showinfo('Error!', 'Username Taken Try a Diffrent One.')
        print('Error!', 'Username Taken Try a Diffrent One.')
    else:
        print('Success!', 'Account Created!')
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(n_username.get()), (n_password.get())])
        ###############################################
        with sqlite3.connect(n_username.get()+'.db') as db2:
            c2 = db2.cursor()

        c2.execute('CREATE TABLE IF NOT EXISTS data (nol TEXT,nobp TEXT NOT NULL primary key '
                   ',nama TEXT NOT NULL,kelas TEXT NOT NULL,jurusan TEXT NOT NULL,fakultas TEXT NOT NULL);')
        c2.execute('CREATE TABLE IF NOT EXISTS poto (id INTEGER NOT NULL primary key AUTOINCREMENT,file TEXT NOT NULL);')
        db2.commit()
        db2.close()
        ###############################################
        print(n_username.get(), "", n_password.get())
        db.commit()
        del_register()

def registerUi():
    global ri
    global n_username
    global n_password

    ri = Tk()
    ri.title("TUGAS IMK")
    ri.call('wm', 'iconphoto', ri._w, PhotoImage(file='iconT.png'))
    ri.geometry("300x300")
    ri.configure(background='#4d79ff')
    n_username = StringVar()
    n_password = StringVar()

    label = Label(ri, text="FORM SIGNUP ", bg='#4d79ff', fg='#ccd9ff', font=("Times New Roman", 12, "bold"))
    label.place(x=90, y=1)
    label1 = Label(ri, text="Username ", bg='#4d79ff', fg='#ccd9ff', font=("Times New Roman", 12, "bold"))
    label1.place(x=10, y=50)
    entry1 = Entry(ri, textvariable=n_username, bg='#1a53ff', fg='#ccd9ff',)
    entry1.place(x=90, y=55)

    label2 = Label(ri, text="Password ", bg='#4d79ff', fg='#ccd9ff', font=("Times New Roman", 12, "bold"))
    label2.place(x=10, y=100)
    entry2 = Entry(ri, textvariable=n_password, bg='#1a53ff', show='*', fg='#ccd9ff',)
    entry2.place(x=90, y=105)

    tombol1 = Button(ri, text="Sign In", command=del_register, fg='#ccd9ff', bg='#668cff')
    tombol1.place(x=70, y=150)
    tombol2 = Button(ri, text="Sign Up", command=register, bg='#668cff', fg='#ccd9ff')
    tombol2.place(x=150, y=150)
    ri.mainloop()

def del_register():
    print("delete register")
    ri.destroy()
    loginUi()

def home():
    global hm
    global x
    hm = Tk()
    hm.title("TUGAS IMK")
    hm.call('wm', 'iconphoto', hm._w, PhotoImage(file='iconT.png'))
    hm.geometry("800x600")
    hm.configure(background='#4d79ff')
    logo = tk.PhotoImage(file='background/i01_bgTM.png')
    fr=tk.Canvas(hm,bg='#4d79ff',height=100,width=795)
    fr.place(y=1,x=1)
    logo1 = tk.PhotoImage(file='icon/data3.png')
    label1 = tk.Label(fr,image=logo,bg='#4d79ff')
    label1.place(x=140, y=0)
    data_data = Button(hm, text="TAMBAH DATA", bg='#668cff', fg='#ccd9ff'
                       ,command=del_home,image=logo1,compound=tk.LEFT, font=("Times New Roman", 12, "bold"))
    data_data.place(x=350, y=200)
    tanya=PhotoImage(file="icon/ic_info(1).png")
    tombol_dev = Button(hm, text="INFO", bg='#668cff',image=tanya
                        , command=de, compound=tk.LEFT, fg='#ccd9ff',font=("Times New Roman", 12, "bold"))
    tombol_dev.place(x=350, y=300)
    ##########
    try:
        with sqlite3.connect(Username.get()+'.db') as db:
            c = db.cursor()
        find_user = ('SELECT file FROM poto WHERE id = 1')
        abv = c.execute(find_user)
        data = []
        for b in abv:
            data.append(b)
        if c.fetchall():
            messagebox.showinfo('Error!', 'GAGAL AKSES')
        db.commit()
        db.close()
        x = data[0]
    except:
        print("foto belum ada")
    ##########
    # open_cv = Button(hm, text="TAMBAH FOTO", bg='#668cff', fg='#ccd9ff', command=tambah_foto,font=("Times New Roman", 12, "bold"))
    # open_cv.place(x=350, y=400)
    try:
        pt=PhotoImage(file=x)
        label_poto=Label(hm,image=pt)
        label_poto.place(x=550, y=200)
    except:
        print("null")
    hm.mainloop()



def suara():
    engine = pyttsx3.init()
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_idID_Andika"
    engine.setProperty('voice', voice_id)
    engine.say("SELAMAT DATANG DI PERUSAHAAN KANIBAL")
    # engine.say("SAYA SEBAGAI ASSISTEN DIGITAL BOSS")
    # engine.say("AKAN MELAYANI BOSS DENGAN SEGENAP RAM SAYA")
    # engine.say("HEHE")
    engine.runAndWait()

def suara_tambah():
    engine = pyttsx3.init()
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_idID_Andika"
    engine.setProperty('voice', voice_id)
    engine.say("ANDA MEMASUKI FORM TAMBAH DATA")
    # engine.say("SAYA SEBAGAI ASSISTEN DIGITAL BOSS")
    # engine.say("AKAN MELAYANI BOSS DENGAN SEGENAP RAM SAYA")
    # engine.say("HEHE")
    engine.runAndWait()



# def tambah_foto():
#     global data2
#     global t
#     data2 = []
#     gt = filedialog.askopenfilename(initialdir="/", title="Select Foto",
#                                     filetype=(("jpeg", "*.jpg"), ("ALL FILES", "*.*"),))
#     print(gt)
#     t = shutil.copy(gt, 'E:/Latihan_pemrograman/buekbaliak/profil/')
#     print("sukses => " + t)
#     tambah_foto2()
#
#     ###################
#
# def tambah_foto2():
#     b = t
#     # try:
#     with sqlite3.connect(Username.get()+'.db') as db10:
#         c11 = db10.cursor()
#
#     # Find Existing username if any take proper action
#     # c11.execute('delete FROM poto WHERE id = 1;')
#     # c11.execute('insert into poto (file)values(?);',t)
#     # abv = c11.execute('select * from poto WHERE id = 1;')
#     sql = ('delete FROM poto WHERE id = 1')
#
#     insert = 'INSERT INTO poto(id,file) VALUES(''1'',?)'
#     sql2 = ('select file from poto WHERE id = 1')
#     c11.execute(sql)
#     c11.execute(insert, (b,))
#     abv = c11.execute(sql2)
#     data = []
#     for b in abv:
#         data.append(b)
#     db10.commit()
#     db10.close()
#
#     print("sukses1")
#     print(t)
#
#     print(data[0])
#     x = data[0]
#     print(x)
#     # pp = PhotoImage(file=x)
#     # ca = tk.Canvas(hm, image=pp, bg='#4d79ff', height=100, width=795)
#     # ca.place(x=1, y=200)




def del_home():
    hm.destroy()
    t1 = threading.Thread(target=suara_tambah)
    t1.start()
    home_data()

def home_data():
    global hmd
    global tabel
    hmd = Tk()
    hmd.title("TUGAS IMK")
    hmd.call('wm', 'iconphoto', hmd._w, PhotoImage(file='iconT.png'))
    hmd.geometry("800x600")
    hmd.configure(background='#4d79ff')
    data_data = Button(hmd, text="Tambah Data", bg='black', fg='#ccd9ff', command=data_del, compound=tk.LEFT,font=("Times New Roman", 12, "bold"))
    data_data.place(x=500, y=550)
    select = Button(hmd, text="hapus", bg='black', fg='#ccd9ff', command=selec, compound=tk.LEFT,font=("Times New Roman", 12, "bold"))
    select.place(x=300, y=550)
    select = Button(hmd, text="edit", bg='black', fg='#ccd9ff', command=del_edit, compound=tk.LEFT,font=("Times New Roman", 12, "bold"))
    select.place(x=100, y=550)
    ###############
    ho=PhotoImage(file="icon/ic_home.png")
    select = Button(hmd, text="Home", bg='black', fg='#ccd9ff',image=ho, command=to_home, compound=tk.LEFT,font=("Times New Roman", 12, "bold"))
    select.place(x=10, y=100)
    logo = tk.PhotoImage(file='background/i01_bgTM.png')
    fr = tk.Canvas(hmd, bg='#4d79ff', height=100, width=795)
    fr.place(y=1, x=1)
    label1 = tk.Label(fr, image=logo, bg='#4d79ff')
    label1.place(x=140, y=0)
    tabel = ttk.Treeview(height=20,column=('NOBP','nama','kelas','jurusan','fakultas'))
    tabel.column('#0',width=-10)
    tabel.column('#1', width=100)
    tabel.column('#2', width=100)
    tabel.column('#3', width=100)
    tabel.column('#4', width=100)
    tabel.heading('NOBP', text="NOBP")
    tabel.heading('nama', text="NAMA")
    tabel.heading('kelas', text="KELAS")
    tabel.heading('jurusan', text="JURUSAN")
    tabel.heading('fakultas', text="FAKULTAS")
    tabel.place(x=100, y=110)
    with sqlite3.connect(Username.get() + '.db') as db:
        c = db.cursor()

    sql = 'select * from data'
    c.execute(sql)
    a = c.execute(sql)
    data = []
    for b in a:
        data.append(list(b))

    for gt in data:
        tabel.insert('', 'end', values=(gt[1], gt[2], gt[3], gt[4],gt[5]))
        print(gt)
    label_dataa = data

    # label_data = Label(fr, text=label_dataa)
    # label_data.place(x=1, y=1)
    hmd.mainloop()

def to_home():
    hmd.destroy()
    home()

def selec():
    libary= tabel.item(tabel.selection())
    print(libary.get('values'))
    data=[]
    for n in libary.get('values'):
        print(n)
        data.append(n)
    print("===============================================")
    print(data[0])
    print(data[1])
    print(data[2])
    print(data[3])
    print(data[4])
    with sqlite3.connect(Username.get() + '.db') as db2:
        c2 = db2.cursor()

    sql='Delete FROM data WHERE nobp=?;'
    c2.execute(sql, [(data[0])])
    db2.commit()
    db2.close()

    # for item in tabel.selection():
    #     item_text = tabel.item(item, "text")
    #     print("data anda => ",item_text)


def tambah_data():
    global add
    with sqlite3.connect(Username.get() + '.db') as db5:
        c = db5.cursor()

    insert = 'INSERT INTO data(nobp,nama,kelas,jurusan,fakultas) VALUES(?,?,?,?,?)'
    c.execute(insert, [(bp.get()), (nm.get()),(kl.get()),(jr.get()),(fk.get())])
    db5.commit()
    home_data()

def data_del():
    print("destroy tambah data")
    hmd.destroy()
    tambah_data_ui()



def tambah_data_ui():
    global tdi
    global bp
    global nm
    global jr
    global fk
    global kl
    tdi = Tk()
    tdi.title("TUGAS IMK")
    tdi.call('wm', 'iconphoto', tdi._w, PhotoImage(file='iconT.png'))
    tdi.geometry("400x400")
    tdi.configure(background='#4d79ff')
    bp = StringVar()
    nm = StringVar()
    jr = StringVar()
    fk = StringVar()
    kl = StringVar()

    label_mauk = Label(tdi, text="FORM ISI DATA",font=("Times New Roman", 12, "bold"))
    label_mauk.place(x=100, y=1)
    label_bp = Label(tdi,text="Masukan nobp anda",font=("Times New Roman", 12, "bold"))
    label_bp.place(x=10,y=50)
    entry_bp=Entry(tdi, textvariable=bp,font=("Times New Roman", 12, "bold"))
    entry_bp.place( x=200,y=50)

    label_nm = Label(tdi,text="Masukan Nama anda",font=("Times New Roman", 12, "bold"))
    label_nm.place(x=10, y=100)
    entry_bp = Entry(tdi, textvariable=nm,font=("Times New Roman", 12, "bold"))
    entry_bp.place( x=200, y = 100)

    label_kl = Label(tdi, text="masukan kelas",font=("Times New Roman", 12, "bold"))
    label_kl.place(x=10, y=150)
    entry_kl = Entry(tdi, textvariable=kl,font=("Times New Roman", 12, "bold"))
    entry_kl.place(x=200, y = 150)

    label_jr = Label(tdi,text="masukan jurusan",font=("Times New Roman", 12, "bold"))
    label_jr.place(x=10,y=200)
    entry_jr = Entry(tdi, textvariable=jr,font=("Times New Roman", 12, "bold"))
    entry_jr.place(x=200, y = 200)

    label_fk = Label(tdi,text="masukan fakultas anda",font=("Times New Roman", 12, "bold"))
    label_fk.place(x=10,y=250)
    entry_fk = Entry(tdi, textvariable=fk,font=("Times New Roman", 12, "bold"))
    entry_fk.place( x=200, y = 250)

    save=Button(tdi, text="save", command=tmbh_data_delet,font=("Times New Roman", 12, "bold"))
    save.place(x=150,y=300)

    # kembali = Button(tdi, text="back")
    # kembali.place(x=200, y=300)

    tdi.mainloop()

def tmbh_data_delet():
    tdi.destroy()
    tambah_data()

def edit():
    global ebp
    global enm
    global ejr
    global efk
    global ekl
    global ed

    ed = Tk()
    ed.title("TUGAS IMK")
    ed.call('wm', 'iconphoto', ed._w, PhotoImage(file='iconT.png'))
    ed.geometry("400x400")
    ed.configure(background='#4d79ff')
    ebp=StringVar()
    enm=StringVar()
    ekl=StringVar()
    ejr=StringVar()
    efk=StringVar()
    ######################################################
    label_mauk = Label(ed, text="FORM EDIT",font=("Times New Roman", 12, "bold"))
    label_mauk.place(x=100, y=1)
    label_bp = Label(ed, text="Masukan nobp anda",font=("Times New Roman", 12, "bold"))
    label_bp.place(x=10, y=50)
    entry_bp = Entry(ed,textvariable=ebp,font=("Times New Roman", 12, "bold"))
    entry_bp.place(x=200, y=50)

    label_nm = Label(ed, text="Masukan Nama anda",font=("Times New Roman", 12, "bold"))
    label_nm.place(x=10, y=100)
    entry_bp = Entry(ed, textvariable=enm,font=("Times New Roman", 12, "bold"))
    entry_bp.place(x=200, y=100)

    label_kl = Label(ed, text="masukan kelas",font=("Times New Roman", 12, "bold"))
    label_kl.place(x=10, y=150)
    entry_kl = Entry(ed, textvariable=ekl,font=("Times New Roman", 12, "bold"))
    entry_kl.place(x=200, y=150)

    label_jr = Label(ed, text="masukan jurusan",font=("Times New Roman", 12, "bold"))
    label_jr.place(x=10, y=200)
    entry_jr = Entry(ed, textvariable=ejr,font=("Times New Roman", 12, "bold"))
    entry_jr.place(x=200, y=200)

    label_fk = Label(ed, text="masukan fakultas anda",font=("Times New Roman", 12, "bold"))
    label_fk.place(x=10, y=250)
    entry_fk = Entry(ed, textvariable=efk,font=("Times New Roman", 12, "bold"))
    entry_fk.place(x=200, y=250)

    save = Button(ed, text="save", command=edit_,font=("Times New Roman", 12, "bold"))
    save.place(x=150, y=300)
    ed.mainloop()


def del_edit():
    hmd.destroy()
    edit()
def del_edit2():
    ed.destroy()
    home_data()


def edit_():
    with sqlite3.connect(Username.get() + '.db') as db2:
        c2 = db2.cursor()

    sql='update data set nobp=?,nama=?,kelas=?,jurusan=?,fakultas=? where nobp=?;'
    c2.execute(sql, [(ebp.get()),(enm.get()),(ekl.get()),(ejr.get()),(efk.get()),(ebp.get())])
    db2.commit()
    db2.close()
    del_edit2()

def de():
    hm.destroy()
    develop()

def develop():
    global dev
    dev = Tk()
    dev.title("TUGAS IMK")
    dev.call('wm', 'iconphoto', dev._w, PhotoImage(file='iconT.png'))
    dev.geometry("800x600")
    dev.configure(background='#4d79ff')
    # dev=Frame(width=100,height=100,padx=10, pady=10,bg='gray37')
    # fr = tk.Canvas(de, bg='#4d79ff', height=100, width=795)
    # fr.place(y=1, x=1)
    ##99b3ff
    #logo1 = tk.PhotoImage(file='icon/data3.png')

    poto1 = PhotoImage(file='background/Untitled3.png')
    poto2 = PhotoImage(file='background/Untitled2.png')
    poto3 = PhotoImage(file='background/Untitled1.png')
    label1 = Label(dev, image=poto3, text="MUHAMMAD RIVAN", compound=tk.BOTTOM
                   , bg='#668cff', fg='#ccd9ff',font=("Times New Roman", 12, "bold"))
    label1.place(x=300, y=0)

    # labelpoto1=Label(dev, image=poto1, text="ADAP", compound=tk.LEFT, bg='#668cff', fg='#ccd9ff',font=("Times New Roman", 12, "bold"))
    # labelpoto1.place(x=1, y=300)
    #
    # labelpoto3 = Label(dev, image=poto3, text="MUHAMMAD RIVAN", compound=tk.RIGHT, bg='#668cff', fg='#ccd9ff',font=("Times New Roman", 12, "bold"))
    # labelpoto3.place(x=425, y=300)

    tombolkembali= Button(dev, text="kembali",bg='black',fg='#ccd9ff',font=("Times New Roman", 12, "bold"),command=del_dev)
    tombolkembali.place(x=1, y=550)
    dev.mainloop()

def del_dev():
    dev.destroy()
    home()

######################
def main_screen():
    loginUi()

main_screen()