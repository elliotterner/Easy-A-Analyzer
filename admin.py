from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class Admin:
    def __init__(self, root):
        self.root = root
        self.root.title("Easy A Program - Administrator")

        self.root.geometry('1500x800')
        self.root.resizable(False, False)
        self.title = StringVar()
        self.department = StringVar()
        self.name = StringVar()
        self.A = StringVar()
        self.B = StringVar()
        self.C = StringVar()
        self.D = StringVar()
        self.F = StringVar()
        self.crn = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()
        self.totalrecord = StringVar()

        headinglbl = Label(root, text="Database Management System", font=("arial", 24, "bold"), bg='#7F7FFF', fg='red')
        headinglbl.pack(side=TOP, fill=X)

        # ***********Frame-1***************
        entry_frame = Frame(root, bd=5, relief='ridge', bg='#E0E0EE')
        entry_frame.place(x=20, y=50, width=350, height=745)

        # Labels of frame-1
        reg_lbl = Label(entry_frame, text="Update database", font=("arial", 15, "bold"), bg='#E0E0EE', fg='red')
        reg_lbl.grid(row=0, columnspan=2)

        titleLabel = Label(entry_frame, text="Course Title", font=("Heiti TC", 13), bg='#E0E0EE')
        titleLabel.grid(row=1, column=0, sticky='w', padx=10, pady=11)

        DepartLabel = Label(entry_frame, text="Department", font=("Heiti TC", 13), bg='#E0E0EE')
        DepartLabel.grid(row=2, column=0, sticky='w', padx=10, pady=11)

        nameLabel = Label(entry_frame, text="Instructor name", font=("Heiti TC", 13), bg='#E0E0EE')
        nameLabel.grid(row=3, column=0, sticky='w', padx=10, pady=11)

        ALabel = Label(entry_frame, text="A percentage", font=("Heiti TC", 13), bg='#E0E0EE')
        ALabel.grid(row=4, column=0, sticky='w', padx=10, pady=11)

        BLabel = Label(entry_frame, text="B percentage", font=("Heiti TC", 13), bg='#E0E0EE')
        BLabel.grid(row=5, column=0, sticky='w', padx=10, pady=11)

        CLabel = Label(entry_frame, text="C percentage", font=("Heiti TC", 13), bg='#E0E0EE')
        CLabel.grid(row=6, column=0, sticky='w', padx=10, pady=11)

        DLabel = Label(entry_frame, text="D percentage", font=("Heiti TC", 13), bg='#E0E0EE')
        DLabel.grid(row=7, column=0, sticky='w', padx=10, pady=11)

        FLabel = Label(entry_frame, text="F percentage", font=("Heiti TC", 13), bg='#E0E0EE')
        FLabel.grid(row=8, column=0, sticky='w', padx=10, pady=11)

        CRNLabel = Label(entry_frame, text="Course CRN", font=("Heiti TC", 13), bg='#E0E0EE')
        CRNLabel.grid(row=9, column=0, sticky='w', padx=10, pady=11)

        # Entry box of Frame-1
        titleEntry = Entry(entry_frame, width=29, bd=3, bg='#E0E0EE', relief='ridge', font=("STSong", 12), textvariable=self.title)
        titleEntry.grid(row=1, column=1, sticky='w', padx=10, pady=11)


        departEnrty = Entry(entry_frame, width=29, bd=3, bg='#E0E0EE', relief='ridge', font=("STSong", 12), textvariable=self.department)
        departEnrty.grid(row=2, column=1, sticky='w', padx=10, pady=11)
        

        insNameEntry = Entry(entry_frame, width=29, bd=3, bg='#E0E0EE', relief='ridge', font=("STSong", 12), textvariable=self.name)
        insNameEntry.grid(row=3, column=1, sticky='w', padx=10, pady=11)

        AEntry = Entry(entry_frame, width=29, bd=3, bg='#E0E0EE', relief='ridge', font=("STSong", 12), textvariable=self.A)
        AEntry.grid(row=4, column=1, sticky='w', padx=10, pady=11)

        BEntry = Entry(entry_frame, width=29, bd=3, bg='#E0E0EE', relief='ridge', font=("STSong", 12), textvariable=self.B)
        BEntry.grid(row=5, column=1, sticky='w', padx=10, pady=11)

        CEntry = Entry(entry_frame, width=29, bd=3, bg='#E0E0EE', relief='ridge', font=("STSong", 12), textvariable=self.C)
        CEntry.grid(row=6, column=1, sticky='w', padx=10, pady=11)

        DEntry = Entry(entry_frame, width=29, bd=3, bg='#E0E0EE', relief='ridge', font=("STSong", 12), textvariable=self.D)
        DEntry.grid(row=7, column=1, sticky='w', padx=10, pady=11)

        FEntry = Entry(entry_frame, width=29, bd=3, bg='#E0E0EE', relief='ridge', font=("STSong", 12), textvariable=self.F)
        FEntry.grid(row=8, column=1, sticky='w', padx=10, pady=11)


        CrnEntry = Entry(entry_frame, width=29, bd=3, bg='#E0E0EE', relief='ridge', font=("STSong", 12), textvariable=self.crn)
        CrnEntry.grid(row=9, column=1, sticky='w', padx=10, pady=11)

        # ***************Functions*********************

        def add_data():
            return

        def fetch_data():
            return

        def clear_data():
            self.title.set("")
            self.department.set("")
            self.name.set("")
            self.A.set("")
            self.B.set("")
            self.C.set("")
            self.D.set("")
            self.F.set("")
            self.crn.set("")


        def focus(e):
            cursor = table.focus()
            content = table.item(cursor)
            row = content['values']
            self.title.set(row[0])
            self.department.set(row[1])
            self.name.set(row[2])
            self.A.set(row[3])
            self.B.set(row[4])
            self.C.set(row[5])
            self.D.set(row[6])
            self.F.set(row[7])
            self.crn.set(row[8])

        def update_data():
            return

        def delete_data():
            return


        def search():
            return

        # **********Frame-3 Button**************

        btn_frame = Frame(entry_frame, bd=5, relief='ridge', bg='#E0E0EE')
        btn_frame.place(x=15, y=590, width=310, height=120)

        add_btn = Button(btn_frame, text='Add', font=("", 12), command=add_data, width="7", bg='#E0E0EE')
        add_btn.grid(row=0, column=1, padx=50, pady=10)

        update_btn = Button(btn_frame, text='Update', font=("", 12), command=update_data, width="7", bg='#E0E0EE')
        update_btn.grid(row=0, column=2, padx=10, pady=10)

        delete_btn = Button(btn_frame, text='Delete', font=("", 12), command=delete_data, width="7", bg='#E0E0EE')
        delete_btn.grid(row=1, column=1, padx=50, pady=10)

        clear_btn = Button(btn_frame, text='Clear', font=("", 12), command=clear_data, width="7", bg='#E0E0EE')
        clear_btn.grid(row=1, column=2, padx=10, pady=10)

        # ***********Frame-2***************
        data_frame = Frame(root, bd=5, relief='ridge', bg='#E0E0EE')
        data_frame.place(x=380, y=50, width=1145, height=745)

        # ***********Frame-2 code*****************
        search_lbl = Label(data_frame, text="Search by", font=("", 13), bg='#E0E0EE')
        search_lbl.grid(row=0, column=0, sticky='w', padx=10, pady=14)

       

        search_entry = Entry(data_frame, bd=3, relief='ridge', font=("", 12), width=15, textvariable=self.search_txt)
        search_entry.grid(row=0, column=1, sticky='w', padx=10, pady=14)

        show_btn = Button(data_frame, text='Find', font=("", 12), command=search)
        show_btn.grid(row=0, column=3, padx=10, pady=10)

        total_lbl = Label(data_frame, text="Total Records", font=("", 13), bg='#E0E0EE')
        total_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=8)

        totalrecord_lbl = Label(data_frame, text="Total Records", font=("", 13), textvariable=self.totalrecord)
        totalrecord_lbl.grid(row=1, column=1, sticky='w', padx=10, pady=8)

        # ************Frame-3 Treeview***************

        viewFrame = Frame(data_frame, bd=5, relief='ridge', bg='wheat')
        viewFrame.place(x=20, y=100, width=1080, height=620)

        xScroll = Scrollbar(viewFrame, orient=HORIZONTAL)
        yScroll = Scrollbar(viewFrame, orient=VERTICAL)
        table=ttk.Treeview(viewFrame,columns=('title.','department','name','A','B','C','D','F','crn'),xscrollcommand=xScroll.set,yscrollcommand=yScroll.set)
        xScroll.pack(side=BOTTOM, fill=X)
        yScroll.pack(side=RIGHT, fill=Y)
        xScroll.configure(command=table.xview)
        yScroll.configure(command=table.yview)

        table.heading("title.", text="Title")
        table.heading("department", text="Department")
        table.heading("name", text="Instructor")
        table.heading("A", text="A percentage")
        table.heading("B", text="B percentage")
        table.heading("C", text="C percentage")
        table.heading("D", text="D percentage")
        table.heading("F", text="F percentage")
        table.heading("crn", text="CRN")

        table.column("title.", width=100)
        table.column("department", width=100)
        table.column("name", width=100)
        table.column("A", width=100)
        table.column("B", width=100)
        table.column("C", width=100)
        table.column("D", width=100)
        table.column("F", width=100)
        table.column("crn", width=100)
        table['show'] = 'headings'
        table.bind('<ButtonRelease-1>', focus)
        fetch_data()
        table.pack(fill=BOTH, expand=1)

root = Tk()
ob = Admin(root)
root.mainloop()