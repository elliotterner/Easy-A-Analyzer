"""
File Name: admin.py
Program Name: Easy A
File purpose: This file is a subsystem of the Easy A program that shows the A and passing grades
                percentage for each natural sciences faculty.
                This file provides a Graphical interface and functions for an administrator user to add/update
                data within the current database.
Creation date: Jan 15 2023
Initial Authors: Jerry Pi
References used:
    mysql deletion learned from: https://www.plus2net.com/python/tkinter-mysql-delete.php
    tkinter creation learned from:https://www.youtube.com/watch?v=YXPyB4XeYLA
    tkinter view learned from:: https://blog.csdn.net/u013278255?type=blog
    tkinter function calls by button learned from: https://www.tutorialspoint.com/call-a-function-with-a-button-or-a-key-in-tkinter
    mysql display learned from:https://www.plus2net.com/python/tkinter-mysql.php
"""

#libraries used
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql

"""
Class Name: Admin
Class Purpose: This class is the base of the GUI and all all necessary functions and class member to interact
                with the database is located within the class
Class Members:
    self.root: The tkinter root variable that creates the UI. Required parameter for this program to work.
    self.root.title: The UI name variable
    self.root.geometry: The UI size variable
    self.titile: The name of the course title in the database
    self.term: The term that the course is offered
    self.name: The name of the instructor of the course
    self.A: The percentage of how many students received grade A in the course
    self.B: The percentage of how many students received grade B in the course
    self.C: The percentage of how many students received grade C in the course
    self.D: The percentage of how many students received grade D in the course
    self.F: The percentage of how many students received grade F in the course
    self.crn: The course crn
    self.searchText: the text that the user entered into the search box
    self.totalrecord: The count of how many data is in the database
    self.facultyType: The type of the faculty

Class Functions:
    addData()
    fetchData()
    clear()
    delete()
    update()
    search()
"""
class Admin:
    def __init__(self, root):
        self.root = root
        self.root.title("Easy A Program - Administrator")
        self.root.geometry('1500x800')
        self.title = StringVar()
        self.term = StringVar()
        self.name = StringVar()
        self.A = StringVar()
        self.B = StringVar()
        self.C = StringVar()
        self.D = StringVar()
        self.F = StringVar()
        self.crn = StringVar()
        self.searchText = StringVar()
        self.totalrecord = StringVar()
        self.facultyType = StringVar()

        #Name of the program
        headinglbl = Label(root, text="Administrator Management System", font=("arial", 24, "bold"), bg='deep sky blue', fg='black')
        headinglbl.pack(side=TOP, fill=X)

        # ***********Frame-1***************
        
        #Entry frame for frame 1
        entryFrame = Frame(root, bd=5, relief='ridge', bg='lavender blush')
        entryFrame.place(x=20, y=50, width=350, height=745)

        # Frame name
        introLabel = Label(entryFrame, text="Update database", font=("arial", 15, "bold"), bg='lavender blush', fg='red')
        introLabel.grid(row=0, columnspan=2)

        #Course title Label
        titleLabel = Label(entryFrame, text="Course Title", font=("arial", 13), bg='lavender blush')
        titleLabel.grid(row=1, column=0, sticky='w', padx=10, pady=11)

        #Course term Label
        DepartLabel = Label(entryFrame, text="Term", font=("arial", 13), bg='lavender blush')
        DepartLabel.grid(row=2, column=0, sticky='w', padx=10, pady=11)

        #Instructor name label
        nameLabel = Label(entryFrame, text="Instructor name", font=("arial", 13), bg='lavender blush')
        nameLabel.grid(row=3, column=0, sticky='w', padx=10, pady=11)

        #A Percentage Label
        ALabel = Label(entryFrame, text="A percentage", font=("arial", 13), bg='lavender blush')
        ALabel.grid(row=4, column=0, sticky='w', padx=10, pady=11)

        #B Percentage Label
        BLabel = Label(entryFrame, text="B percentage", font=("arial", 13), bg='lavender blush')
        BLabel.grid(row=5, column=0, sticky='w', padx=10, pady=11)

        #C Percentage Label
        CLabel = Label(entryFrame, text="C percentage", font=("arial", 13), bg='lavender blush')
        CLabel.grid(row=6, column=0, sticky='w', padx=10, pady=11)

        #D Percentage Label
        DLabel = Label(entryFrame, text="D percentage", font=("arial", 13), bg='lavender blush')
        DLabel.grid(row=7, column=0, sticky='w', padx=10, pady=11)

        #F Percentage Label
        FLabel = Label(entryFrame, text="F percentage", font=("arial", 13), bg='lavender blush')
        FLabel.grid(row=8, column=0, sticky='w', padx=10, pady=11)

        #CRN Label
        CRNLabel = Label(entryFrame, text="Course CRN", font=("arial", 13), bg='lavender blush')
        CRNLabel.grid(row=9, column=0, sticky='w', padx=10, pady=11)

        #Faculty type label
        facultyLabel = Label(entryFrame, text="Faculty Type", font=("arial", 13), bg='lavender blush')
        facultyLabel.grid(row=10, column=0, sticky='w', padx=10, pady=11)

        # Entry boxes of Frame-1
        #Title entry
        titleEntry = Entry(entryFrame, width=29, bd=3, bg='lavender blush', relief='ridge', font=("arial", 12), textvariable=self.title)
        titleEntry.grid(row=1, column=1, sticky='w', padx=10, pady=11)
        
        #Term entry
        departEnrty = Entry(entryFrame, width=29, bd=3, bg='lavender blush', relief='ridge', font=("arial", 12), textvariable=self.term)
        departEnrty.grid(row=2, column=1, sticky='w', padx=10, pady=11)

        #Instructor name entry
        insNameEntry = Entry(entryFrame, width=29, bd=3, bg='lavender blush', relief='ridge', font=("arial", 12), textvariable=self.name)
        insNameEntry.grid(row=3, column=1, sticky='w', padx=10, pady=11)

        #A percentage entry
        AEntry = Entry(entryFrame, width=29, bd=3, bg='lavender blush', relief='ridge', font=("arial", 12), textvariable=self.A)
        AEntry.grid(row=4, column=1, sticky='w', padx=10, pady=11)

        #B percentage entry
        BEntry = Entry(entryFrame, width=29, bd=3, bg='lavender blush', relief='ridge', font=("arial", 12), textvariable=self.B)
        BEntry.grid(row=5, column=1, sticky='w', padx=10, pady=11)

        #C percentage entry
        CEntry = Entry(entryFrame, width=29, bd=3, bg='lavender blush', relief='ridge', font=("arial", 12), textvariable=self.C)
        CEntry.grid(row=6, column=1, sticky='w', padx=10, pady=11)

        #D percentage entry
        DEntry = Entry(entryFrame, width=29, bd=3, bg='lavender blush', relief='ridge', font=("arial", 12), textvariable=self.D)
        DEntry.grid(row=7, column=1, sticky='w', padx=10, pady=11)

        #F percentage entry
        FEntry = Entry(entryFrame, width=29, bd=3, bg='lavender blush', relief='ridge', font=("arial", 12), textvariable=self.F)
        FEntry.grid(row=8, column=1, sticky='w', padx=10, pady=11)

        #CRN entry
        CrnEntry = Entry(entryFrame, width=29, bd=3, bg='lavender blush', relief='ridge', font=("arial", 12), textvariable=self.crn)
        CrnEntry.grid(row=9, column=1, sticky='w', padx=10, pady=11)

        #Faculty type entry
        FaEntry = Entry(entryFrame, width=29, bd=3, bg='lavender blush', relief='ridge', font=("arial", 12), textvariable=self.facultyType)
        FaEntry.grid(row=10, column=1, sticky='w', padx=10, pady=11)

        # ***************Functions*********************
        """
        Function Name: addData()
        Usage: allow administrator to add new data into the databace
        """
        def addData():
            #Connect to my sql
            con = mysql.connect(host="ix.cs.uoregon.edu", port=3673, user="prodrig2", password="irodmario@2001", database="422json")

            #create cursor and get the course crn from the database
            custer = con.cursor() 
            custer.execute("select * from 422json.naturalsciences where crn=%s", (str(self.crn.get()),))

            #get rows of all data and if there is data then return an Error
            rows = custer.fetchall()
            if len(rows) != 0:
                messagebox.showerror('ERROR', "The data is already in the system")
            #Otherwise check if all required categories are filled, if not then return an Error
            else:
                if (self.title.get() == "" or self.name.get() == "" or self.term.get() == "" 
                or self.A.get() == ""  
                or self.B.get() == "" 
                or self.C.get() == "" 
                or self.D.get() == ""
                or self.F.get() == "" 
                or self.crn.get() == ""
                or self.facultyType.get() == ""):
                    messagebox.showerror("ERROR", "Please enter the correct data in each catagory")
                #Otherwise add the entered data into the data base    
                else:
                    #get the title to show that message upon success
                    info = str(self.title.get())
                    #get the title to show that message upon success
                    info2 = str(self.crn.get())

                    #execute mysql and add into database
                    custer.execute("""insert into 422json.naturalsciences values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (self.title.get(),self.term.get(), self.name.get(),
                    self.A.get(), self.B.get(), self.C.get(), self.D.get(), self.F.get(), self.crn.get(), self.facultyType.get()))
                    con.commit()
                    con.close()

                    #clear all data and return success message
                    fetchData()
                    clear()
                    messagebox.showinfo('Success', f'{info} with CRN: {info2} added successfully!')

        """
        Function Name: fetchData()
        Function Usage: Refresh the table with the current data
        """
        def fetchData():
            #connect and run mysql
            con = mysql.connect(host="ix.cs.uoregon.edu", port=3673, user="prodrig2", password="irodmario@2001", database="422json")
            custer = con.cursor()
            custer.execute('select * from 422json.naturalsciences')

            #grab all data
            rows = custer.fetchall()

            #Delete the old table and insert each row in the current database to accomplish refresh
            if rows != 0:
                self.totalrecord.set(len(rows))
                table.delete(*table.get_children())

                for row in rows:
                    table.insert('', END, values=row)
                con.commit()
            con.close()

        """
        Function name: clear()
        Usage: clear all the entries and reset each class value
        """
        def clear():
            #set each class member value to empty string
            self.title.set("")
            self.term.set("")
            self.name.set("")
            self.A.set("")
            self.B.set("")
            self.C.set("")
            self.D.set("")
            self.F.set("")
            self.crn.set("")
            self.facultyType.set("")

        """
        Function name: focus()
        Usage: Auto fill the values when a table item is selected
        """
        def focus(e):
            cursor = table.focus()
            content = table.item(cursor)
            row = content['values']
            self.title.set(row[0])
            self.term.set(row[1])
            self.name.set(row[2])
            self.A.set(row[3])
            self.B.set(row[4])
            self.C.set(row[5])
            self.D.set(row[6])
            self.F.set(row[7])
            self.crn.set(row[8])
            self.facultyType.set(row[9])

        """
        Function Name: update()
        Usage: Allow the administrator user to update the information of a course with certain crn
        """
        def update():
            #If one or more required field is empty, show error
            if (self.title.get() == "" or self.name.get() == "" or self.term.get() == "" 
                or self.A.get() == ""  
                or self.B.get() == "" 
                or self.C.get() == "" 
                or self.D.get() == ""
                or self.F.get() == "" 
                or self.crn.get() == ""
                or self.facultyType.get() == ""):
                    messagebox.showerror("ERROR", "Please enter the correct data in each catagory")
            #otherwise update all categories
            else:
                #store the course crn to find the course in the database
                crn = self.crn.get()

                #connect and execute with mysql database
                con = mysql.connect(host="ix.cs.uoregon.edu", port=3673, user="prodrig2", password="irodmario@2001", database="422json")
                custer = con.cursor()
                #find the selected course and read in each category to acomplish update
                custer.execute('UPDATE 422json.naturalsciences SET COURSE_NAME=%s, TERM=%s, INSTRUCTOR=%s, APREC=%s, BPREC=%s, CPREC=%s, DPREC=%s, FPREC=%s, faculty=%s where crn=%s',
                (self.title.get(),self.term.get(), self.name.get(), self.A.get(), self.B.get(), self.C.get(), self.D.get(), self.F.get(), self.facultyType.get(), self.crn.get()))
                con.commit()
                con.close()
                fetchData()
                clear()
                messagebox.showinfo('Success', f'Course CRN: {crn} is updated in the database')

        """
        Function name: delete()
        Usage: delete a course with the input crn from the database
        """
        def delete():
            #Find selected crn and if crn is not provided then show error message
            if self.crn.get():

                #connect with mysql database
                info = self.crn.get()
                con = mysql.connect(host="ix.cs.uoregon.edu", port=3673, user="prodrig2", password="irodmario@2001", database="422json")
                custer = con.cursor()
                #find the selected crn and delete from the database
                custer.execute("delete from 422json.naturalsciences where crn=%s", (info,))
                con.commit()
                con.close()
                fetchData()
                clear()
                messagebox.showinfo('Success', f'Course CRN: {info} is deleted from the database')
            else:
                messagebox.showinfo('Error', f'invalid CRN to delete')

        """
        Function name: search()
        Usage: find and show the row in the table area for the selected crn
        """
        def search():
            #Get the selected crn
            crn = self.searchText.get()

            #connect with mysql
            con = mysql.connect(host="ix.cs.uoregon.edu", port=3673, user="prodrig2", password="irodmario@2001", database="422json")
            custer = con.cursor()

            #Find the course with selected crn in the database
            custer.execute("select * from 422json.naturalsciences where crn=%s", (crn,))

            #get the table content with the selected crn
            vals = custer.fetchall()

            #Remove everything in the table first then insert back the selected row
            if len(vals) != 0:
                table.delete(*table.get_children())
                for value in vals:
                    table.insert('', END, values=value)
                con.commit()
            else:
                messagebox.showinfo('Not Found', f'Search CRN not found')

            con.close()

                

        # **********Frame-3 Button**************
        #Button entry frame
        btnFrame = Frame(entryFrame, bd=5, relief='ridge', bg='lavender blush')
        btnFrame.place(x=15, y=590, width=310, height=120)

        #place add button
        addBtn = Button(btnFrame, text='Add', font=("", 12), command=addData, width="7", bg='lavender blush')
        addBtn.grid(row=0, column=1, padx=50, pady=10)

        #place update button
        updateBtn = Button(btnFrame, text='Update', font=("", 12), command=update, width="7", bg='lavender blush')
        updateBtn.grid(row=0, column=2, padx=10, pady=10)

        #place delete button
        deleteBtn = Button(btnFrame, text='Delete', font=("", 12), command=delete, width="7", bg='lavender blush')
        deleteBtn.grid(row=1, column=1, padx=50, pady=10)

        #place clear button
        clearBtn = Button(btnFrame, text='Clear', font=("", 12), command=clear, width="7", bg='lavender blush')
        clearBtn.grid(row=1, column=2, padx=10, pady=10)

        # ***********Frame-2***************
        #second data frame for the searching area
        dataFrame = Frame(root, bd=5, relief='ridge', bg='lavender blush')
        dataFrame.place(x=380, y=50, width=1145, height=745)

        #place search label, entry and button
        searchLabel = Label(dataFrame, text="Search by CRN", font=("", 13), bg='lavender blush')
        searchLabel.grid(row=0, column=0, sticky='w', padx=10, pady=14)
        searchEntry = Entry(dataFrame, bd=3, relief='ridge', font=("", 12), width=15, textvariable=self.searchText)
        searchEntry.grid(row=0, column=1, sticky='w', padx=10, pady=14)
        showBtn = Button(dataFrame, text='Find', font=("", 12), command=search)
        showBtn.grid(row=0, column=3, padx=10, pady=10)

        #Holds the total count of courses stored in the database and place the label
        totalLabel = Label(dataFrame, text="Total Records", font=("", 13), bg='lavender blush')
        totalLabel.grid(row=1, column=0, sticky='w', padx=10, pady=8)
        totalrecordLabel = Label(dataFrame, text="Total Records", font=("", 13), textvariable=self.totalrecord)
        totalrecordLabel.grid(row=1, column=1, sticky='w', padx=10, pady=8)

        # ************Frame-3 Treeview***************
        # Third data frame that display the view of table
        viewFrame = Frame(dataFrame, bd=5, relief='ridge', bg='wheat')
        viewFrame.place(x=20, y=100, width=1080, height=620)

        #The horizontal and verticle scroll bars
        xScroll = Scrollbar(viewFrame, orient=HORIZONTAL)
        yScroll = Scrollbar(viewFrame, orient=VERTICAL)

        #Create a table with variable that represents class memebrs
        table=ttk.Treeview(viewFrame,columns=('title.','term','name','A','B','C','D','F','crn', 'faculty.'),xscrollcommand=xScroll.set,yscrollcommand=yScroll.set)
        
        #pack the scroll bars onto the UI
        xScroll.pack(side=BOTTOM, fill=X)
        yScroll.pack(side=RIGHT, fill=Y)
        xScroll.configure(command=table.xview)
        yScroll.configure(command=table.yview)

        #Bound each table column variable with the corresponding class member
        table.heading("title.", text="Title")
        table.heading("term", text="term")
        table.heading("name", text="Instructor")
        table.heading("A", text="A percentage")
        table.heading("B", text="B percentage")
        table.heading("C", text="C percentage")
        table.heading("D", text="D percentage")
        table.heading("F", text="F percentage")
        table.heading("crn", text="CRN")
        table.heading("faculty.", text="Faculty Type")

        #set each table column and its attributs
        table.column("title.", width=100)
        table.column("term", width=100)
        table.column("name", width=100)
        table.column("A", width=100)
        table.column("B", width=100)
        table.column("C", width=100)
        table.column("D", width=100)
        table.column("F", width=100)
        table.column("crn", width=100)
        table.column("faculty.", width=100)
        table['show'] = 'headings'

        #allow user to select and auto fill when selecting from the table
        table.bind('<ButtonRelease-1>', focus)

        #get all values and pack the table on to the screen
        fetchData()
        table.pack(fill=BOTH, expand=1)

#Initialize and run tkiner 
root = Tk()
ob = Admin(root)
root.mainloop()