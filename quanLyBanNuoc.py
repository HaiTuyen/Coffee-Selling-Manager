from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import datetime


class Manager():
    def __init__(self):
        super().__init__()

        self.root = Tk() # Create the root window
        self.root.title("Coffee Selling Manager") # Create title of root window
        self.root.resizable(False, False)

        self.centerWindow() # Center the root window on the screen
        self.progTitle() # Create header for root window

        self.root.config(bg='#FFF2CC')
        self.root.iconbitmap("managerlogo.ico")
        
    def centerWindow(self):
        window_width = 1000
        window_height = 650

        # get the screen dimension
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y-30}')

    def progTitle(self):
        self.label_title = Label(self.root, text="HAI TUYEN'S COFFEE HOUSE", font= ('Roboto 20 bold'), bg="#FFFFFF", fg="#843C0C")
        #self.label_title.grid(row=0, column=0, ipadx=317, columnspan=2)
        self.label_title.pack(fill="x", pady=(10,0))



class infoFrame():
    def __init__(self, root):
        self.wrapper1 = LabelFrame(root, bd=5, bg="#FFE699")
        self.wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
        self.mycanvas = Canvas(self.wrapper1, width=900, height=350, highlightthickness=0, bg="#FFE699")
        self.mycanvas.pack(side=LEFT, fill="y", padx=10)

        yscrollbar = ttk.Scrollbar(self.wrapper1, orient="vertical", command=self.mycanvas.yview)
        yscrollbar.pack(side=RIGHT, fill="y")
        self.mycanvas.configure(yscrollcommand=yscrollbar.set)
        self.mycanvas.bind('<Configure>', lambda e: self.mycanvas.configure(scrollregion = self.mycanvas.bbox('all')))
        self.myframe = Frame(self.mycanvas, bg="#FFE699")
        self.mycanvas.create_window((0,0), window=self.myframe, anchor="nw")

        #Create a list of variables
        self.var = ['', '', '', [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], 
                        [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], 0, '']
        
        self.var[0] = StringVar() # Name
        self.var[1] = StringVar() # Phone
        self.var[2] = StringVar() # Email

        self.var[3][0] = IntVar() # Phin Sữa Đá
        self.var[3][1] = IntVar() 
        self.var[3][2] = IntVar() 
         
        self.var[4][0] = IntVar() # Phin Đen Đá
        self.var[4][1] = IntVar() 
        self.var[4][2] = IntVar()
        
        self.var[5][0] = IntVar() # Bạc Xĩu Đá
        self.var[5][1] = IntVar() 
        self.var[5][2] = IntVar() 
        
        self.var[6][0] = IntVar() # Espresso
        self.var[6][1] = IntVar() 
        self.var[6][2] = IntVar()
        
        self.var[7][0] = IntVar() # Cappuccino
        self.var[7][1] = IntVar()
        self.var[7][2] = IntVar()
        
        self.var[8][0] = IntVar() # Mocha
        self.var[8][1] = IntVar()
        self.var[8][2] = IntVar()
        
        self.var[9][0] = IntVar() # Trà Sen Vàng
        self.var[9][1] = IntVar()
        self.var[9][2] = IntVar()
        
        self.var[10][0] = IntVar() # Trà Thạch Đào
        self.var[10][1] = IntVar()
        self.var[10][2] = IntVar()
        
        self.var[11][0] = IntVar() # Trà Thạch Vải
        self.var[11][1] = IntVar()
        self.var[11][2] = IntVar()
        
        self.var[12][0] = IntVar() # Trà xanh đậu đỏ
        self.var[12][1] = IntVar()
        self.var[12][2] = IntVar()
        
        self.var[13][0] = IntVar() # Freeze Trà Xanh
        self.var[13][1] = IntVar()
        self.var[13][2] = IntVar()
        
        self.var[14][0] = IntVar() # Freeze Sô-cô-la
        self.var[14][1] = IntVar()
        self.var[14][2] = IntVar()
        
        self.var[15][0] = IntVar() # Freeze Cookies
        self.var[15][1] = IntVar()
        self.var[15][2] = IntVar()
        
        self.var[16][0] = IntVar() # Freeze Xanh Đậu Đỏ
        self.var[16][1] = IntVar()
        self.var[16][2] = IntVar()
        
        self.var[17][0] = IntVar() # Freeze Classic Phin
        self.var[17][1] = IntVar() 
        self.var[17][2] = IntVar()
        
        self.var[18][0] = IntVar() # Chanh Đá Xay
        self.var[18][1] = IntVar()
        self.var[18][2] = IntVar()
        
        self.var[19][0] = IntVar() # Chanh Dây Đá
        self.var[19][1] = IntVar()
        self.var[19][2] = IntVar()

        self.var[20][0] = IntVar() # Tắc Đá Viên
        self.var[20][1] = IntVar()
        self.var[20][2] = IntVar()

        self.var[21][0] = IntVar() # Sô-cô-la
        self.var[21][1] = IntVar() 
        self.var[21][2] = IntVar()

        self.var[22][0] = IntVar() # Sữa Chua Đá
        self.var[22][1] = IntVar()
        self.var[22][2] = IntVar()

        self.var[23] = 0 # Total cost 
        

    def show(self):
        #---LABEL: CÀ PHÊ PHA PHIN
        self.label_name = Label(self.myframe, text="CÀ PHÊ PHA PHIN", bg="#FFE699", font=('Calibri(Body) 11 bold italic underline'))
        self.label_name.grid(row=0, column=0, pady=(10,0), sticky="w")
        
        # Label: Phin Sữa Đá
        self.label_name = Label(self.myframe, text="Phin Sữa Đá", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=1, column=0, pady=(10,0), sticky="w")
        # Size: Phin Sữa Đá
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=1, column=1, pady=(10,0), sticky="w", padx=(100,0))
        self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[3][0])
        self.entry1_1.grid(row=1, column=2, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=1, column=3, pady=(10,0), padx=(30,0), sticky="w")
        self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[3][1])
        self.entry1_2.grid(row=1, column=4, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=1, column=5, pady=(10,0), padx=(30,0),sticky="w")
        self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[3][2])
        self.entry1_3.grid(row=1, column=6, pady=(10,0), sticky="w")

        #Label: Phin Đen Đá
        self.label_name = Label(self.myframe, text="Phin Đen Đá", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=2, column=0, pady=(5,0), sticky="w")
        #Size: Phin Đen Đá
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=2, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry2_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[4][0])
        self.entry2_1.grid(row=2, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=2, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry2_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[4][1])
        self.entry2_2.grid(row=2, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=2, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry2_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[4][2])
        self.entry2_3.grid(row=2, column=6, pady=(5,0), sticky="w")

        #Label: Bạc Xĩu Đá
        self.label_name = Label(self.myframe, text="Bạc Xĩu Đá", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=3, column=0, pady=(5,0), sticky="w")
        #Size: Bạc Xĩu Đá 
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=3, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry3_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[5][0])
        self.entry3_1.grid(row=3, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=3, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry3_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[5][1])
        self.entry3_2.grid(row=3, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=3, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry3_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[5][2])
        self.entry3_3.grid(row=3, column=6, pady=(5,0), sticky="w")

        #---LABEL: CÀ PHÊ ESPRESSO
        self.label_name = Label(self.myframe, text="CÀ PHÊ ESPRESSO", bg="#FFE699", font=('Calibri(Body) 11 bold italic underline'))
        self.label_name.grid(row=4, column=0, pady=(10,0), sticky="w")
        
        # Label: Espresso/Americano
        self.label_name = Label(self.myframe, text="Espresso/Americano", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=5, column=0, pady=(10,0), sticky="w")
        # Size: Espresso/Americano
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=5, column=1, pady=(10,0), sticky="w", padx=(100,0))
        self.entry4_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[6][0])
        self.entry4_1.grid(row=5, column=2, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=5, column=3, pady=(10,0), padx=(30,0), sticky="w")
        self.entry4_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[6][1])
        self.entry4_2.grid(row=5, column=4, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=5, column=5, pady=(10,0), padx=(30,0),sticky="w")
        self.entry4_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[6][2])
        self.entry4_3.grid(row=5, column=6, pady=(10,0), sticky="w")

        #Label: Cappuccino/Latte
        self.label_name = Label(self.myframe, text="Cappuccino/Latte", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=6, column=0, pady=(5,0), sticky="w")
        #Size: Cappuccino/Latte
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=6, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry5_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[7][0])
        self.entry5_1.grid(row=6, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=6, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry5_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[7][1])
        self.entry5_2.grid(row=6, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=6, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry5_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[7][2])
        self.entry5_3.grid(row=6, column=6, pady=(5,0), sticky="w")

        #Label: Mocha/Macchiato
        self.label_name = Label(self.myframe, text="Mocha/Macchiato", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=7, column=0, pady=(5,0), sticky="w")
        #Size: Mocha/Macchiato
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=7, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry6_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[8][0])
        self.entry6_1.grid(row=7, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=7, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry6_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[8][1])
        self.entry6_2.grid(row=7, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=7, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry6_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[8][2])
        self.entry6_3.grid(row=7, column=6, pady=(5,0), sticky="w")

        #---LABEL: TRÀ
        self.label_name = Label(self.myframe, text="TRÀ", bg="#FFE699", font=('Calibri(Body) 11 bold italic underline'))
        self.label_name.grid(row=8, column=0, pady=(10,0), sticky="w")
        
        # Label: Sen Vàng
        self.label_name = Label(self.myframe, text="Sen Vàng", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=9, column=0, pady=(10,0), sticky="w")
        # Size: Sen Vàng
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=9, column=1, pady=(10,0), sticky="w", padx=(100,0))
        self.entry7_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[9][0])
        self.entry7_1.grid(row=9, column=2, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=9, column=3, pady=(10,0), padx=(30,0), sticky="w")
        self.entry7_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[9][1])
        self.entry7_2.grid(row=9, column=4, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=9, column=5, pady=(10,0), padx=(30,0),sticky="w")
        self.entry7_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[9][2])
        self.entry7_3.grid(row=9, column=6, pady=(10,0), sticky="w")

        #Label: Thạch Đào
        self.label_name = Label(self.myframe, text="Thạch Đào", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=10, column=0, pady=(5,0), sticky="w")
        #Size: Thạch Đào
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=10, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry8_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[10][0])
        self.entry8_1.grid(row=10, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=10, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry8_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[10][1])
        self.entry8_2.grid(row=10, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=10, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry8_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[10][2])
        self.entry8_3.grid(row=10, column=6, pady=(5,0), sticky="w")

        #Label: Thạch Vải
        self.label_name = Label(self.myframe, text="Thạch Vải", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=11, column=0, pady=(5,0), sticky="w")
        #Size: Thạch Vải
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=11, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry9_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[11][0])
        self.entry9_1.grid(row=11, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=11, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry9_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[11][1])
        self.entry9_2.grid(row=11, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=11, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry9_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[11][2])
        self.entry9_3.grid(row=11, column=6, pady=(5,0), sticky="w")

        #Label: Xanh Đậu Đỏ
        self.label_name = Label(self.myframe, text="Xanh Đậu Đỏ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=12, column=0, pady=(5,0), sticky="w")
        #Size: Xanh Đậu Đỏ
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=12, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry10_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[12][0])
        self.entry10_1.grid(row=12, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=12, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry10_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[12][1])
        self.entry10_2.grid(row=12, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=12, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry10_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[12][2])
        self.entry10_3.grid(row=12, column=6, pady=(5,0), sticky="w")

        #---LABEL: FREEZE
        self.label_name = Label(self.myframe, text="FREEZE", bg="#FFE699", font=('Calibri(Body) 11 bold italic underline'))
        self.label_name.grid(row=13, column=0, pady=(10,0), sticky="w")
        
        # Label: Trà Xanh
        self.label_name = Label(self.myframe, text="Trà Xanh", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=14, column=0, pady=(10,0), sticky="w")
        # Size: Trà Xanh
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=14, column=1, pady=(10,0), sticky="w", padx=(100,0))
        self.entry11_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[13][0])
        self.entry11_1.grid(row=14, column=2, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=14, column=3, pady=(10,0), padx=(30,0), sticky="w")
        self.entry11_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[13][1])
        self.entry11_2.grid(row=14, column=4, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=14, column=5, pady=(10,0), padx=(30,0),sticky="w")
        self.entry11_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[13][2])
        self.entry11_3.grid(row=14, column=6, pady=(10,0), sticky="w")

        #Label: Sô-cô-la
        self.label_name = Label(self.myframe, text="Sô-cô-la", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=15, column=0, pady=(5,0), sticky="w")
        #Size: Sô-cô-la
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=15, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry12_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[14][0])
        self.entry12_1.grid(row=15, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=15, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry12_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[14][1])
        self.entry12_2.grid(row=15, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=15, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry12_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[14][2])
        self.entry12_3.grid(row=15, column=6, pady=(5,0), sticky="w")

        #Label: Cookies & Cream
        self.label_name = Label(self.myframe, text="Cookies & Cream", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=16, column=0, pady=(5,0), sticky="w")
        #Size: Cookies & Cream
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=16, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry13_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[15][0])
        self.entry13_1.grid(row=16, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=16, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry13_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[15][1])
        self.entry13_2.grid(row=16, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=16, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry13_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[15][2])
        self.entry13_3.grid(row=16, column=6, pady=(5,0), sticky="w")

        #Label: Caramel Phin
        self.label_name = Label(self.myframe, text="Xanh Đậu Đỏ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=17, column=0, pady=(5,0), sticky="w")
        #Size: Caramel Phin
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=17, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry14_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[16][0])
        self.entry14_1.grid(row=17, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=17, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry14_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[16][1])
        self.entry14_2.grid(row=17, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=17, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry14_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[16][2])
        self.entry14_3.grid(row=17, column=6, pady=(5,0), sticky="w")

        #Label: Classic Phin
        self.label_name = Label(self.myframe, text="Classic Phin", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=19, column=0, pady=(5,0), sticky="w")
        #Size: Classic Phin
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=19, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry15_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[17][0])
        self.entry15_1.grid(row=19, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=19, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry15_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[17][1])
        self.entry15_2.grid(row=19, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=19, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry15_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[17][2])
        self.entry15_3.grid(row=19, column=6, pady=(5,0), sticky="w")

        #---LABEL: THỨC UỐNG KHÁC
        self.label_name = Label(self.myframe, text="THỨC UỐNG KHÁC", bg="#FFE699", font=('Calibri(Body) 11 bold italic underline'))
        self.label_name.grid(row=20, column=0, pady=(10,0), sticky="w")
        
        # Label: Chanh Đá Xay
        self.label_name = Label(self.myframe, text="Chanh Đá Xay", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=21, column=0, pady=(10,0), sticky="w")
        # Size: Chanh Đá Xay
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=21, column=1, pady=(10,0), sticky="w", padx=(100,0))
        self.entry16_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[18][0])
        self.entry16_1.grid(row=21, column=2, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=21, column=3, pady=(10,0), padx=(30,0), sticky="w")
        self.entry16_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[18][1])
        self.entry16_2.grid(row=21, column=4, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=21, column=5, pady=(10,0), padx=(30,0),sticky="w")
        self.entry16_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[18][2])
        self.entry16_3.grid(row=21, column=6, pady=(10,0), sticky="w")

        #Label: Chanh Dây Đá
        self.label_name = Label(self.myframe, text="Chanh Dây Đá", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=22, column=0, pady=(5,0), sticky="w")
        #Size: Chanh Dây Đá
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=22, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry17_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[19][0])
        self.entry17_1.grid(row=22, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=22, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry17_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[19][1])
        self.entry17_2.grid(row=22, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=22, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry17_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[19][2])
        self.entry17_3.grid(row=22, column=6, pady=(5,0), sticky="w")

        #Label: Tắc Đá Viên
        self.label_name = Label(self.myframe, text="Tắc Đá Viên", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=23, column=0, pady=(5,0), sticky="w")
        #Size: Tắc Đá Viên
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=23, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry18_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[20][0])
        self.entry18_1.grid(row=23, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=23, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry18_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[20][1])
        self.entry18_2.grid(row=23, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=23, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry18_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[20][2])
        self.entry18_3.grid(row=23, column=6, pady=(5,0), sticky="w")

        #Label: Sô-cô-la
        self.label_name = Label(self.myframe, text="Sô-cô-la", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=24, column=0, pady=(5,0), sticky="w")
        #Size: Sô-cô-la
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=24, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry19_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[21][0])
        self.entry19_1.grid(row=24, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=24, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry19_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[21][1])
        self.entry19_2.grid(row=24, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=24, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry19_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[21][2])
        self.entry19_3.grid(row=24, column=6, pady=(5,0), sticky="w")

        #Label: Sữa Chua Đá
        self.label_name = Label(self.myframe, text="Sữa Chua Đá", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=25, column=0, pady=(5,0), sticky="w")
        #Size: Sữa Chua Đá
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=25, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry20_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[22][0])
        self.entry20_1.grid(row=25, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=25, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry20_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[22][1])
        self.entry20_2.grid(row=25, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=25, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry20_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.var[22][2])
        self.entry20_3.grid(row=25, column=6, pady=(5,0), sticky="w")

        #---LABEL: THÔNG TIN THANH TOÁN
        self.label_name = Label(self.myframe, text="THÔNG TIN THANH TOÁN", bg="#FFE699", font=('Calibri(Body) 11 bold italic underline'))
        self.label_name.grid(row=26, column=0, pady=(10,0), sticky="w")
        
        # Label: Họ và tên
        self.label_name = Label(self.myframe, text="Họ tên: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=27, column=0, pady=(10,0), sticky="w")
        # Entry: Họ và tên
        self.entry_name = ttk.Entry(self.myframe, width=30, font=('Calibri(Body) 12'), textvariable=self.var[0])
        self.entry_name.grid(row=27, column=0, padx=20, pady=(10,0), columnspan=2)

        # Label: Số điện thoại
        self.label_name = Label(self.myframe, text="SĐT: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=28, column=0, pady=(10,0), sticky="w")
        # Entry: Số điện thoại
        self.entry_phone = ttk.Entry(self.myframe, width=30, font=('Calibri(Body) 12'), textvariable=self.var[1])
        self.entry_phone.grid(row=28, column=0, padx=20, pady=(10,0), columnspan=2)

        # Label: Email
        self.label_name = Label(self.myframe, text="Email: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=29, column=0, pady=(10,10), sticky="w")
        # Entry: Email
        self.entry_email = ttk.Entry(self.myframe, width=30, font=('Calibri(Body) 12'), textvariable=self.var[2])
        self.entry_email.grid(row=29, column=0, padx=20, pady=(10,10), columnspan=2)



def date():
    date_res = '' 
    today = datetime.datetime.today()
    date_res += str(today.day)
    month = str(today.month)
    if (int(month) < 10):
        month = '0'+str(today.month)
    date_res += month
    year = str(today.year)
    date_res += year[2:]
    return date_res

record_glb = 0
def loadID():
    connect = sqlite3.connect('data.db')
    cursor = connect.cursor()
    global record_glb
    try:
        cursor.execute("SELECT *, oid FROM addresses")
        records = cursor.fetchall()
        for record in records:
            record_glb = record[65]
    except:
        print("No data initialized")

    connect.commit()
    return record_glb

def indexID(i):
    if (i < 10):
        return '000' + str(i)
    elif (i < 100):
        return '00' + str(i)
    elif (i < 1000):
        return '0' + str(i)
    else:
        return str(i)

def total_update(s1, s2, s3):
    return int(s1)*30+int(s2)*40+int(s3)*50

class buttonFrame(): 
    def __init__(self, root, topframe): 
        self.root = root
        self.topframe = topframe

    def showButton(self):
        self.date = StringVar()
        self.id = StringVar()

        self.wrapper2 = LabelFrame(self.root, bd=5, bg="#FFE699")
        self.wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)

        #Label: Hôm nay
        self.label_name = Label(self.wrapper2, text="Hôm nay: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=0, column=0, pady=(10,0), padx=(10,0), sticky="w")
        #Entry: Hôm nay
        today = datetime.datetime.today()
        self.entry_date = ttk.Entry(self.wrapper2, width=16, font=('Calibri(Body) 12 italic'))
        self.entry_date.insert(0, f"{today:%a, %b %d, %Y}")
        self.entry_date.grid(row=0, column=1, pady=(10,0))

        #Button: Xem tất cả hóa đơn
        self.btn_search = Button(self.wrapper2, text="Xem tất cả hóa đơn", bg="#FF6600", fg="#000000", font=('Calibri(Body) 11 bold'), bd=5, highlightcolor="#000000", width=24, height=4, command=self.query)
        self.btn_search.grid(row=1, column=0, rowspan=2,columnspan=2, pady=(10,0), padx=(10,0), sticky="w")

        #Label: Nhập ID
        self.label_name = Label(self.wrapper2, text="Nhập ID: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=0, column=3, pady=(10,0), padx=(130,0), sticky="w")
        #Entry: Nhập ID
        self.entry_id = ttk.Entry(self.wrapper2, width=18, font=('Calibri(Body) 12'), textvariable=self.id)
        self.entry_id.grid(row=0, column=4, pady=(10,0))

        #Button: Xem hóa đơn
        self.btn_search = Button(self.wrapper2, text="Xem hóa đơn", bg="#FF6600", fg="#000000", font=('Calibri(Body) 11 bold'), bd=5, highlightcolor="#000000", width=26, command=lambda: self.edit(self.id.get()))
        self.btn_search.grid(row=1, column=3, columnspan=2, pady=(10,0), padx=(130,0), sticky="w")

        #Button: Xóa
        self.btn_search = Button(self.wrapper2, text="Xóa", bg="#FF6600", fg="#000000", font=('Calibri(Body) 11 bold'), bd=5, highlightcolor="#000000", width=7, command=lambda: self.delete(self.id.get()))
        self.btn_search.grid(row=2, column=3, pady=(10,0), padx=(130,0), sticky="w")

        #Button: Chỉnh sửa
        self.btn_search = Button(self.wrapper2, text="Chỉnh sửa", bg="#FF6600", fg="#000000", font=('Calibri(Body) 11 bold'), bd=5, highlightcolor="#000000", width=16, command=lambda: self.edit(self.id.get()))
        self.btn_search.grid(row=2, column=4, columnspan=2, pady=(10,0), padx=(10,0), sticky="w")

        #Label: ID
        self.label_name = Label(self.wrapper2, text="ID: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=0, column=5, pady=(10,0), padx=(130,0), sticky="w")
        #Entry: ID - DISABLED
        self.entry_id_current = ttk.Entry(self.wrapper2, width=18 ,font=('Calibri(Body) 12 bold'))
        self.entry_id_current.insert(0, "HT" + date() + "AN" + indexID(loadID() + 1))
        self.entry_id_current.grid(row=0, column=6, pady=(10,0))

        #Button: Thêm hóa đơn
        self.btn_search = Button(self.wrapper2, text="Thêm", bg="#FF6600", fg="#000000", font=('Calibri(Body) 11 bold'), bd=5, highlightcolor="#000000", width=20, height=4, command=self.submit)
        self.btn_search.grid(row=1, column=5, rowspan=2, columnspan=2, pady=(10,0), padx=(130,0), sticky="w")

    def submit(self):
        self.connect = sqlite3.connect('data.db') # Make connection to database
        self.cursor = connect.cursor()

        # Calculate the total cost of one bill
        for i in range(3,23):
            self.topframe.var[23] += self.topframe.var[i][0].get()*30 + self.topframe.var[i][1].get()*40 + self.topframe.var[i][2].get()*50
    

        # Insert into table
        self.cursor.execute (""" INSERT INTO addresses VALUES (
            :name, :phone, :email,
            :phinSuaDa1, :phinSuaDa2, :phinSuaDa3 , 
            :phinDenDa1, :phinDenDa2, :phinDenDa3 ,
            :bacXiuDa1, :bacXiuDa2, :bacXiuDa3 ,
            :espresso1, :espresso2, :espresso3 ,
            :cappiccino1, :cappiccino2 , :cappiccino3 ,
            :mocha1, :mocha2, :mocha3 ,
            :traSenVang1, :traSenVang2, :traSenVang3 , 
            :traThachDao1, :traThachDao2, :traThachDao3 , 
            :traThachVai1, :traThachVai2, :traThachVai3,
            :xanhDauDo1, :xanhDauDo2 , :xanhDauDo3 , 
            :freezeTraXanh1, :freezeTraXanh2 , :freezeTraXanh3 , 
            :freezeSocola1, :freezeSocola2 , :freezeSocola3 , 
            :freezeCookies1, :freezeCookies2 , :freezeCookies3 ,
            :freezeXanhDauDo1, :freezeXanhDauDo2 , :freezeXanhDauDo3 , 
            :freezeClassicPhin1, :freezeClassicPhin2, :freezeClassicPhin3,
            :chanhDaXay1, :chanhDaXay2, :chanhDaXay3,
            :chanhDayDa1, :chanhDayDa2, :chanhDayDa3,
            :tacDaVien1, :tacDaVien2, :tacDaVien3,
            :socola1, :socola2, :socola3, 
            :suaChuaDa1, :suaChuaDa2, :suaChuaDa3, 
            :totalCost, :ID
            )""",
                {
                    'name': self.topframe.var[0].get(), 'phone': self.topframe.var[1].get(), 'email': self.topframe.var[2].get(),
                    'phinSuaDa1': self.topframe.var[3][0].get(), 'phinSuaDa2': self.topframe.var[3][1].get(), 'phinSuaDa3': self.topframe.var[3][2].get(), 
                    'phinDenDa1': self.topframe.var[4][0].get(), 'phinDenDa2': self.topframe.var[4][1].get(), 'phinDenDa3': self.topframe.var[4][2].get(),
                    'bacXiuDa1': self.topframe.var[5][0].get(), 'bacXiuDa2': self.topframe.var[5][1].get(), 'bacXiuDa3': self.topframe.var[5][2].get(),
                    'espresso1': self.topframe.var[6][0].get(), 'espresso2': self.topframe.var[6][1].get(), 'espresso3': self.topframe.var[6][2].get(),
                    'cappiccino1': self.topframe.var[7][0].get(), 'cappiccino2': self.topframe.var[7][1].get(), 'cappiccino3': self.topframe.var[7][2].get(),
                    'mocha1': self.topframe.var[8][0].get(), 'mocha2': self.topframe.var[8][1].get(), 'mocha3': self.topframe.var[8][2].get(),
                    'traSenVang1': self.topframe.var[9][0].get(), 'traSenVang2': self.topframe.var[9][1].get(), 'traSenVang3': self.topframe.var[9][2].get(), 
                    'traThachDao1': self.topframe.var[10][0].get(), 'traThachDao2': self.topframe.var[10][1].get(), 'traThachDao3': self.topframe.var[10][2].get(), 
                    'traThachVai1': self.topframe.var[11][0].get(), 'traThachVai2': self.topframe.var[11][1].get(), 'traThachVai3': self.topframe.var[11][2].get(),
                    'xanhDauDo1': self.topframe.var[12][0].get(), 'xanhDauDo2': self.topframe.var[12][1].get(), 'xanhDauDo3': self.topframe.var[12][2].get(), 
                    'freezeTraXanh1': self.topframe.var[13][0].get(), 'freezeTraXanh2': self.topframe.var[13][1].get(), 'freezeTraXanh3': self.topframe.var[13][2].get(), 
                    'freezeSocola1': self.topframe.var[14][0].get(), 'freezeSocola2': self.topframe.var[14][1].get(), 'freezeSocola3': self.topframe.var[14][2].get(), 
                    'freezeCookies1': self.topframe.var[15][0].get(), 'freezeCookies2': self.topframe.var[15][1].get(), 'freezeCookies3': self.topframe.var[15][2].get(),
                    'freezeXanhDauDo1': self.topframe.var[16][0].get(), 'freezeXanhDauDo2': self.topframe.var[16][1].get(), 'freezeXanhDauDo3': self.topframe.var[16][2].get(), 
                    'freezeClassicPhin1': self.topframe.var[17][0].get(), 'freezeClassicPhin2': self.topframe.var[17][1].get(), 'freezeClassicPhin3': self.topframe.var[17][2].get(),
                    'chanhDaXay1': self.topframe.var[18][0].get(), 'chanhDaXay2': self.topframe.var[18][1].get(), 'chanhDaXay3': self.topframe.var[18][2].get(),
                    'chanhDayDa1': self.topframe.var[19][0].get(), 'chanhDayDa2': self.topframe.var[19][1].get(), 'chanhDayDa3': self.topframe.var[19][2].get(),
                    'tacDaVien1': self.topframe.var[20][0].get(), 'tacDaVien2': self.topframe.var[20][1].get(), 'tacDaVien3': self.topframe.var[20][2].get(),
                    'socola1': self.topframe.var[21][0].get(), 'socola2': self.topframe.var[21][1].get(), 'socola3': self.topframe.var[21][2].get(), 
                    'suaChuaDa1': self.topframe.var[22][0].get(), 'suaChuaDa2': self.topframe.var[22][1].get(), 'suaChuaDa3': self.topframe.var[22][2].get(),
                    'totalCost': self.topframe.var[23], 'ID': self.entry_id_current.get()
                })

        connect.commit()

        # Update ID entry
        self.entry_id_current.delete(0, END)
        self.entry_id_current.insert(0, "HT" + date() + "AN" + indexID(loadID() + 1))
        # Clear the text boxes
        self.topframe.entry1_1.delete(0, END)
        self.topframe.entry1_1.insert(0, 0)
        self.topframe.entry1_2.delete(0, END)
        self.topframe.entry1_2.insert(0, 0)
        self.topframe.entry1_3.delete(0, END)
        self.topframe.entry1_3.insert(0, 0)

        self.topframe.entry2_1.delete(0, END)
        self.topframe.entry2_1.insert(0, 0)
        self.topframe.entry2_2.delete(0, END)
        self.topframe.entry2_2.insert(0, 0)
        self.topframe.entry2_3.delete(0, END)
        self.topframe.entry2_3.insert(0, 0)

        self.topframe.entry3_1.delete(0, END)
        self.topframe.entry3_1.insert(0, 0)
        self.topframe.entry3_2.delete(0, END)
        self.topframe.entry3_2.insert(0, 0)
        self.topframe.entry3_3.delete(0, END)
        self.topframe.entry3_3.insert(0, 0)

        self.topframe.entry4_1.delete(0, END)
        self.topframe.entry4_1.insert(0, 0)
        self.topframe.entry4_2.delete(0, END)
        self.topframe.entry4_2.insert(0, 0)
        self.topframe.entry4_3.delete(0, END)
        self.topframe.entry4_3.insert(0, 0)

        self.topframe.entry5_1.delete(0, END)
        self.topframe.entry5_1.insert(0, 0)
        self.topframe.entry5_2.delete(0, END)
        self.topframe.entry5_2.insert(0, 0)
        self.topframe.entry5_3.delete(0, END)
        self.topframe.entry5_3.insert(0, 0)

        self.topframe.entry6_1.delete(0, END)
        self.topframe.entry6_1.insert(0, 0)
        self.topframe.entry6_2.delete(0, END)
        self.topframe.entry6_2.insert(0, 0)
        self.topframe.entry6_3.delete(0, END)
        self.topframe.entry6_3.insert(0, 0)

        self.topframe.entry7_1.delete(0, END)
        self.topframe.entry7_1.insert(0, 0)
        self.topframe.entry7_2.delete(0, END)
        self.topframe.entry7_2.insert(0, 0)
        self.topframe.entry7_3.delete(0, END)
        self.topframe.entry7_3.insert(0, 0)

        self.topframe.entry8_1.delete(0, END)
        self.topframe.entry8_1.insert(0, 0)
        self.topframe.entry8_2.delete(0, END)
        self.topframe.entry8_2.insert(0, 0)
        self.topframe.entry8_3.delete(0, END)
        self.topframe.entry8_3.insert(0, 0)

        self.topframe.entry9_1.delete(0, END)
        self.topframe.entry9_1.insert(0, 0)
        self.topframe.entry9_2.delete(0, END)
        self.topframe.entry9_2.insert(0, 0)
        self.topframe.entry9_3.delete(0, END)
        self.topframe.entry9_3.insert(0, 0)

        self.topframe.entry10_1.delete(0, END)
        self.topframe.entry10_1.insert(0, 0)
        self.topframe.entry10_2.delete(0, END)
        self.topframe.entry10_2.insert(0, 0)
        self.topframe.entry10_3.delete(0, END)
        self.topframe.entry10_3.insert(0, 0)

        self.topframe.entry11_1.delete(0, END)
        self.topframe.entry11_1.insert(0, 0)
        self.topframe.entry11_2.delete(0, END)
        self.topframe.entry11_2.insert(0, 0)
        self.topframe.entry11_3.delete(0, END)
        self.topframe.entry11_3.insert(0, 0)

        self.topframe.entry12_1.delete(0, END)
        self.topframe.entry12_1.insert(0, 0)
        self.topframe.entry12_2.delete(0, END)
        self.topframe.entry12_2.insert(0, 0)
        self.topframe.entry12_3.delete(0, END)
        self.topframe.entry12_3.insert(0, 0)

        self.topframe.entry13_1.delete(0, END)
        self.topframe.entry13_1.insert(0, 0)
        self.topframe.entry13_2.delete(0, END)
        self.topframe.entry13_2.insert(0, 0)
        self.topframe.entry13_3.delete(0, END)
        self.topframe.entry13_3.insert(0, 0)

        self.topframe.entry14_1.delete(0, END)
        self.topframe.entry14_1.insert(0, 0)
        self.topframe.entry14_2.delete(0, END)
        self.topframe.entry14_2.insert(0, 0)
        self.topframe.entry14_3.delete(0, END)
        self.topframe.entry14_3.insert(0, 0)

        self.topframe.entry15_1.delete(0, END)
        self.topframe.entry15_1.insert(0, 0)
        self.topframe.entry15_2.delete(0, END)
        self.topframe.entry15_2.insert(0, 0)
        self.topframe.entry15_3.delete(0, END)
        self.topframe.entry15_3.insert(0, 0)

        self.topframe.entry16_1.delete(0, END)
        self.topframe.entry16_1.insert(0, 0)
        self.topframe.entry16_2.delete(0, END)
        self.topframe.entry16_2.insert(0, 0)
        self.topframe.entry16_3.delete(0, END)
        self.topframe.entry16_3.insert(0, 0)

        self.topframe.entry17_1.delete(0, END)
        self.topframe.entry17_1.insert(0, 0)
        self.topframe.entry17_2.delete(0, END)
        self.topframe.entry17_2.insert(0, 0)
        self.topframe.entry17_3.delete(0, END)
        self.topframe.entry17_3.insert(0, 0)

        self.topframe.entry18_1.delete(0, END)
        self.topframe.entry18_1.insert(0, 0)
        self.topframe.entry18_2.delete(0, END)
        self.topframe.entry18_2.insert(0, 0)
        self.topframe.entry18_3.delete(0, END)
        self.topframe.entry18_3.insert(0, 0)

        self.topframe.entry19_1.delete(0, END)
        self.topframe.entry19_1.insert(0, 0)
        self.topframe.entry19_2.delete(0, END)
        self.topframe.entry19_2.insert(0, 0)
        self.topframe.entry19_3.delete(0, END)
        self.topframe.entry19_3.insert(0, 0)

        self.topframe.entry20_1.delete(0, END)
        self.topframe.entry20_1.insert(0, 0)
        self.topframe.entry20_2.delete(0, END)
        self.topframe.entry20_2.insert(0, 0)
        self.topframe.entry20_3.delete(0, END)
        self.topframe.entry20_3.insert(0, 0)

        self.topframe.entry_name.delete(0, END)
        self.topframe.entry_name.insert(0, '')
        self.topframe.entry_phone.delete(0, END)
        self.topframe.entry_phone.insert(0, '')
        self.topframe.entry_email.delete(0, END)
        self.topframe.entry_email.insert(0, '')

        self.edit("HT" + date() + "AN" + indexID(loadID()))

    def query(self):
        global viewer
        viewer = Tk() 
        viewer.title('Danh sách hóa đơn')
        viewer.iconbitmap('managerlogo.ico')
        viewer.geometry("500x600+50+50")
        viewer.resizable(FALSE, FALSE)
        
        # Connect to database
        connect = sqlite3.connect('data.db')
        # Create a cursor
        cursor = connect.cursor()
        # Query the database
        cursor.execute("SELECT *, oid FROM addresses")
        records = cursor.fetchall()


        # Create Treeview Frame
        tree_frame = Frame(viewer)
        tree_frame.pack(side="left", padx=10, pady=10)
      
        # Create Treeview
        my_tree = ttk.Treeview(tree_frame, selectmode="extended", height=400)
        # Pack to the screen
        my_tree.pack(side="left", fill="both")

        # Treeview Scrollbar
        tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=my_tree.yview)
        tree_scroll.pack(side=RIGHT, fill="y")
        my_tree.configure(yscrollcommand=tree_scroll.set)

        # Define Our Columns
        my_tree['columns'] = ("ID", "Khách hàng", "SĐT", "Tổng tiền")
        # Formate Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("ID", anchor=CENTER, width=120)
        my_tree.column("Khách hàng", anchor=W, width=140)
        my_tree.column("SĐT", anchor=CENTER, width=100)
        my_tree.column("Tổng tiền", anchor=W, width=100)

        # Create Headings 
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("ID", text="ID", anchor=CENTER)
        my_tree.heading("Khách hàng", text="Khách hàng", anchor=W)
        my_tree.heading("SĐT", text="SĐT", anchor=CENTER)
        my_tree.heading("Tổng tiền", text="Tổng tiền", anchor=W)

        # Create striped row tags
        my_tree.tag_configure('oddrow', background="#FFFFFF")
        my_tree.tag_configure('evenrow', background="#FFE699")

        global count
        count = 0
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text="", values=(record[64], record[0], record[1], record[63]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text="", values=(record[64], record[0], record[1], record[63]), tags=('oddrow',))

            count += 1
        
        # Commit changes
        connect.commit()

    def edit(self, id): 
        global editor
        editor = Tk() 
        editor.title('Chỉnh sửa hóa đơn')
        editor.iconbitmap('managerlogo.ico')
        editor.geometry("1000x500")
        editor.resizable(FALSE, FALSE)
        
        
        # Create a database or connection to one (in a fuction)
        connect = sqlite3.connect('data.db')
        
        # Create cursor (in a fuction)
        cursor = connect.cursor()
        
        # Convert the ID into index number in database
        record_id = str(int(id[10:])) #HT290822AN0001
        
        # Query the database
        cursor.execute("SELECT * FROM addresses WHERE oid = " + record_id)
        records = cursor.fetchall()

        # Create global variables for text box names
        self.wrapper3 = LabelFrame(editor, bd=5, bg="#FFE699")
        self.wrapper3.pack(fill="both", expand="yes", padx=10, pady=5)
        self.mycanvas1 = Canvas(self.wrapper3, width=900, height=400, highlightthickness=0, bg="#FFE699")
        self.mycanvas1.pack(side=LEFT, fill="y", padx=10)

        yscrollbar = ttk.Scrollbar(self.wrapper3, orient="vertical", command=self.mycanvas1.yview)
        yscrollbar.pack(side=RIGHT, fill="y")
        self.mycanvas1.configure(yscrollcommand=yscrollbar.set)
        self.mycanvas1.bind('<Configure>', lambda e: self.mycanvas1.configure(scrollregion = self.mycanvas1.bbox('all')))
        self.myframe1 = Frame(self.mycanvas1, bg="#FFE699")
        self.mycanvas1.create_window((0,0), window=self.myframe1, anchor="nw")

        
        #---LABEL: CÀ PHÊ PHA PHIN
        self.label_name = Label(self.myframe1, text="CÀ PHÊ PHA PHIN", bg="#FFE699", font=('Calibri(Body) 11 bold italic underline'))
        self.label_name.grid(row=0, column=0, pady=(10,0), sticky="w")
        
        # Label: Phin Sữa Đá
        self.label_name = Label(self.myframe1, text="Phin Sữa Đá", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=1, column=0, pady=(10,0), sticky="w")
        # Size: Phin Sữa Đá
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=1, column=1, pady=(10,0), sticky="w", padx=(100,0))
        self.entry1_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry1_1.grid(row=1, column=2, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=1, column=3, pady=(10,0), padx=(30,0), sticky="w")
        self.entry1_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry1_2.grid(row=1, column=4, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=1, column=5, pady=(10,0), padx=(30,0),sticky="w")
        self.entry1_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry1_3.grid(row=1, column=6, pady=(10,0), sticky="w")

        #Label: Phin Đen Đá
        self.label_name = Label(self.myframe1, text="Phin Đen Đá", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=2, column=0, pady=(5,0), sticky="w")
        #Size: Phin Đen Đá
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=2, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry2_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry2_1.grid(row=2, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=2, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry2_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry2_2.grid(row=2, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=2, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry2_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry2_3.grid(row=2, column=6, pady=(5,0), sticky="w")

        #Label: Bạc Xĩu Đá
        self.label_name = Label(self.myframe1, text="Bạc Xĩu Đá", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=3, column=0, pady=(5,0), sticky="w")
        #Size: Bạc Xĩu Đá 
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=3, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry3_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry3_1.grid(row=3, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=3, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry3_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry3_2.grid(row=3, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=3, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry3_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry3_3.grid(row=3, column=6, pady=(5,0), sticky="w")

        #---LABEL: CÀ PHÊ ESPRESSO
        self.label_name = Label(self.myframe1, text="CÀ PHÊ ESPRESSO", bg="#FFE699", font=('Calibri(Body) 11 bold italic underline'))
        self.label_name.grid(row=4, column=0, pady=(10,0), sticky="w")
        
        # Label: Espresso/Americano
        self.label_name = Label(self.myframe1, text="Espresso/Americano", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=5, column=0, pady=(10,0), sticky="w")
        # Size: Espresso/Americano
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=5, column=1, pady=(10,0), sticky="w", padx=(100,0))
        self.entry4_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry4_1.grid(row=5, column=2, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=5, column=3, pady=(10,0), padx=(30,0), sticky="w")
        self.entry4_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry4_2.grid(row=5, column=4, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=5, column=5, pady=(10,0), padx=(30,0),sticky="w")
        self.entry4_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry4_3.grid(row=5, column=6, pady=(10,0), sticky="w")

        #Label: Cappuccino/Latte
        self.label_name = Label(self.myframe1, text="Cappuccino/Latte", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=6, column=0, pady=(5,0), sticky="w")
        #Size: Cappuccino/Latte
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=6, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry5_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry5_1.grid(row=6, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=6, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry5_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry5_2.grid(row=6, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=6, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry5_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry5_3.grid(row=6, column=6, pady=(5,0), sticky="w")

        #Label: Mocha/Macchiato
        self.label_name = Label(self.myframe1, text="Mocha/Macchiato", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=7, column=0, pady=(5,0), sticky="w")
        #Size: Mocha/Macchiato
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=7, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry6_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry6_1.grid(row=7, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=7, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry6_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry6_2.grid(row=7, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=7, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry6_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry6_3.grid(row=7, column=6, pady=(5,0), sticky="w")

        #---LABEL: TRÀ
        self.label_name = Label(self.myframe1, text="TRÀ", bg="#FFE699", font=('Calibri(Body) 11 bold italic underline'))
        self.label_name.grid(row=8, column=0, pady=(10,0), sticky="w")
        
        # Label: Sen Vàng
        self.label_name = Label(self.myframe1, text="Sen Vàng", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=9, column=0, pady=(10,0), sticky="w")
        # Size: Sen Vàng
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=9, column=1, pady=(10,0), sticky="w", padx=(100,0))
        self.entry7_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry7_1.grid(row=9, column=2, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=9, column=3, pady=(10,0), padx=(30,0), sticky="w")
        self.entry7_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry7_2.grid(row=9, column=4, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=9, column=5, pady=(10,0), padx=(30,0),sticky="w")
        self.entry7_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry7_3.grid(row=9, column=6, pady=(10,0), sticky="w")

        #Label: Thạch Đào
        self.label_name = Label(self.myframe1, text="Thạch Đào", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=10, column=0, pady=(5,0), sticky="w")
        #Size: Thạch Đào
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=10, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry8_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry8_1.grid(row=10, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=10, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry8_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry8_2.grid(row=10, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=10, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry8_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry8_3.grid(row=10, column=6, pady=(5,0), sticky="w")

        #Label: Thạch Vải
        self.label_name = Label(self.myframe1, text="Thạch Vải", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=11, column=0, pady=(5,0), sticky="w")
        #Size: Thạch Vải
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=11, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry9_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry9_1.grid(row=11, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=11, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry9_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry9_2.grid(row=11, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=11, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry9_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry9_3.grid(row=11, column=6, pady=(5,0), sticky="w")

        #Label: Xanh Đậu Đỏ
        self.label_name = Label(self.myframe1, text="Xanh Đậu Đỏ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=12, column=0, pady=(5,0), sticky="w")
        #Size: Xanh Đậu Đỏ
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=12, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry10_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry10_1.grid(row=12, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=12, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry10_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry10_2.grid(row=12, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=12, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry10_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry10_3.grid(row=12, column=6, pady=(5,0), sticky="w")

        #---LABEL: FREEZE
        self.label_name = Label(self.myframe1, text="FREEZE", bg="#FFE699", font=('Calibri(Body) 11 bold italic underline'))
        self.label_name.grid(row=13, column=0, pady=(10,0), sticky="w")
        
        # Label: Trà Xanh
        self.label_name = Label(self.myframe1, text="Trà Xanh", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=14, column=0, pady=(10,0), sticky="w")
        # Size: Trà Xanh
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=14, column=1, pady=(10,0), sticky="w", padx=(100,0))
        self.entry11_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry11_1.grid(row=14, column=2, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=14, column=3, pady=(10,0), padx=(30,0), sticky="w")
        self.entry11_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry11_2.grid(row=14, column=4, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=14, column=5, pady=(10,0), padx=(30,0),sticky="w")
        self.entry11_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry11_3.grid(row=14, column=6, pady=(10,0), sticky="w")

        #Label: Sô-cô-la
        self.label_name = Label(self.myframe1, text="Sô-cô-la", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=15, column=0, pady=(5,0), sticky="w")
        #Size: Sô-cô-la
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=15, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry12_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry12_1.grid(row=15, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=15, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry12_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry12_2.grid(row=15, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=15, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry12_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry12_3.grid(row=15, column=6, pady=(5,0), sticky="w")

        #Label: Cookies & Cream
        self.label_name = Label(self.myframe1, text="Cookies & Cream", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=16, column=0, pady=(5,0), sticky="w")
        #Size: Cookies & Cream
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=16, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry13_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry13_1.grid(row=16, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=16, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry13_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry13_2.grid(row=16, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=16, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry13_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry13_3.grid(row=16, column=6, pady=(5,0), sticky="w")

        #Label: Xanh Đậu Đỏ
        self.label_name = Label(self.myframe1, text="Xanh Đậu Đỏ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=17, column=0, pady=(5,0), sticky="w")
        #Size: Xanh Đậu Đỏ
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=17, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry14_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry14_1.grid(row=17, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=17, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry14_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry14_2.grid(row=17, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=17, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry14_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry14_3.grid(row=17, column=6, pady=(5,0), sticky="w")

        #Label: Classic Phin
        self.label_name = Label(self.myframe1, text="Classic Phin", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=19, column=0, pady=(5,0), sticky="w")
        #Size: Classic Phin
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=19, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry15_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry15_1.grid(row=19, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=19, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry15_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry15_2.grid(row=19, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=19, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry15_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry15_3.grid(row=19, column=6, pady=(5,0), sticky="w")

        #---LABEL: THỨC UỐNG KHÁC
        self.label_name = Label(self.myframe1, text="THỨC UỐNG KHÁC", bg="#FFE699", font=('Calibri(Body) 11 bold italic underline'))
        self.label_name.grid(row=20, column=0, pady=(10,0), sticky="w")
        
        # Label: Chanh Đá Xay
        self.label_name = Label(self.myframe1, text="Chanh Đá Xay", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=21, column=0, pady=(10,0), sticky="w")
        # Size: Chanh Đá Xay
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=21, column=1, pady=(10,0), sticky="w", padx=(100,0))
        self.entry16_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry16_1.grid(row=21, column=2, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=21, column=3, pady=(10,0), padx=(30,0), sticky="w")
        self.entry16_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry16_2.grid(row=21, column=4, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=21, column=5, pady=(10,0), padx=(30,0),sticky="w")
        self.entry16_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry16_3.grid(row=21, column=6, pady=(10,0), sticky="w")

        #Label: Chanh Dây Đá
        self.label_name = Label(self.myframe1, text="Chanh Dây Đá", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=22, column=0, pady=(5,0), sticky="w")
        #Size: Chanh Dây Đá
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=22, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry17_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry17_1.grid(row=22, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=22, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry17_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry17_2.grid(row=22, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=22, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry17_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry17_3.grid(row=22, column=6, pady=(5,0), sticky="w")

        #Label: Tắc Đá Viên
        self.label_name = Label(self.myframe1, text="Tắc Đá Viên", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=23, column=0, pady=(5,0), sticky="w")
        #Size: Tắc Đá Viên
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=23, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry18_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry18_1.grid(row=23, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=23, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry18_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry18_2.grid(row=23, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=23, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry18_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry18_3.grid(row=23, column=6, pady=(5,0), sticky="w")

        #Label: Sô-cô-la
        self.label_name = Label(self.myframe1, text="Sô-cô-la", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=24, column=0, pady=(5,0), sticky="w")
        #Size: Sô-cô-la
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=24, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry19_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry19_1.grid(row=24, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=24, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry19_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry19_2.grid(row=24, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=24, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry19_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry19_3.grid(row=24, column=6, pady=(5,0), sticky="w")

        #Label: Sữa Chua Đá
        self.label_name = Label(self.myframe1, text="Sữa Chua Đá", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=25, column=0, pady=(5,0), sticky="w")
        #Size: Sữa Chua Đá
        self.label_size = Label(self.myframe1, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=25, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry20_1 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry20_1.grid(row=25, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=25, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry20_2 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry20_2.grid(row=25, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe1, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=25, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry20_3 = ttk.Entry(self.myframe1, font=('Calibri(Body) 11'), width=3)
        self.entry20_3.grid(row=25, column=6, pady=(5,0), sticky="w")

        #---LABEL: THÔNG TIN KHÁCH HÀNG
        self.label_name = Label(self.myframe1, text="THÔNG TIN KHÁCH HÀNG", bg="#FFE699", font=('Calibri(Body) 11 bold italic underline'))
        self.label_name.grid(row=26, column=0, pady=(10,0), sticky="w")
        
        # Label: Họ và tên
        self.label_name = Label(self.myframe1, text="Họ tên: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=27, column=0, pady=(10,0), sticky="w")
        # Entry: Họ và tên
        self.entry_name = ttk.Entry(self.myframe1, width=30, font=('Calibri(Body) 12'))
        self.entry_name.grid(row=27, column=0, padx=20, pady=(10,0), columnspan=2)

        # Label: Số điện thoại
        self.label_name = Label(self.myframe1, text="SĐT: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=28, column=0, pady=(10,0), sticky="w")
        # Entry: Số điện thoại
        self.entry_phone = ttk.Entry(self.myframe1, width=30, font=('Calibri(Body) 12'))
        self.entry_phone.grid(row=28, column=0, padx=20, pady=(10,0), columnspan=2)

        # Label: Email
        self.label_name = Label(self.myframe1, text="Email: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=29, column=0, pady=(10,10), sticky="w")
        # Entry: Email
        self.entry_email = ttk.Entry(self.myframe1, width=30, font=('Calibri(Body) 12'))
        self.entry_email.grid(row=29, column=0, padx=20, pady=(10,10), columnspan=2)

        # Label: Tổng tiền
        self.label_name = Label(self.myframe1, text="Tổng tiền: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=30, column=0, pady=(10,10), sticky="w")
        # Entry: Tổng tiền
        self.entry_total = ttk.Entry(self.myframe1, width=30, font=('Calibri(Body) 12'))
        self.entry_total.grid(row=31, column=0, padx=20, pady=(10,10), columnspan=2)


        for record in records:
            self.entry1_1.insert(0, record[3])
            self.entry1_2.insert(0, record[4])
            self.entry1_3.insert(0, record[5])
            
            self.entry2_1.insert(0, record[6])
            self.entry2_2.insert(0, record[7])
            self.entry2_3.insert(0, record[8])
            
            self.entry3_1.insert(0, record[9])
            self.entry3_2.insert(0, record[10])
            self.entry3_3.insert(0, record[11])
            
            self.entry4_1.insert(0, record[12])
            self.entry4_2.insert(0, record[13])
            self.entry4_3.insert(0, record[14])
            
            self.entry5_1.insert(0, record[15])
            self.entry5_2.insert(0, record[16])
            self.entry5_3.insert(0, record[17])
            
            self.entry6_1.insert(0, record[18])
            self.entry6_2.insert(0, record[19])
            self.entry6_3.insert(0, record[20])
            
            self.entry7_1.insert(0, record[21])
            self.entry7_2.insert(0, record[22])
            self.entry7_3.insert(0, record[23])
            
            self.entry8_1.insert(0, record[24])
            self.entry8_2.insert(0, record[25])
            self.entry8_3.insert(0, record[26])
            
            self.entry9_1.insert(0, record[27])
            self.entry9_2.insert(0, record[28])
            self.entry9_3.insert(0, record[29])
            
            self.entry10_1.insert(0, record[30])
            self.entry10_2.insert(0, record[31])
            self.entry10_3.insert(0, record[32])
            
            self.entry11_1.insert(0, record[33])
            self.entry11_2.insert(0, record[34])
            self.entry11_3.insert(0, record[35])
            
            self.entry12_1.insert(0, record[36])
            self.entry12_2.insert(0, record[37])
            self.entry12_3.insert(0, record[38])
            
            self.entry13_1.insert(0, record[39])
            self.entry13_2.insert(0, record[40])
            self.entry13_3.insert(0, record[41])
            
            self.entry14_1.insert(0, record[42])
            self.entry14_2.insert(0, record[43])
            self.entry14_3.insert(0, record[44])
            
            self.entry15_1.insert(0, record[45])
            self.entry15_2.insert(0, record[46])
            self.entry15_3.insert(0, record[47])
            
            self.entry16_1.insert(0, record[48])
            self.entry16_2.insert(0, record[49])
            self.entry16_3.insert(0, record[50])
            
            self.entry17_1.insert(0, record[51])
            self.entry17_2.insert(0, record[52])
            self.entry17_3.insert(0, record[53])
            
            self.entry18_1.insert(0, record[54])
            self.entry18_2.insert(0, record[55])
            self.entry18_3.insert(0, record[56])
            
            self.entry19_1.insert(0, record[57])
            self.entry19_2.insert(0, record[58])
            self.entry19_3.insert(0, record[59])
            
            self.entry20_1.insert(0, record[60])
            self.entry20_2.insert(0, record[61])
            self.entry20_3.insert(0, record[62])
            
            self.entry_name.insert(0, record[0])
            self.entry_phone.insert(0, record[1])
            self.entry_email.insert(0, record[2])
            self.entry_total.insert(0, record[63])
            
        # Create the lower frame
        # self.wrapper4 = LabelFrame(editor, bd=5, bg="#FFE699")
        # self.wrapper4.pack(fill="both", expand="yes", padx=10, pady=10)

        # Button: Lưu thông tin
        self.btn_save = Button(editor, text="Lưu thông tin", bg="#FF6600", fg="#000000", font=('Calibri(Body) 11 bold'), bd=5, highlightcolor="#000000", width=26, command=lambda: self.update(id))
        self.btn_save.pack(fill="both", expand="yes", padx=10, pady=(5,10))

    def update(self, id):
        # Create a database or connection to one
        connect = sqlite3.connect('data.db')
        # Create cursor (in a fuction)
        cursor = connect.cursor()
        # Convert the ID into index number in database
        record_id = str(int(id[10:])) #HT290822NB0001
        # Update total cost 
        totalCost = total_update(self.entry1_1.get(), self.entry1_2.get(), self.entry1_3.get()) + total_update(self.entry2_1.get(), self.entry2_2.get(), self.entry2_3.get())+total_update(self.entry3_1.get(), self.entry3_2.get(), self.entry3_3.get())+total_update(self.entry4_1.get(), self.entry4_2.get(), self.entry4_3.get())+total_update(self.entry5_1.get(), self.entry5_2.get(), self.entry5_3.get())+total_update(self.entry6_1.get(), self.entry6_2.get(), self.entry6_3.get())+total_update(self.entry7_1.get(), self.entry7_2.get(), self.entry7_3.get())+total_update(self.entry8_1.get(), self.entry8_2.get(), self.entry8_3.get())+total_update(self.entry9_1.get(), self.entry9_2.get(), self.entry9_3.get())+total_update(self.entry10_1.get(), self.entry10_2.get(), self.entry10_3.get())+total_update(self.entry11_1.get(), self.entry11_2.get(), self.entry11_3.get())+total_update(self.entry12_1.get(), self.entry12_2.get(), self.entry12_3.get())+total_update(self.entry13_1.get(), self.entry13_2.get(), self.entry13_3.get())+total_update(self.entry14_1.get(), self.entry14_2.get(), self.entry14_3.get())+total_update(self.entry15_1.get(), self.entry15_2.get(), self.entry15_3.get())+total_update(self.entry16_1.get(), self.entry16_2.get(), self.entry16_3.get())+total_update(self.entry17_1.get(), self.entry17_2.get(), self.entry17_3.get())+total_update(self.entry18_1.get(), self.entry18_2.get(), self.entry18_3.get())+total_update(self.entry19_1.get(), self.entry19_2.get(), self.entry19_3.get())+total_update(self.entry20_1.get(), self.entry20_2.get(), self.entry20_3.get())

        cursor.execute("""UPDATE addresses SET
            name = :name, phone = :phone, email = :email,
            phinSuaDa1 = :phinSuaDa1, phinSuaDa2 = :phinSuaDa2, phinSuaDa3 = :phinSuaDa3, 
            phinDenDa1 = :phinDenDa1, phinDenDa2 = :phinDenDa2, phinDenDa3 = :phinDenDa3,
            bacXiuDa1 = :bacXiuDa1, bacXiuDa2 = :bacXiuDa2, bacXiuDa3 = :bacXiuDa3,
            espresso1 = :espresso1, espresso2 = :espresso2, espresso3 = :espresso3,
            cappiccino1 = :cappiccino1, cappiccino2 = :cappiccino2, cappiccino3 = :cappiccino3,
            mocha1 = :mocha1, mocha2 = :mocha2, mocha3 = :mocha3,
            traSenVang1 = :traSenVang1, traSenVang2 = :traSenVang2, traSenVang3 = :traSenVang3, 
            traThachDao1 = :traThachDao1, traThachDao2 = :traThachDao2, traThachDao3 = :traThachDao3, 
            traThachVai1 = :traThachVai1, traThachVai2 = :traThachVai2, traThachVai3 = :traThachVai3,
            xanhDauDo1 = :xanhDauDo1, xanhDauDo2 = :xanhDauDo2, xanhDauDo3 = :xanhDauDo3, 
            freezeTraXanh1 = :freezeTraXanh1, freezeTraXanh2 = :freezeTraXanh2, freezeTraXanh3 = :freezeTraXanh3, 
            freezeSocola1 = :freezeSocola1, freezeSocola2 = :freezeSocola2, freezeSocola3 = :freezeSocola3, 
            freezeCookies1 = :freezeCookies1, freezeCookies2 = :freezeCookies2, freezeCookies3 = :freezeCookies3,
            freezeXanhDauDo1 = :freezeXanhDauDo1, freezeXanhDauDo2 = :freezeXanhDauDo2, freezeXanhDauDo3 = :freezeXanhDauDo3, 
            freezeClassicPhin1 = :freezeClassicPhin1, freezeClassicPhin2 = :freezeClassicPhin2, freezeClassicPhin3 = :freezeClassicPhin3,
            chanhDaXay1 = :chanhDaXay1, chanhDaXay2 = :chanhDaXay2, chanhDaXay3 = :chanhDaXay3,
            chanhDayDa1 = :chanhDayDa1, chanhDayDa2 = :chanhDayDa2, chanhDayDa3 = :chanhDayDa3,
            tacDaVien1 = :tacDaVien1, tacDaVien2 = :tacDaVien2, tacDaVien3 = :tacDaVien3,
            socola1 = :socola1, socola2 = :socola2, socola3 = :socola3, 
            suaChuaDa1 = :suaChuaDa1, suaChuaDa2 = :suaChuaDa2, suaChuaDa3 = :suaChuaDa3,
            totalCost = :totalCost
            WHERE oid = :oid""",
            {
                'name': self.entry_name.get(), 'phone': self.entry_phone.get(), 'email': self.entry_email.get(),
                'phinSuaDa1': self.entry1_1.get(), 'phinSuaDa2': self.entry1_2.get(), 'phinSuaDa3': self.entry1_3.get(), 
                'phinDenDa1': self.entry2_1.get(), 'phinDenDa2': self.entry2_2.get(), 'phinDenDa3': self.entry2_3.get(),
                'bacXiuDa1': self.entry3_1.get(), 'bacXiuDa2': self.entry3_2.get(), 'bacXiuDa3': self.entry3_3.get(),
                'espresso1': self.entry4_1.get(), 'espresso2': self.entry4_2.get(), 'espresso3': self.entry4_3.get(),
                'cappiccino1': self.entry5_1.get(), 'cappiccino2': self.entry5_2.get(), 'cappiccino3': self.entry5_3.get(),
                'mocha1': self.entry6_1.get(), 'mocha2': self.entry6_2.get(), 'mocha3': self.entry6_3.get(),
                'traSenVang1': self.entry7_1.get(), 'traSenVang2': self.entry7_2.get(), 'traSenVang3': self.entry7_3.get(), 
                'traThachDao1': self.entry8_1.get(), 'traThachDao2': self.entry8_2.get(), 'traThachDao3': self.entry8_3.get(), 
                'traThachVai1': self.entry9_1.get(), 'traThachVai2': self.entry9_2.get(), 'traThachVai3': self.entry9_3.get(),
                'xanhDauDo1': self.entry10_1.get(), 'xanhDauDo2': self.entry10_2.get(), 'xanhDauDo3': self.entry10_3.get(), 
                'freezeTraXanh1': self.entry11_1.get(), 'freezeTraXanh2': self.entry11_2.get(), 'freezeTraXanh3': self.entry11_3.get(), 
                'freezeSocola1': self.entry12_1.get(), 'freezeSocola2': self.entry12_2.get(), 'freezeSocola3': self.entry12_3.get(), 
                'freezeCookies1': self.entry13_1.get(), 'freezeCookies2': self.entry13_2.get(), 'freezeCookies3': self.entry13_3.get(),
                'freezeXanhDauDo1': self.entry14_1.get(), 'freezeXanhDauDo2': self.entry14_2.get(), 'freezeXanhDauDo3': self.entry14_3.get(), 
                'freezeClassicPhin1': self.entry15_1.get(), 'freezeClassicPhin2': self.entry15_2.get(), 'freezeClassicPhin3': self.entry15_3.get(),
                'chanhDaXay1': self.entry16_1.get(), 'chanhDaXay2': self.entry16_2.get(), 'chanhDaXay3': self.entry16_3.get(),
                'chanhDayDa1': self.entry17_1.get(), 'chanhDayDa2': self.entry17_2.get(), 'chanhDayDa3': self.entry17_3.get(),
                'tacDaVien1': self.entry18_1.get(), 'tacDaVien2': self.entry18_2.get(), 'tacDaVien3': self.entry18_3.get(),
                'socola1': self.entry19_1.get(), 'socola2': self.entry19_2.get(), 'socola3': self.entry19_3.get(), 
                'suaChuaDa1': self.entry20_1.get(), 'suaChuaDa2': self.entry20_2.get(), 'suaChuaDa3': self.entry20_3.get(),
                'totalCost': totalCost,

                'oid': record_id
            }
        )

        # Commit changes
        connect.commit()
        # Close the editor window
        editor.destroy()

    def delete(self, id):
        # Create a connection
        connect = sqlite3.connect('data.db') 
        # Create cursor (in a fuction)
        cursor = connect.cursor()

        record_id = str(int(id[10:]))
        # Delete a record
        cursor.execute("DELETE from addresses WHERE oid=" + record_id) 

        # Commit changes
        connect.commit()


mode = 0
class Login(): 
    def  __init__(self):  
        self.login = Tk() # Create the root window
        self.login.config(bg="#FFF2CC")
        self.login.title("Coffee Selling Manager") # Create title of root window
        self.login.iconbitmap("managerlogo.ico")
        self.login.resizable(False, False)

        self.username = StringVar()
        self.password = StringVar()

        self.check = 0
        window_width = 1000
        window_height = 650

        # Get the screen dimension
        screen_width = self.login.winfo_screenwidth()
        screen_height = self.login.winfo_screenheight()
        # Find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        # Set the position of the window to the center of the screen
        self.login.geometry(f'{window_width}x{window_height}+{center_x}+{center_y-30}')

        # Create heading
        self.label_title = Label(self.login, text="HAI TUYEN'S COFFEE HOUSE", font= ('Roboto 30 bold'), bg="#FFFFFF", fg="#843C0C")
        self.label_title.grid(row=0, column=0, columnspan=2, pady=(30,50), ipadx=232)


        # Initialize login information
        self.credentials = {'User Name': ['haituyen', 'tekyq7'], 'Password': ['1234', '1234']}
        self.entryLst = []

        # Label: 
        self.label_username = Label(self.login, text="User Name:", bg="#FFF2CC", font=('Calibri(Body) 12'))
        self.label_username.grid(row=1, column=0, padx=(350,0), pady=5)
        self.ent_username = Entry(self.login, font=('Calibri(Body) 12'), textvariable=self.username)
        self.ent_username.grid(row=1, column=1, padx=(0,350), pady=5)

        self.label_password = Label(self.login, text="Password:", bg="#FFF2CC", font=('Calibri(Body) 12'))
        self.label_password.grid(row=2, column=0, padx=(350,0), pady=5)
        self.ent_password = Entry(self.login, font=('Calibri(Body) 12'), textvariable=self.password)
        self.ent_password.grid(row=2, column=1, padx=(0,350), pady=5)

        self.entryLst.append(self.username)
        self.entryLst.append(self.password)

        
        # Login button
        loginButton = Button(self.login, text="Đăng Nhập", bg="#FF6600", fg="#000000", font=('Calibri(Body) 11 bold'), bd=5, highlightcolor="#000000", command=self.validateLogin)
        loginButton.grid(row=3, column=0, columnspan=2, pady=15, ipadx=50)  

        # Add image
        my_img = ImageTk.PhotoImage(Image.open("E:\TEKY\Product_HP1_HP3_SNLTW\coffee5.png"))
        my_imgLabel = Label(self.login, image=my_img, highlightthickness=0, highlightcolor="#FFF2CC")
        my_imgLabel.grid(row=4, column=0, columnspan=2)
        self.login.mainloop()


    def validateLogin(self):
        user_entry = [entry.get() for entry in self.entryLst]
        
        for x in zip(*self.credentials.values()):
            if list(x) == user_entry:
                self.check = 1
                self.login.destroy()
                break

        if self.check == 0:
            self.popup()
            self.login.destroy()
                

    def popup(self):
        response = messagebox.showwarning("Cảnh báo", "Thông tin đăng nhập sai, chương trình sẽ kết thúc.") # String thứ 1: title của popup, string thứ 2: nội dung của popup
        #Label(root, text=response).pack()


def createDataBase(connect):
    cursor = connect.cursor()
    cursor.execute( """ CREATE TABLE addresses(
        name text, phone text, email text,
        phinSuaDa1 int, phinSuaDa2 int, phinSuaDa3 int, 
        phinDenDa1 int, phinDenDa2 int, phinDenDa3 int,
        bacXiuDa1 int, bacXiuDa2 int, bacXiuDa3 int,
        espresso1 int, espresso2 int, espresso3 int,
        cappiccino1 int, cappiccino2 int, cappiccino3 int,
        mocha1 int, mocha2 int, mocha3 int,
        traSenVang1 int, traSenVang2 int, traSenVang3 int, 
        traThachDao1 int, traThachDao2 int, traThachDao3 int, 
        traThachVai1 int, traThachVai2 int, traThachVai3 int,
        xanhDauDo1 int, xanhDauDo2 int, xanhDauDo3 int, 
        freezeTraXanh1 int, freezeTraXanh2 int, freezeTraXanh3 int, 
        freezeSocola1 int, freezeSocola2 int, freezeSocola3 int, 
        freezeCookies1 int, freezeCookies2 int, freezeCookies3 int,
        freezeXanhDauDo1 int, freezeXanhDauDo2 int, freezeXanhDauDo3 int, 
        freezeClassicPhin1 int, freezeClassicPhin2 int, freezeClassicPhin3 int,
        chanhDaXay1 int, chanhDaXay2 int, chanhDaXay3 int,
        chanhDayDa1 int, chanhDayDa2 int, chanhDayDa3 int,
        tacDaVien1 int, tacDaVien2 int, tacDaVien3 int,
        socola1 int, socola2 int, socola3 int, 
        suaChuaDa1 int, suaChuaDa2 int, suaChuaDa3 int,
        totalCost int, ID text
        )""") 
    

if __name__ == "__main__": 
    login = Login()
    if (login.check == 1):
        # Create a database or connection to one (in a fuction)
        connect = sqlite3.connect('data.db')
        # Create cursor (in a fuction)
        cursor = connect.cursor()

        #createDataBase(connect)

        a = Manager()
        topFrame = infoFrame(a.root)
        topFrame.show()
        lowFrame = buttonFrame(a.root, topFrame)
        lowFrame.showButton()

        #Commit changes in database 
        connect.commit()
        #Close database
        #connect.close()
        mainloop()

    
        
    
    
