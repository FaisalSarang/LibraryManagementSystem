import tkinter
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title= ("Library Management System")
        self.root.geometry("1550x800+0+0")

        #Variable
        self.member_var=StringVar()
        self.rollno_var=StringVar()
        self.title_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address_var=StringVar()
        self.mobileno_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.actualprice_var=StringVar()


        lbltitle = Label(self.root, text = "LIBRARY MANAGEMENT SYSTEM", bg = "#d5ba8c",fg = "#aa182c", bd = 20, relief=RIDGE,font = ("times new roman", 50, "bold"), padx = 2, pady = 6)
        lbltitle.pack(side=TOP,fill=X)

        frame = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#d5ba8c")
        frame.place(x=0,y=130,width=1530,height=400)

        #Left Frame
        DataFrameLeft = LabelFrame(frame, text = "Library Members Information", bg = "#eadcc5",fg = "#653a2b", bd = 12, relief=RIDGE,font = ("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember = Label(DataFrameLeft, text="Member Type",  bg = "#eadcc5",fg = "#653a2b", font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember = ttk.Combobox(DataFrameLeft,font=("Times New Roman",12,"bold"), textvariable=self.member_var, width=27, state="readonly")
        comMember["value"] = ("Admin","Professor","Assisstant Professor","Student")
        comMember.grid(row=0,column=1)

        lblRollNo = Label(DataFrameLeft, text="Roll No", bg = "#eadcc5",fg = "#653a2b", font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lblRollNo.grid(row=1,column=0,sticky=W)
        txtRollNo = Entry(DataFrameLeft, textvariable=self.rollno_var, font=("Times New Roman",15,"bold"),width=23)
        txtRollNo.grid(row=1,column=1, padx=2,pady=6)

        lblTitle = Label(DataFrameLeft, text="Title", bg = "#eadcc5",fg = "#653a2b", font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle = ttk.Combobox(DataFrameLeft,font=("Times New Roman",12,"bold"), textvariable=self.title_var, width=27, state="readonly")
        txtTitle["value"] = ("Mr","Ms","Mrs")
        txtTitle.grid(row=2,column=1, padx=2,pady=6)

        lblFirstName = Label(DataFrameLeft, text="First Name", bg = "#eadcc5",fg = "#653a2b", font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("Times New Roman",15,"bold"), textvariable=self.firstname_var,width=23)
        txtFirstName.grid(row=3,column=1, padx=2,pady=6)

        lblLastName = Label(DataFrameLeft, text="Last Name",  bg = "#eadcc5",fg = "#653a2b", font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("Times New Roman",15,"bold"), textvariable=self.lastname_var,width=23)
        txtLastName.grid(row=4,column=1, padx=2,pady=6)

        lblAddress = Label(DataFrameLeft, text="Address",  bg = "#eadcc5",fg = "#653a2b", font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lblAddress.grid(row=5,column=0,sticky=W)
        txtAddress = Entry(DataFrameLeft, font=("Times New Roman",15,"bold"), textvariable=self.address_var,width=23)
        txtAddress.grid(row=5,column=1, padx=2,pady=6)

        lblMobile = Label(DataFrameLeft, text="Mobile No", bg = "#eadcc5",fg = "#653a2b", font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lblMobile.grid(row=6,column=0,sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("Times New Roman",15,"bold"), textvariable=self.mobileno_var, width=23)
        txtMobile.grid(row=6,column=1, padx=2,pady=6)

        lblBookID = Label(DataFrameLeft, text="Book ID", bg = "#eadcc5",fg = "#653a2b", font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lblBookID.grid(row=0,column=3,sticky=W)
        txtBookID = Entry(DataFrameLeft, font=("Times New Roman",15,"bold"), textvariable=self.bookid_var, width=23)
        txtBookID.grid(row=0,column=4, padx=2,pady=6)

        lblBookTitle = Label(DataFrameLeft, text="Book Title", bg = "#eadcc5",fg = "#653a2b", font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=3,sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("Times New Roman",15,"bold"), textvariable=self.booktitle_var, width=23)
        txtBookTitle.grid(row=1,column=4, padx=2,pady=6)

        lblAuthor = Label(DataFrameLeft, text="Author",  bg = "#eadcc5",fg = "#653a2b", font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=3,sticky=W)
        txtAuthor = Entry(DataFrameLeft, font=("Times New Roman",15,"bold"), textvariable=self.author_var,width=23)
        txtAuthor.grid(row=2,column=4, padx=2,pady=6)

        lblDateBorrowed = Label(DataFrameLeft, text="Date Borrowed", bg = "#eadcc5",fg = "#653a2b", font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=3,sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=("Times New Roman",15,"bold"), textvariable=self.dateborrowed_var, width=23)
        txtDateBorrowed.grid(row=3,column=4, padx=2,pady=6)

        lblDateDue = Label(DataFrameLeft, text="Date Due", bg = "#eadcc5",fg = "#653a2b", font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=3,sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=("Times New Roman",15,"bold"), textvariable=self.datedue_var, width=23)
        txtDateDue.grid(row=4,column=4, padx=2,pady=6)

        lblLateReturnFine = Label(DataFrameLeft, text="Late Return Fine", bg = "#eadcc5",fg = "#653a2b", font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=5,column=3,sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=("Times New Roman",15,"bold"), textvariable=self.latereturnfine_var, width=23)
        txtLateReturnFine.grid(row=5,column=4, padx=2,pady=6)

        lblActualPrice = Label(DataFrameLeft, text="Actual Price", bg = "#eadcc5",fg = "#653a2b", font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=6,column=3,sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=("Times New Roman",15,"bold"), textvariable=self.actualprice_var, width=23)
        txtActualPrice.grid(row=6,column=4, padx=2,pady=6)



        #Right Frame    
        DataFrameRight = LabelFrame(frame, text = "Book Details", bg = "#eadcc5",fg = "#653a2b", bd = 12, relief=RIDGE,font = ("times new roman", 12, "bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtBox=Text(DataFrameRight, font=("Times New Roman",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        
        # listBooks=[ "To Kill a Mockingbird",
        #     "1984",
        #     "Pride and Prejudice",
        #     "The Great Gatsby",
        #     "Moby Dick",
        #     "War and Peace",
        #     "Crime and Punishment",
        #     "The Catcher in the Rye",
        #     "The Lord of the Rings",
        #     "Jane Eyre",
        #     "Animal Farm",
        #     "The Hobbit",
        #     "Brave New World",
        #     "Wuthering Heights",
        #     "Harry Potter and the Sorcerer's Stone",
        #     "The Alchemist",
        #     "The Kite Runner",
        #     "Great Expectations",
        #     "The Chronicles of Narnia",
        #     "Gone with the Wind",
        #     "The Odyssey",
        #     "Les Misérables",
        #     "Dracula",
        #     "A Tale of Two Cities",
        #     "The Shining",
        #     "The Picture of Dorian Gray",
        #     "Don Quixote",
        #     "The Secret Garden",
        #     "Little Women",
        #     "The Divine Comedy",
        #     "Frankenstein",
        #     "The Iliad",
        #     "Emma",
        #     "The Color Purple",
        #     "Anna Karenina",
        #     "The Grapes of Wrath",
        #     "The Da Vinci Code",
        #     "The Hunger Games",
        #     "Fahrenheit 451",
        #     "Life of Pi",
        #     "Catch-22",
        #     "The Road",
        #     "Beloved",
        #     "Dune",
        #     "Slaughterhouse-Five",
        #     "The Book Thief",
        #     "The Girl with the Dragon Tattoo",
        #     "Ender's Game",
        #     "The Handmaid's Tale",
        #     "The Sun Also Rises",
        #     "A Clockwork Orange",
        #     "One Hundred Years of Solitude",
        #     "The Old Man and the Sea",
        #     "Invisible Man",
        #     "The Bell Jar",
        #     "The Stranger",
        #     "The Fountainhead",
        #     "Siddhartha",
        #     "A Brave New World",
        #     "The Secret History",
        #     "Middlemarch",
        #     "The Goldfinch",
        #     "The Brothers Karamazov",
        #     "The Time Traveler's Wife",
        #     "Atlas Shrugged",
        #     "Watership Down",
        #     "Norwegian Wood",
        #     "Lolita",
        #     "The Poisonwood Bible",
        #     "Memoirs of a Geisha",
        #     "The Light We Cannot See",
        #     "A Game of Thrones",
        #     "Pillars of the Earth",
        #     "Rebecca",
        #     "The Joy Luck Club",
        #     "On the Road",
        #     "Ulysses",
        #     "The Name of the Rose",
        #     "The Wind-Up Bird Chronicle",
        #     "Good Omens",
        #     "The Stand",
        #     "The Prince",
        #     "The Art of War",
        #     "The Little Prince",
        #     "Man's Search for Meaning",
        #     "The Power of Now",
        #     "Thinking, Fast and Slow",
        #     "Rich Dad Poor Dad",
        #     "How to Win Friends and Influence People",
        #     "Sapiens: A Brief History of Humankind",
        #     "The Subtle Art of Not Giving a F*ck",
        #     "Atomic Habits",
        #     "Educated",
        #     "Becoming",
        #     "The Four Agreements",
        #     "The 7 Habits of Highly Effective People"
        # ]

        listBooks = {
        "To Kill a Mockingbird": {"book_id": "110001", "author": "Harper Lee", "price": "45 SAR", "late_fee": "50 SAR"},
        "1984": {"book_id": "110002", "author": "George Orwell", "price": "40 SAR", "late_fee": "50 SAR"},
        "Pride and Prejudice": {"book_id": "110003", "author": "Jane Austen", "price": "30 SAR", "late_fee": "40 SAR"},
        "The Great Gatsby": {"book_id": "110004", "author": "F. Scott Fitzgerald", "price": "35 SAR", "late_fee": "45 SAR"},
        "Moby Dick": {"book_id": "110005", "author": "Herman Melville", "price": "50 SAR", "late_fee": "55 SAR"},
        "War and Peace": {"book_id": "110006", "author": "Leo Tolstoy", "price": "60 SAR", "late_fee": "60 SAR"},
        "Crime and Punishment": {"book_id": "110007", "author": "Fyodor Dostoevsky", "price": "55 SAR", "late_fee": "60 SAR"},
        "The Catcher in the Rye": {"book_id": "110008", "author": "J.D. Salinger", "price": "40 SAR", "late_fee": "45 SAR"},
        "The Lord of the Rings": {"book_id": "110009", "author": "J.R.R. Tolkien", "price": "75 SAR", "late_fee": "80 SAR"},
        "Jane Eyre": {"book_id": "110010", "author": "Charlotte Brontë", "price": "45 SAR", "late_fee": "50 SAR"},
        "Animal Farm": {"book_id": "110011", "author": "George Orwell", "price": "30 SAR", "late_fee": "35 SAR"},
        "The Hobbit": {"book_id": "110012", "author": "J.R.R. Tolkien", "price": "50 SAR", "late_fee": "55 SAR"},
        "Brave New World": {"book_id": "110013", "author": "Aldous Huxley", "price": "40 SAR", "late_fee": "45 SAR"},
        "Wuthering Heights": {"book_id": "110014", "author": "Emily Brontë", "price": "45 SAR", "late_fee": "50 SAR"},
        "Harry Potter and the Sorcerer's Stone": {"book_id": "110015", "author": "J.K. Rowling", "price": "60 SAR", "late_fee": "65 SAR"},
        "The Alchemist": {"book_id": "110016", "author": "Paulo Coelho", "price": "35 SAR", "late_fee": "40 SAR"},
        "The Kite Runner": {"book_id": "110017", "author": "Khaled Hosseini", "price": "45 SAR", "late_fee": "50 SAR"},
        "Great Expectations": {"book_id": "110018", "author": "Charles Dickens", "price": "40 SAR", "late_fee": "45 SAR"},
        "The Chronicles of Narnia": {"book_id": "110019", "author": "C.S. Lewis", "price": "70 SAR", "late_fee": "75 SAR"},
        "Gone with the Wind": {"book_id": "110020", "author": "Margaret Mitchell", "price": "55 SAR", "late_fee": "60 SAR"},
        "The Odyssey": {"book_id": "110021", "author": "Homer", "price": "65 SAR", "late_fee": "70 SAR"},
        "Les Misérables": {"book_id": "110022", "author": "Victor Hugo", "price": "70 SAR", "late_fee": "75 SAR"},
        "Dracula": {"book_id": "110023", "author": "Bram Stoker", "price": "40 SAR", "late_fee": "45 SAR"},
        "A Tale of Two Cities": {"book_id": "110024", "author": "Charles Dickens", "price": "45 SAR", "late_fee": "50 SAR"},
        "The Shining": {"book_id": "110025", "author": "Stephen King", "price": "50 SAR", "late_fee": "55 SAR"},
        "The Picture of Dorian Gray": {"book_id": "110026", "author": "Oscar Wilde", "price": "40 SAR", "late_fee": "45 SAR"},
        "Don Quixote": {"book_id": "110027", "author": "Miguel de Cervantes", "price": "60 SAR", "late_fee": "65 SAR"},
        "The Secret Garden": {"book_id": "110028", "author": "Frances Hodgson Burnett", "price": "35 SAR", "late_fee": "40 SAR"},
        "Little Women": {"book_id": "110029", "author": "Louisa May Alcott", "price": "45 SAR", "late_fee": "50 SAR"},
        "The Divine Comedy": {"book_id": "110030", "author": "Dante Alighieri", "price": "65 SAR", "late_fee": "70 SAR"},
        "Frankenstein": {"book_id": "110031", "author": "Mary Shelley", "price": "40 SAR", "late_fee": "45 SAR"},
        "The Iliad": {"book_id": "110032", "author": "Homer", "price": "65 SAR", "late_fee": "70 SAR"},
        "Emma": {"book_id": "110033", "author": "Jane Austen", "price": "40 SAR", "late_fee": "45 SAR"},
        "The Color Purple": {"book_id": "110034", "author": "Alice Walker", "price": "45 SAR", "late_fee": "50 SAR"},
        "Anna Karenina": {"book_id": "110035", "author": "Leo Tolstoy", "price": "60 SAR", "late_fee": "65 SAR"},
        "The Grapes of Wrath": {"book_id": "110036", "author": "John Steinbeck", "price": "50 SAR", "late_fee": "55 SAR"},
        "The Da Vinci Code": {"book_id": "110037", "author": "Dan Brown", "price": "55 SAR", "late_fee": "60 SAR"},
        "The Hunger Games": {"book_id": "110038", "author": "Suzanne Collins", "price": "45 SAR", "late_fee": "50 SAR"},
        "Fahrenheit 451": {"book_id": "110039", "author": "Ray Bradbury", "price": "40 SAR", "late_fee": "45 SAR"},
        "Life of Pi": {"book_id": "110040", "author": "Yann Martel", "price": "50 SAR", "late_fee": "55 SAR"},
        "Catch-22": {"book_id": "110041", "author": "Joseph Heller", "price": "45 SAR", "late_fee": "50 SAR"},
        "The Road": {"book_id": "110042", "author": "Cormac McCarthy", "price": "50 SAR", "late_fee": "55 SAR"},
        "Beloved": {"book_id": "110043", "author": "Toni Morrison", "price": "45 SAR", "late_fee": "50 SAR"},
        "Dune": {"book_id": "110044", "author": "Frank Herbert", "price": "60 SAR", "late_fee": "65 SAR"},
        "Slaughterhouse-Five": {"book_id": "110045", "author": "Kurt Vonnegut", "price": "45 SAR", "late_fee": "50 SAR"},
        "The Book Thief": {"book_id": "110046", "author": "Markus Zusak", "price": "50 SAR", "late_fee": "55 SAR"},
        "The Girl with the Dragon Tattoo": {"book_id": "110047", "author": "Stieg Larsson", "price": "55 SAR", "late_fee": "60 SAR"},
        "Ender's Game": {"book_id": "110048", "author": "Orson Scott Card", "price": "45 SAR", "late_fee": "50 SAR"},
        "The Handmaid's Tale": {"book_id": "110049", "author": "Margaret Atwood", "price": "50 SAR", "late_fee": "55 SAR"},
        "The Sun Also Rises": {"book_id": "110050", "author": "Ernest Hemingway", "price": "40 SAR", "late_fee": "45 SAR"},}


        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if value in listBooks:
                book_details = listBooks[value]
                self.bookid_var.set(book_details["book_id"])
                self.booktitle_var.set(value)
                self.author_var.set(book_details["author"])

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set(book_details["late_fee"])
                self.actualprice_var.set(book_details["price"])

        listBox = Listbox(DataFrameRight, font=("Times New Roman",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)
        
        for item in listBooks:
            listBox.insert(END,item)

        #Buttons Frame
        FrameButton = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#d5ba8c")
        FrameButton.place(x=0,y=530,width=1530,height=70)

        btnAddData = Button(FrameButton,text="Add Data", command=self.add_data,font = ("times new roman", 12, "bold"), bg = "#eadcc5",fg = "#653a2b", width=26)
        btnAddData.grid(row=0,column=0)

        btnAddData = Button(FrameButton,text="Show Data", command=self.ShowData, font = ("times new roman", 12, "bold"), bg = "#eadcc5",fg = "#653a2b", width=26)
        btnAddData.grid(row=0,column=1)

        btnAddData = Button(FrameButton,text="Update", command=self.update, font = ("times new roman", 12, "bold"), bg = "#eadcc5",fg = "#653a2b", width=26)
        btnAddData.grid(row=0,column=2)

        btnAddData = Button(FrameButton,text="Delete", command=self.delete, font = ("times new roman", 12, "bold"), bg = "#eadcc5",fg = "#653a2b", width=26)
        btnAddData.grid(row=0,column=3)

        btnAddData = Button(FrameButton,text="Reset", command=self.reset, font = ("times new roman", 12, "bold"), bg = "#eadcc5",fg = "#653a2b", width=26)
        btnAddData.grid(row=0,column=4)

        btnAddData = Button(FrameButton,text="Exit", command=self.iExit, font = ("times new roman", 12, "bold"), bg = "#eadcc5",fg = "#653a2b", width=26)
        btnAddData.grid(row=0,column=5)

        #Information Frame
        FrameInformation = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#d5ba8c")
        FrameInformation.place(x=0,y=600,width=1530,height=195)

        Table_frame = Frame(FrameInformation,bd=6,relief=RIDGE,bg="#d5ba8c")
        Table_frame.place(x=0,y=2,width=1460,height=165)

        xscroll = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_frame,columns=("MemberType","RollNo","Title","FirstName","LastName","Address","MobileNo","BookID","BookTitle","Author","DateBorrowed","DateDue","LateReturnFine","ActualPrice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("MemberType", text="Member Type")
        self.library_table.heading("RollNo", text="Roll No")
        self.library_table.heading("Title", text="Title")
        self.library_table.heading("FirstName", text="First Name")
        self.library_table.heading("LastName", text="Last Name")
        self.library_table.heading("Address", text="Address")
        self.library_table.heading("MobileNo", text="Mobile No")
        self.library_table.heading("BookID", text="Book ID")
        self.library_table.heading("BookTitle", text="Book Title")
        self.library_table.heading("Author", text="Author")
        self.library_table.heading("DateBorrowed", text="Date Borrowed")
        self.library_table.heading("DateDue", text="Date Due")
        self.library_table.heading("LateReturnFine", text="Late Return Fine")
        self.library_table.heading("ActualPrice", text="Actual Price")
        
        
        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("MemberType", width=100)
        self.library_table.column("RollNo", width=100)
        self.library_table.column("Title", width=100)
        self.library_table.column("FirstName", width=100)
        self.library_table.column("LastName", width=100)
        self.library_table.column("Address", width=100)
        self.library_table.column("MobileNo", width=100)
        self.library_table.column("BookID", width=100)
        self.library_table.column("BookTitle", width=100)
        self.library_table.column("Author", width=100)
        self.library_table.column("DateBorrowed", width=100)
        self.library_table.column("DateDue", width=100)
        self.library_table.column("LateReturnFine", width=100)
        self.library_table.column("ActualPrice", width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def update(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="password",database="library")
        my_cursor = conn.cursor()
        my_cursor.execute("update librarydb set Member=%s,Title=%s,FirstName=%s,LastName=%s,Address=%s,MobileNo=%s,BookID=%s,BookTitle=%s,Author=%s,DateBorrowed=%s,DateDue=%s,LateReturnFine=%s,ActualPrice=%s WHERE RollNo=%s",(
            self.member_var.get(),
            self.title_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address_var.get(),
            self.mobileno_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.latereturnfine_var.get(),
            self.actualprice_var.get(),
            self.rollno_var.get()
        ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been updated!")

    def add_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="password",database="library")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into librarydb values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.member_var.get(),
            self.rollno_var.get(),
            self.title_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address_var.get(),
            self.mobileno_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.latereturnfine_var.get(),
            self.actualprice_var.get()
        ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success!","Member has been added successfully!")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="password",database="library")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from librarydb")
        rows = my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content["values"]

        self.member_var.set(row[0])
        self.rollno_var.set(row[1])
        self.title_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address_var.set(row[5])
        self.mobileno_var.set(row[6])
        self.bookid_var.set(row[7])
        self.booktitle_var.set(row[8])
        self.author_var.set(row[9])
        self.dateborrowed_var.set(row[10])
        self.datedue_var.set(row[11])
        self.latereturnfine_var.set(row[12])
        self.actualprice_var.set(row[13])

    def ShowData(self):
        self.txtBox.insert(END,"Member Type\t\t" + self.member_var.get() + "\n")
        self.txtBox.insert(END,"Roll No\t\t" + self.rollno_var.get() + "\n")
        self.txtBox.insert(END,"Title\t\t" + self.title_var.get() + "\n")
        self.txtBox.insert(END,"First Name\t\t" + self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"Last Name\t\t" + self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address\t\t" + self.address_var.get() + "\n")
        self.txtBox.insert(END,"Mobile No\t\t" + self.mobileno_var.get() + "\n")
        self.txtBox.insert(END,"Book ID\t\t" + self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title\t\t" + self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Author\t\t" + self.author_var.get() + "\n")
        self.txtBox.insert(END,"Date Borrowed\t\t" + self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"Date Due\t\t" + self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"Late Return Fine\t\t" + self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END,"Actual Price\t\t" + self.actualprice_var.get() + "\n")

    def reset(self):
        self.member_var.set("")
        self.rollno_var.set("")
        self.title_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address_var.set("")
        self.mobileno_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.author_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.latereturnfine_var.set("")
        self.actualprice_var.set("")
        self.txtBox.delete("1.0",END)

    

    # def delete(self):
    #     if self.rollno_var.get()=="":
    #         messagebox.showerror("Error","Select a member first")
    #     else:
    #         conn = mysql.connector.connect(host="localhost",username="root",password="password",database="library")
    #         my_cursor = conn.cursor()
    #         my_cursor.execute("delete from librarydb where RollNo=%s",(self.rollno_var.get(),))

    #         conn.commit()
    #         self.fetch_data()
    #         self.reset()
    #         conn.close()

    #         messagebox.showinfo("Success","Member has been deleted successfully")
        
    def delete(self):
        if self.rollno_var.get() == "":
            messagebox.showerror("Error", "Select a member first")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="password", database="library")
            my_cursor = conn.cursor()

            my_cursor.execute("DELETE FROM librarydb WHERE RollNo=%s", (self.rollno_var.get(),))
            
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("Success", "Member has been deleted successfully")
            print("fetch_data() called after delete.")


        
    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Library Management System", "Do you want to exit?")
        if iExit>0:
            self.root.destroy()
            return

if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()