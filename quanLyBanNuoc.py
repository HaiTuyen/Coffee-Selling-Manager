from tkinter import *
from tkinter import ttk
import sqlite3
from xml.dom.minidom import Identified



class Bill(): 
    def __init__(self, khachhang, phinSuaDa, phinDenDa, bacXiuDa, espresso, cappiccino, mocha, traSenVang, traThachDao, traThachVai, xanhDauDo, freezeTraXanh,
                freezeSocola, freezeCookies, freezeXanhDauDo, freezeClassicPhin, chanhDaXay, chanhDayDa, tacDaVien, socola, suaChuaDa):

                  self.name = khachhang[1]
                  self.phone = khachhang[2]
                  self.email = khachhang[3]
                  self.phinSuaDa = [phinSuaDa[0], phinSuaDa[1], phinSuaDa[2]]
                  self.phinDenDa = [phinDenDa[0], phinDenDa[1], phinDenDa[2]]
                  self.bacXiuDa = [bacXiuDa[0], bacXiuDa[1], bacXiuDa[2]]
                  self.espresso = [espresso[0], espresso[1], espresso[2]]
                  self.cappiccino = [cappiccino[0], cappiccino[1], cappiccino[2]]
                  self.mocha = [mocha[0], mocha[1], mocha[2]]
                  self.traSenVang = [traSenVang[0], traSenVang[1], traSenVang[2]]
                  self.traThachDao = [traThachDao[0], traThachDao[1], traThachDao[2]]
                  self.traThachVai = [traThachVai[0], traThachVai[1], traThachVai[2]]
                  self.xanhDauDo = [xanhDauDo[0], xanhDauDo[1], xanhDauDo[2]]
                  self.freezeTraXanh = [freezeTraXanh[0], freezeTraXanh[1], freezeTraXanh[2]]
                  self.freezeSocola = [freezeSocola[0], freezeSocola[1], freezeSocola[2]]
                  self.freezeCookies = [freezeCookies[0], freezeCookies[1], freezeCookies[2]]
                  self.freezeXanhDauDo = [freezeXanhDauDo[0], freezeXanhDauDo[1], freezeXanhDauDo[2]]
                  self.freezeClassicPhin = [freezeClassicPhin[0], freezeClassicPhin[1], freezeClassicPhin[2]]
                  self.chanhDaXay = [chanhDaXay[0], chanhDaXay[1], chanhDaXay[2]]
                  self.chanhDayDa = [chanhDayDa[0], chanhDayDa[1], chanhDayDa[2]]
                  self.tacDaVien = [tacDaVien[0], tacDaVien[1], tacDaVien[2]]
                  self.socola = [socola[0], socola[1], socola[2]]
                  self.suaChuaDa = [suaChuaDa[0], suaChuaDa[1], suaChuaDa[2]]

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

    
#     def topFrame(self):

#         self.khachhang = ['','','']
#         self.khachhang[0] = StringVar()
#         self.khachhang[1] = StringVar()
#         self.khachhang[2] = StringVar()

#         self.phinSuaDa = [0,0,0]
#         self.phinSuaDa[0] = IntVar()
#         self.phinSuaDa[1] = IntVar()
#         self.phinSuaDa[2] = IntVar()
        
#         self.phinDenDa = [0,0,0]
#         self.phinDenDa[0] = IntVar()
#         self.phinDenDa[1] = IntVar()
#         self.phinDenDa[2] = IntVar()

#         self.bacXiuDa = [0,0,0]
#         self.bacXiuDa[0] = IntVar()
#         self.bacXiuDa[1] = IntVar()
#         self.bacXiuDa[2] = IntVar()

#         self.espresso = [0,0,0]
#         self.espresso[0] = IntVar()
#         self.espresso[1] = IntVar()
#         self.espresso[2] = IntVar()

#         self.cappiccino = [0,0,0]
#         self.cappiccino[0] = IntVar()
#         self.cappiccino[1] = IntVar()
#         self.cappiccino[2] = IntVar()

#         self.mocha = [0,0,0]
#         self.mocha[0] = IntVar()
#         self.mocha[1] = IntVar()
#         self.mocha[2] = IntVar()

#         self.traSenVang = [0,0,0]
#         self.traSenVang[0] = IntVar()
#         self.traSenVang[1] = IntVar()
#         self.traSenVang[2] = IntVar()

#         self.traThachDao = [0,0,0]
#         self.traThachDao[0] = IntVar()
#         self.traThachDao[1] = IntVar()
#         self.traThachDao[2] = IntVar()

#         self.traThachVai = [0,0,0]
#         self.traThachVai[0] = IntVar()
#         self.traThachVai[1] = IntVar()
#         self.traThachVai[2] = IntVar()

#         self.xanhDauDo = [0,0,0]
#         self.xanhDauDo[0] = IntVar()
#         self.xanhDauDo[1] = IntVar()
#         self.xanhDauDo[2] = IntVar()

#         self.freezeTraXanh = [0,0,0]
#         self.freezeTraXanh[0] = IntVar()
#         self.freezeTraXanh[1] = IntVar()
#         self.freezeTraXanh[2] = IntVar()

#         self.freezeSocola = [0,0,0]
#         self.freezeSocola[0] = IntVar()
#         self.freezeSocola[1] = IntVar()
#         self.freezeSocola[2] = IntVar()

#         self.freezeCookies = [0,0,0]
#         self.freezeCookies[0] = IntVar()
#         self.freezeCookies[1] = IntVar()
#         self.freezeCookies[2] = IntVar()

#         self.freezeXanhDauDo = [0,0,0]
#         self.freezeXanhDauDo[0] = IntVar()
#         self.freezeXanhDauDo[1] = IntVar()
#         self.freezeXanhDauDo[2] = IntVar()

#         self.freezeClassicPhin = [0,0,0]
#         self.freezeClassicPhin[0] = IntVar()
#         self.freezeClassicPhin[1] = IntVar()
#         self.freezeClassicPhin[2] = IntVar()

#         self.chanhDaXay = [0,0,0]
#         self.chanhDaXay[0] = IntVar()
#         self.chanhDaXay[1] = IntVar()
#         self.chanhDaXay[2] = IntVar()

#         self.chanhDayDa = [0,0,0]
#         self.chanhDayDa[0] = IntVar()
#         self.chanhDayDa[1] = IntVar()
#         self.chanhDayDa[2] = IntVar()

#         self.tacDaVien = [0,0,0]
#         self.tacDaVien[0] = IntVar()
#         self.tacDaVien[1] = IntVar()
#         self.tacDaVien[2] = IntVar()

#         self.socola = [0,0,0]
#         self.socola[0] = IntVar()
#         self.socola[1] = IntVar()
#         self.socola[2] = IntVar()

#         self.suaChuaDa = [0,0,0]
#         self.suaChuaDa[0] = IntVar()
#         self.suaChuaDa[1] = IntVar()
#         self.suaChuaDa[2] = IntVar()
        
#         self.wrapper1 = LabelFrame(self.root, bd=5, bg="#FFE699")
#         self.wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
#         self.mycanvas = Canvas(self.wrapper1, width=900, height=200, highlightthickness=0, bg="#FFE699")
#         self.mycanvas.pack(side=LEFT, fill="y", padx=10)

#         yscrollbar = ttk.Scrollbar(self.wrapper1, orient="vertical", command=self.mycanvas.yview)
#         yscrollbar.pack(side=RIGHT, fill="y")
#         self.mycanvas.configure(yscrollcommand=yscrollbar.set)
#         self.mycanvas.bind('<Configure>', lambda e: self.mycanvas.configure(scrollregion = self.mycanvas.bbox('all')))
#         self.myframe = Frame(self.mycanvas, bg="#FFE699")
#         self.mycanvas.create_window((0,0), window=self.myframe, anchor="nw")


#         #---LABEL: CÀ PHÊ PHA PHIN
#         self.label_name = Label(self.myframe, text="CÀ PHÊ PHA PHIN", bg="#FFE699", font=('Calibri(Body) 11 bold italic underline'))
#         self.label_name.grid(row=0, column=0, pady=(10,0), sticky="w")
        
#         # Label: Phin Sữa Đá
#         self.label_name = Label(self.myframe, text="Phin Sữa Đá", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=1, column=0, pady=(10,0), sticky="w")
#         # Size: Phin Sữa Đá
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=1, column=1, pady=(10,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.phinSuaDa[0])
#         self.entry1_1.grid(row=1, column=2, pady=(10,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=1, column=3, pady=(10,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.phinSuaDa[1])
#         self.entry1_2.grid(row=1, column=4, pady=(10,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=1, column=5, pady=(10,0), padx=(30,0),sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.phinSuaDa[2])
#         self.entry1_3.grid(row=1, column=6, pady=(10,0), sticky="w")

#         #Label: Phin Đen Đá
#         self.label_name = Label(self.myframe, text="Phin Đen Đá", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=2, column=0, pady=(5,0), sticky="w")
#         #Size: Phin Đen Đá
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=2, column=1, pady=(5,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.phinDenDa[0])
#         self.entry1_1.grid(row=2, column=2, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=2, column=3, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.phinDenDa[0])
#         self.entry1_2.grid(row=2, column=4, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=2, column=5, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.phinDenDa[2])
#         self.entry1_3.grid(row=2, column=6, pady=(5,0), sticky="w")

#         #Label: Bạc Xĩu Đá
#         self.label_name = Label(self.myframe, text="Bạc Xĩu Đá", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=3, column=0, pady=(5,0), sticky="w")
#         #Size: Bạc Xĩu Đá 
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=3, column=1, pady=(5,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.bacXiuDa[0])
#         self.entry1_1.grid(row=3, column=2, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=3, column=3, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.bacXiuDa[1])
#         self.entry1_2.grid(row=3, column=4, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=3, column=5, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.bacXiuDa[2])
#         self.entry1_3.grid(row=3, column=6, pady=(5,0), sticky="w")

#         #---LABEL: CÀ PHÊ ESPRESSO
#         self.label_name = Label(self.myframe, text="CÀ PHÊ ESPRESSO", bg="#FFE699", font=('Calibri(Body) 11 bold italic underline'))
#         self.label_name.grid(row=4, column=0, pady=(10,0), sticky="w")
        
#         # Label: Espresso/Americano
#         self.label_name = Label(self.myframe, text="Espresso/Americano", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=5, column=0, pady=(10,0), sticky="w")
#         # Size: Espresso/Americano
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=5, column=1, pady=(10,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.espresso[0])
#         self.entry1_1.grid(row=5, column=2, pady=(10,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=5, column=3, pady=(10,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.espresso[1])
#         self.entry1_2.grid(row=5, column=4, pady=(10,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=5, column=5, pady=(10,0), padx=(30,0),sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.espresso[2])
#         self.entry1_3.grid(row=5, column=6, pady=(10,0), sticky="w")

#         #Label: Cappuccino/Latte
#         self.label_name = Label(self.myframe, text="Cappuccino/Latte", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=6, column=0, pady=(5,0), sticky="w")
#         #Size: Cappuccino/Latte
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=6, column=1, pady=(5,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.cappiccino[0])
#         self.entry1_1.grid(row=6, column=2, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=6, column=3, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.cappiccino[1])
#         self.entry1_2.grid(row=6, column=4, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=6, column=5, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.cappiccino[2])
#         self.entry1_3.grid(row=6, column=6, pady=(5,0), sticky="w")

#         #Label: Mocha/Macchiato
#         self.label_name = Label(self.myframe, text="Mocha/Macchiato", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=7, column=0, pady=(5,0), sticky="w")
#         #Size: Mocha/Macchiato
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=7, column=1, pady=(5,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.mocha[0])
#         self.entry1_1.grid(row=7, column=2, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=7, column=3, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.mocha[1])
#         self.entry1_2.grid(row=7, column=4, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=7, column=5, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.mocha[2])
#         self.entry1_3.grid(row=7, column=6, pady=(5,0), sticky="w")

#         #---LABEL: TRÀ
#         self.label_name = Label(self.myframe, text="TRÀ", bg="#FFE699", font=('Calibri(Body) 11 bold italic underline'))
#         self.label_name.grid(row=8, column=0, pady=(10,0), sticky="w")
        
#         # Label: Sen Vàng
#         self.label_name = Label(self.myframe, text="Sen Vàng", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=9, column=0, pady=(10,0), sticky="w")
#         # Size: Sen Vàng
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=9, column=1, pady=(10,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.traSenVang[0])
#         self.entry1_1.grid(row=9, column=2, pady=(10,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=9, column=3, pady=(10,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.traSenVang[1])
#         self.entry1_2.grid(row=9, column=4, pady=(10,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=9, column=5, pady=(10,0), padx=(30,0),sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.traSenVang[2])
#         self.entry1_3.grid(row=9, column=6, pady=(10,0), sticky="w")

#         #Label: Thạch Đào
#         self.label_name = Label(self.myframe, text="Thạch Đào", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=10, column=0, pady=(5,0), sticky="w")
#         #Size: Thạch Đào
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=10, column=1, pady=(5,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.traThachDao[0])
#         self.entry1_1.grid(row=10, column=2, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=10, column=3, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.traThachDao[1])
#         self.entry1_2.grid(row=10, column=4, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=10, column=5, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.traThachDao[2])
#         self.entry1_3.grid(row=10, column=6, pady=(5,0), sticky="w")

#         #Label: Thạch Vải
#         self.label_name = Label(self.myframe, text="Thạch Vải", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=11, column=0, pady=(5,0), sticky="w")
#         #Size: Thạch Vải
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=11, column=1, pady=(5,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.traThachVai[0])
#         self.entry1_1.grid(row=11, column=2, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=11, column=3, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.traThachVai[1])
#         self.entry1_2.grid(row=11, column=4, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=11, column=5, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.traThachVai[2])
#         self.entry1_3.grid(row=11, column=6, pady=(5,0), sticky="w")

#         #Label: Xanh Đậu Đỏ
#         self.label_name = Label(self.myframe, text="Xanh Đậu Đỏ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=12, column=0, pady=(5,0), sticky="w")
#         #Size: Xanh Đậu Đỏ
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=12, column=1, pady=(5,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.xanhDauDo[0])
#         self.entry1_1.grid(row=12, column=2, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=12, column=3, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.xanhDauDo[1])
#         self.entry1_2.grid(row=12, column=4, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=12, column=5, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.xanhDauDo[2])
#         self.entry1_3.grid(row=12, column=6, pady=(5,0), sticky="w")

#         #---LABEL: FREEZE
#         self.label_name = Label(self.myframe, text="FREEZE", bg="#FFE699", font=('Calibri(Body) 11 bold italic underline'))
#         self.label_name.grid(row=13, column=0, pady=(10,0), sticky="w")
        
#         # Label: Trà Xanh
#         self.label_name = Label(self.myframe, text="Trà Xanh", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=14, column=0, pady=(10,0), sticky="w")
#         # Size: Trà Xanh
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=14, column=1, pady=(10,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeTraXanh[0])
#         self.entry1_1.grid(row=14, column=2, pady=(10,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=14, column=3, pady=(10,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeTraXanh[1])
#         self.entry1_2.grid(row=14, column=4, pady=(10,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=14, column=5, pady=(10,0), padx=(30,0),sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeTraXanh[2])
#         self.entry1_3.grid(row=14, column=6, pady=(10,0), sticky="w")

#         #Label: Sô-cô-la
#         self.label_name = Label(self.myframe, text="Sô-cô-la", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=15, column=0, pady=(5,0), sticky="w")
#         #Size: Sô-cô-la
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=15, column=1, pady=(5,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeSocola[0])
#         self.entry1_1.grid(row=15, column=2, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=15, column=3, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeSocola[1])
#         self.entry1_2.grid(row=15, column=4, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=15, column=5, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeSocola[2])
#         self.entry1_3.grid(row=15, column=6, pady=(5,0), sticky="w")

#         #Label: Cookies & Cream
#         self.label_name = Label(self.myframe, text="Cookies & Cream", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=16, column=0, pady=(5,0), sticky="w")
#         #Size: Cookies & Cream
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=16, column=1, pady=(5,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeCookies[0])
#         self.entry1_1.grid(row=16, column=2, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=16, column=3, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeCookies[1])
#         self.entry1_2.grid(row=16, column=4, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=16, column=5, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeCookies[2])
#         self.entry1_3.grid(row=16, column=6, pady=(5,0), sticky="w")

#         #Label: Caramel Phin
#         self.label_name = Label(self.myframe, text="Xanh Đậu Đỏ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=17, column=0, pady=(5,0), sticky="w")
#         #Size: Caramel Phin
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=17, column=1, pady=(5,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeXanhDauDo[0])
#         self.entry1_1.grid(row=17, column=2, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=17, column=3, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeXanhDauDo[1])
#         self.entry1_2.grid(row=17, column=4, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=17, column=5, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeXanhDauDo[2])
#         self.entry1_3.grid(row=17, column=6, pady=(5,0), sticky="w")

#         #Label: Classic Phin
#         self.label_name = Label(self.myframe, text="Classic Phin", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=19, column=0, pady=(5,0), sticky="w")
#         #Size: Classic Phin
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=19, column=1, pady=(5,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeClassicPhin[0])
#         self.entry1_1.grid(row=19, column=2, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=19, column=3, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeClassicPhin[1])
#         self.entry1_2.grid(row=19, column=4, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=19, column=5, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeClassicPhin[2])
#         self.entry1_3.grid(row=19, column=6, pady=(5,0), sticky="w")

#         #---LABEL: THỨC UỐNG KHÁC
#         self.label_name = Label(self.myframe, text="THỨC UỐNG KHÁC", bg="#FFE699", font=('Calibri(Body) 11 bold italic underline'))
#         self.label_name.grid(row=20, column=0, pady=(10,0), sticky="w")
        
#         # Label: Chanh Đá Xay
#         self.label_name = Label(self.myframe, text="Chanh Đá Xay", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=21, column=0, pady=(10,0), sticky="w")
#         # Size: Chanh Đá Xay
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=21, column=1, pady=(10,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.chanhDaXay[0])
#         self.entry1_1.grid(row=21, column=2, pady=(10,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=21, column=3, pady=(10,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.chanhDaXay[1])
#         self.entry1_2.grid(row=21, column=4, pady=(10,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=21, column=5, pady=(10,0), padx=(30,0),sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.chanhDaXay[2])
#         self.entry1_3.grid(row=21, column=6, pady=(10,0), sticky="w")

#         #Label: Chanh Dây Đá
#         self.label_name = Label(self.myframe, text="Chanh Dây Đá", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=22, column=0, pady=(5,0), sticky="w")
#         #Size: Chanh Dây Đá
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=22, column=1, pady=(5,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.chanhDayDa[0])
#         self.entry1_1.grid(row=22, column=2, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=22, column=3, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.chanhDayDa[1])
#         self.entry1_2.grid(row=22, column=4, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=22, column=5, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.chanhDayDa[2])
#         self.entry1_3.grid(row=22, column=6, pady=(5,0), sticky="w")

#         #Label: Tắc Đá Viên
#         self.label_name = Label(self.myframe, text="Tắc Đá Viên", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=23, column=0, pady=(5,0), sticky="w")
#         #Size: Tắc Đá Viên
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=23, column=1, pady=(5,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.tacDaVien[0])
#         self.entry1_1.grid(row=23, column=2, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=23, column=3, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.tacDaVien[1])
#         self.entry1_2.grid(row=23, column=4, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=23, column=5, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.tacDaVien[2])
#         self.entry1_3.grid(row=23, column=6, pady=(5,0), sticky="w")

#         #Label: Sô-cô-la
#         self.label_name = Label(self.myframe, text="Sô-cô-la", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=24, column=0, pady=(5,0), sticky="w")
#         #Size: Sô-cô-la
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=24, column=1, pady=(5,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.socola[0])
#         self.entry1_1.grid(row=24, column=2, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=24, column=3, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.socola[1])
#         self.entry1_2.grid(row=24, column=4, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=24, column=5, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.socola[2])
#         self.entry1_3.grid(row=24, column=6, pady=(5,0), sticky="w")

#         #Label: Sữa Chua Đá
#         self.label_name = Label(self.myframe, text="Sữa Chua Đá", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=25, column=0, pady=(5,0), sticky="w")
#         #Size: Classic Phin
#         self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=25, column=1, pady=(5,0), sticky="w", padx=(100,0))
#         self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.suaChuaDa[0])
#         self.entry1_1.grid(row=25, column=2, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=25, column=3, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.suaChuaDa[1])
#         self.entry1_2.grid(row=25, column=4, pady=(5,0), sticky="w")
#         self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
#         self.label_size.grid(row=25, column=5, pady=(5,0), padx=(30,0), sticky="w")
#         self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.suaChuaDa[2])
#         self.entry1_3.grid(row=25, column=6, pady=(5,0), sticky="w")

#         #---LABEL: THÔNG TIN KHÁCH HÀNG
#         self.label_name = Label(self.myframe, text="THÔNG TIN KHÁCH HÀNG", bg="#FFE699", font=('Calibri(Body) 11 bold italic underline'))
#         self.label_name.grid(row=26, column=0, pady=(10,0), sticky="w")
        
#         # Label: Họ và tên
#         self.label_name = Label(self.myframe, text="Họ tên: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=27, column=0, pady=(10,0), sticky="w")
#         # Entry: Họ và tên
#         self.entry_name = ttk.Entry(self.myframe, width=30, font=('Calibri(Body) 12'), textvariable=self.khachhang[0])
#         self.entry_name.grid(row=27, column=0, padx=20, pady=(10,0), columnspan=2)

#         # Label: Số điện thoại
#         self.label_name = Label(self.myframe, text="SĐT: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=28, column=0, pady=(10,0), sticky="w")
#         # Entry: Số điện thoại
#         self.entry_name = ttk.Entry(self.myframe, width=30, font=('Calibri(Body) 12'), textvariable=self.khachhang[1])
#         self.entry_name.grid(row=28, column=0, padx=20, pady=(10,0), columnspan=2)

#         # Label: Email
#         self.label_name = Label(self.myframe, text="Email: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
#         self.label_name.grid(row=29, column=0, pady=(10,10), sticky="w")
#         # Entry: Email
#         self.entry_name = ttk.Entry(self.myframe, width=30, font=('Calibri(Body) 12'), textvariable=self.khachhang[2])
#         self.entry_name.grid(row=29, column=0, padx=20, pady=(10,10), columnspan=2)
# ##

    # def bottomFrame(self):
    #     self.date = StringVar()

    #     self.wrapper2 = LabelFrame(self.root, bd=5, bg="#FFE699")
    #     self.wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)

    #     #Label: Nhập ngày
    #     self.label_name = Label(self.wrapper2, text="Nhập ngày: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
    #     self.label_name.grid(row=0, column=0, pady=(10,0), padx=(10,0), sticky="w")
    #     #Entry: Nhập ngày
    #     self.entry_name = ttk.Entry(self.wrapper2, width=16, font=('Calibri(Body) 12'), textvariable=self.date)
    #     self.entry_name.grid(row=0, column=1, pady=(10,0))


    #     #Button: Tìm kiếm
    #     self.btn_search = Button(self.wrapper2, text="Tìm kiếm", bg="#FF6600", fg="#000000", font=('Calibri(Body) 11 bold'), bd=5, highlightcolor="#000000", width=25)
    #     self.btn_search.grid(row=1, column=0, columnspan=2, pady=(10,0), padx=(10,0), sticky="w")

    #     #Button: Xem tất cả hóa đơn
    #     self.btn_search = Button(self.wrapper2, text="Xem tất cả hóa đơn", bg="#FF6600", fg="#000000", font=('Calibri(Body) 11 bold'), bd=5, highlightcolor="#000000", width=25)
    #     self.btn_search.grid(row=2, column=0, columnspan=2, pady=(10,0), padx=(10,0), sticky="w")

    #     #Label: Nhập ID
    #     self.label_name = Label(self.wrapper2, text="Nhập ID: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
    #     self.label_name.grid(row=0, column=3, pady=(10,0), padx=(130,0), sticky="w")
    #     #Entry: Nhập ID
    #     self.entry_name = ttk.Entry(self.wrapper2, width=18, font=('Calibri(Body) 12'), textvariable=self.date)
    #     self.entry_name.grid(row=0, column=4, pady=(10,0))


    #     #Button: Chi tiết hóa đơn
    #     self.btn_search = Button(self.wrapper2, text="Chi tiết hóa đơn", bg="#FF6600", fg="#000000", font=('Calibri(Body) 11 bold'), bd=5, highlightcolor="#000000", width=25)
    #     self.btn_search.grid(row=1, column=3, columnspan=2, pady=(10,0), padx=(130,0), sticky="w")

    #     #Button: Xóa
    #     self.btn_search = Button(self.wrapper2, text="Xóa", bg="#FF6600", fg="#000000", font=('Calibri(Body) 11 bold'), bd=5, highlightcolor="#000000", width=7)
    #     self.btn_search.grid(row=2, column=3, pady=(10,0), padx=(130,0), sticky="w")

    #     #Button: Chỉnh sửa
    #     self.btn_search = Button(self.wrapper2, text="Chỉnh sửa", bg="#FF6600", fg="#000000", font=('Calibri(Body) 11 bold'), bd=5, highlightcolor="#000000", width=12)
    #     self.btn_search.grid(row=2, column=4, columnspan=2, pady=(10,0), padx=(8,0), sticky="w")


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

        self.khachhang = ['','','']
        self.khachhang[0] = StringVar()
        self.khachhang[1] = StringVar()
        self.khachhang[2] = StringVar()
        self.phinSuaDa = [0,0,0]
        self.phinSuaDa[0] = IntVar()
        self.phinSuaDa[1] = IntVar()
        self.phinSuaDa[2] = IntVar()
        self.phinDenDa = [0,0,0]
        self.phinDenDa[0] = IntVar()
        self.phinDenDa[1] = IntVar()
        self.phinDenDa[2] = IntVar()
        self.bacXiuDa = [0,0,0]
        self.bacXiuDa[0] = IntVar()
        self.bacXiuDa[1] = IntVar()
        self.bacXiuDa[2] = IntVar()
        self.espresso = [0,0,0]
        self.espresso[0] = IntVar()
        self.espresso[1] = IntVar()
        self.espresso[2] = IntVar()
        self.cappiccino = [0,0,0]
        self.cappiccino[0] = IntVar()
        self.cappiccino[1] = IntVar()
        self.cappiccino[2] = IntVar()
        self.mocha = [0,0,0]
        self.mocha[0] = IntVar()
        self.mocha[1] = IntVar()
        self.mocha[2] = IntVar()
        self.traSenVang = [0,0,0]
        self.traSenVang[0] = IntVar()
        self.traSenVang[1] = IntVar()
        self.traSenVang[2] = IntVar()
        self.traThachDao = [0,0,0]
        self.traThachDao[0] = IntVar()
        self.traThachDao[1] = IntVar()
        self.traThachDao[2] = IntVar()
        self.traThachVai = [0,0,0]
        self.traThachVai[0] = IntVar()
        self.traThachVai[1] = IntVar()
        self.traThachVai[2] = IntVar()
        self.xanhDauDo = [0,0,0]
        self.xanhDauDo[0] = IntVar()
        self.xanhDauDo[1] = IntVar()
        self.xanhDauDo[2] = IntVar()
        self.freezeTraXanh = [0,0,0]
        self.freezeTraXanh[0] = IntVar()
        self.freezeTraXanh[1] = IntVar()
        self.freezeTraXanh[2] = IntVar()
        self.freezeSocola = [0,0,0]
        self.freezeSocola[0] = IntVar()
        self.freezeSocola[1] = IntVar()
        self.freezeSocola[2] = IntVar()
        self.freezeCookies = [0,0,0]
        self.freezeCookies[0] = IntVar()
        self.freezeCookies[1] = IntVar()
        self.freezeCookies[2] = IntVar()
        self.freezeXanhDauDo = [0,0,0]
        self.freezeXanhDauDo[0] = IntVar()
        self.freezeXanhDauDo[1] = IntVar()
        self.freezeXanhDauDo[2] = IntVar()
        self.freezeClassicPhin = [0,0,0]
        self.freezeClassicPhin[0] = IntVar()
        self.freezeClassicPhin[1] = IntVar()
        self.freezeClassicPhin[2] = IntVar()
        self.chanhDaXay = [0,0,0]
        self.chanhDaXay[0] = IntVar()
        self.chanhDaXay[1] = IntVar()
        self.chanhDaXay[2] = IntVar()
        self.chanhDayDa = [0,0,0]
        self.chanhDayDa[0] = IntVar()
        self.chanhDayDa[1] = IntVar()
        self.chanhDayDa[2] = IntVar()
        self.tacDaVien = [0,0,0]
        self.tacDaVien[0] = IntVar()
        self.tacDaVien[1] = IntVar()
        self.tacDaVien[2] = IntVar()
        self.socola = [0,0,0]
        self.socola[0] = IntVar()
        self.socola[1] = IntVar()
        self.socola[2] = IntVar()
        self.suaChuaDa = [0,0,0]
        self.suaChuaDa[0] = IntVar()
        self.suaChuaDa[1] = IntVar()
        self.suaChuaDa[2] = IntVar()
    
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
        self.entry1_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.phinSuaDa[0])
        self.entry1_1.grid(row=1, column=2, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=1, column=3, pady=(10,0), padx=(30,0), sticky="w")
        self.entry1_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.phinSuaDa[1])
        self.entry1_2.grid(row=1, column=4, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=1, column=5, pady=(10,0), padx=(30,0),sticky="w")
        self.entry1_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.phinSuaDa[2])
        self.entry1_3.grid(row=1, column=6, pady=(10,0), sticky="w")

        #Label: Phin Đen Đá
        self.label_name = Label(self.myframe, text="Phin Đen Đá", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=2, column=0, pady=(5,0), sticky="w")
        #Size: Phin Đen Đá
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=2, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry2_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.phinDenDa[0])
        self.entry2_1.grid(row=2, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=2, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry2_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.phinDenDa[1])
        self.entry2_2.grid(row=2, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=2, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry2_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.phinDenDa[2])
        self.entry2_3.grid(row=2, column=6, pady=(5,0), sticky="w")

        #Label: Bạc Xĩu Đá
        self.label_name = Label(self.myframe, text="Bạc Xĩu Đá", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=3, column=0, pady=(5,0), sticky="w")
        #Size: Bạc Xĩu Đá 
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=3, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry3_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.bacXiuDa[0])
        self.entry3_1.grid(row=3, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=3, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry3_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.bacXiuDa[1])
        self.entry3_2.grid(row=3, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=3, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry3_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.bacXiuDa[2])
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
        self.entry4_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.espresso[0])
        self.entry4_1.grid(row=5, column=2, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=5, column=3, pady=(10,0), padx=(30,0), sticky="w")
        self.entry4_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.espresso[1])
        self.entry4_2.grid(row=5, column=4, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=5, column=5, pady=(10,0), padx=(30,0),sticky="w")
        self.entry4_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.espresso[2])
        self.entry4_3.grid(row=5, column=6, pady=(10,0), sticky="w")

        #Label: Cappuccino/Latte
        self.label_name = Label(self.myframe, text="Cappuccino/Latte", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=6, column=0, pady=(5,0), sticky="w")
        #Size: Cappuccino/Latte
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=6, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry5_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.cappiccino[0])
        self.entry5_1.grid(row=6, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=6, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry5_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.cappiccino[1])
        self.entry5_2.grid(row=6, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=6, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry5_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.cappiccino[2])
        self.entry5_3.grid(row=6, column=6, pady=(5,0), sticky="w")

        #Label: Mocha/Macchiato
        self.label_name = Label(self.myframe, text="Mocha/Macchiato", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=7, column=0, pady=(5,0), sticky="w")
        #Size: Mocha/Macchiato
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=7, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry6_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.mocha[0])
        self.entry6_1.grid(row=7, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=7, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry6_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.mocha[1])
        self.entry6_2.grid(row=7, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=7, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry6_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.mocha[2])
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
        self.entry7_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.traSenVang[0])
        self.entry7_1.grid(row=9, column=2, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=9, column=3, pady=(10,0), padx=(30,0), sticky="w")
        self.entry7_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.traSenVang[1])
        self.entry7_2.grid(row=9, column=4, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=9, column=5, pady=(10,0), padx=(30,0),sticky="w")
        self.entry7_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.traSenVang[2])
        self.entry7_3.grid(row=9, column=6, pady=(10,0), sticky="w")

        #Label: Thạch Đào
        self.label_name = Label(self.myframe, text="Thạch Đào", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=10, column=0, pady=(5,0), sticky="w")
        #Size: Thạch Đào
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=10, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry8_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.traThachDao[0])
        self.entry8_1.grid(row=10, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=10, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry8_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.traThachDao[1])
        self.entry8_2.grid(row=10, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=10, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry8_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.traThachDao[2])
        self.entry8_3.grid(row=10, column=6, pady=(5,0), sticky="w")

        #Label: Thạch Vải
        self.label_name = Label(self.myframe, text="Thạch Vải", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=11, column=0, pady=(5,0), sticky="w")
        #Size: Thạch Vải
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=11, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry9_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.traThachVai[0])
        self.entry9_1.grid(row=11, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=11, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry9_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.traThachVai[1])
        self.entry9_2.grid(row=11, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=11, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry9_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.traThachVai[2])
        self.entry9_3.grid(row=11, column=6, pady=(5,0), sticky="w")

        #Label: Xanh Đậu Đỏ
        self.label_name = Label(self.myframe, text="Xanh Đậu Đỏ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=12, column=0, pady=(5,0), sticky="w")
        #Size: Xanh Đậu Đỏ
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=12, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry10_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.xanhDauDo[0])
        self.entry10_1.grid(row=12, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=12, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry10_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.xanhDauDo[1])
        self.entry10_2.grid(row=12, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=12, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry10_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.xanhDauDo[2])
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
        self.entry11_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeTraXanh[0])
        self.entry11_1.grid(row=14, column=2, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=14, column=3, pady=(10,0), padx=(30,0), sticky="w")
        self.entry11_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeTraXanh[1])
        self.entry11_2.grid(row=14, column=4, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=14, column=5, pady=(10,0), padx=(30,0),sticky="w")
        self.entry11_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeTraXanh[2])
        self.entry11_3.grid(row=14, column=6, pady=(10,0), sticky="w")

        #Label: Sô-cô-la
        self.label_name = Label(self.myframe, text="Sô-cô-la", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=15, column=0, pady=(5,0), sticky="w")
        #Size: Sô-cô-la
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=15, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry12_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeSocola[0])
        self.entry12_1.grid(row=15, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=15, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry12_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeSocola[1])
        self.entry12_2.grid(row=15, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=15, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry12_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeSocola[2])
        self.entry12_3.grid(row=15, column=6, pady=(5,0), sticky="w")

        #Label: Cookies & Cream
        self.label_name = Label(self.myframe, text="Cookies & Cream", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=16, column=0, pady=(5,0), sticky="w")
        #Size: Cookies & Cream
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=16, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry13_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeCookies[0])
        self.entry13_1.grid(row=16, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=16, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry13_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeCookies[1])
        self.entry13_2.grid(row=16, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=16, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry13_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeCookies[2])
        self.entry13_3.grid(row=16, column=6, pady=(5,0), sticky="w")

        #Label: Caramel Phin
        self.label_name = Label(self.myframe, text="Xanh Đậu Đỏ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=17, column=0, pady=(5,0), sticky="w")
        #Size: Caramel Phin
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=17, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry14_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeXanhDauDo[0])
        self.entry14_1.grid(row=17, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=17, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry14_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeXanhDauDo[1])
        self.entry14_2.grid(row=17, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=17, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry14_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeXanhDauDo[2])
        self.entry14_3.grid(row=17, column=6, pady=(5,0), sticky="w")

        #Label: Classic Phin
        self.label_name = Label(self.myframe, text="Classic Phin", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=19, column=0, pady=(5,0), sticky="w")
        #Size: Classic Phin
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=19, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry15_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeClassicPhin[0])
        self.entry15_1.grid(row=19, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=19, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry15_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeClassicPhin[1])
        self.entry15_2.grid(row=19, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=19, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry15_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.freezeClassicPhin[2])
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
        self.entry16_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.chanhDaXay[0])
        self.entry16_1.grid(row=21, column=2, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=21, column=3, pady=(10,0), padx=(30,0), sticky="w")
        self.entry16_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.chanhDaXay[1])
        self.entry16_2.grid(row=21, column=4, pady=(10,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=21, column=5, pady=(10,0), padx=(30,0),sticky="w")
        self.entry16_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.chanhDaXay[2])
        self.entry16_3.grid(row=21, column=6, pady=(10,0), sticky="w")

        #Label: Chanh Dây Đá
        self.label_name = Label(self.myframe, text="Chanh Dây Đá", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=22, column=0, pady=(5,0), sticky="w")
        #Size: Chanh Dây Đá
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=22, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry17_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.chanhDayDa[0])
        self.entry17_1.grid(row=22, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=22, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry17_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.chanhDayDa[1])
        self.entry17_2.grid(row=22, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=22, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry17_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.chanhDayDa[2])
        self.entry17_3.grid(row=22, column=6, pady=(5,0), sticky="w")

        #Label: Tắc Đá Viên
        self.label_name = Label(self.myframe, text="Tắc Đá Viên", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=23, column=0, pady=(5,0), sticky="w")
        #Size: Tắc Đá Viên
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=23, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry18_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.tacDaVien[0])
        self.entry18_1.grid(row=23, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=23, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry18_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.tacDaVien[1])
        self.entry18_2.grid(row=23, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=23, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry18_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.tacDaVien[2])
        self.entry18_3.grid(row=23, column=6, pady=(5,0), sticky="w")

        #Label: Sô-cô-la
        self.label_name = Label(self.myframe, text="Sô-cô-la", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=24, column=0, pady=(5,0), sticky="w")
        #Size: Sô-cô-la
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=24, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry19_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.socola[0])
        self.entry19_1.grid(row=24, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=24, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry19_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.socola[1])
        self.entry19_2.grid(row=24, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=24, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry19_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.socola[2])
        self.entry19_3.grid(row=24, column=6, pady=(5,0), sticky="w")

        #Label: Sữa Chua Đá
        self.label_name = Label(self.myframe, text="Sữa Chua Đá", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=25, column=0, pady=(5,0), sticky="w")
        #Size: Sữa Chua Đá
        self.label_size = Label(self.myframe, text="Nhỏ (30.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=25, column=1, pady=(5,0), sticky="w", padx=(100,0))
        self.entry20_1 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.suaChuaDa[0])
        self.entry20_1.grid(row=25, column=2, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Vừa (40.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=25, column=3, pady=(5,0), padx=(30,0), sticky="w")
        self.entry20_2 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.suaChuaDa[1])
        self.entry20_2.grid(row=25, column=4, pady=(5,0), sticky="w")
        self.label_size = Label(self.myframe, text="Lớn (50.000đ):", bg="#FFE699", font=('Calibri(Body) 11'))
        self.label_size.grid(row=25, column=5, pady=(5,0), padx=(30,0), sticky="w")
        self.entry20_3 = ttk.Entry(self.myframe, font=('Calibri(Body) 11'), width=3, textvariable=self.suaChuaDa[2])
        self.entry20_3.grid(row=25, column=6, pady=(5,0), sticky="w")

        #---LABEL: THÔNG TIN KHÁCH HÀNG
        self.label_name = Label(self.myframe, text="THÔNG TIN KHÁCH HÀNG", bg="#FFE699", font=('Calibri(Body) 11 bold italic underline'))
        self.label_name.grid(row=26, column=0, pady=(10,0), sticky="w")
        
        # Label: Họ và tên
        self.label_name = Label(self.myframe, text="Họ tên: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=27, column=0, pady=(10,0), sticky="w")
        # Entry: Họ và tên
        self.entry_name = ttk.Entry(self.myframe, width=30, font=('Calibri(Body) 12'), textvariable=self.khachhang[0])
        self.entry_name.grid(row=27, column=0, padx=20, pady=(10,0), columnspan=2)

        # Label: Số điện thoại
        self.label_name = Label(self.myframe, text="SĐT: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=28, column=0, pady=(10,0), sticky="w")
        # Entry: Số điện thoại
        self.entry_phone = ttk.Entry(self.myframe, width=30, font=('Calibri(Body) 12'), textvariable=self.khachhang[1])
        self.entry_phone.grid(row=28, column=0, padx=20, pady=(10,0), columnspan=2)

        # Label: Email
        self.label_name = Label(self.myframe, text="Email: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=29, column=0, pady=(10,10), sticky="w")
        # Entry: Email
        self.entry_email = ttk.Entry(self.myframe, width=30, font=('Calibri(Body) 12'), textvariable=self.khachhang[2])
        self.entry_email.grid(row=29, column=0, padx=20, pady=(10,10), columnspan=2)


class buttonFrame(): 
    def __init__(self, root, topframe): 
        self.root = root
        self.topframe = topframe
        self.khachhang = topframe.khachhang
        self.phinSuaDa = topframe.phinSuaDa
        self.phinDenDa = topframe.phinDenDa
        self.bacXiuDa = topframe.bacXiuDa
        self.espresso = topframe.espresso
        self.cappiccino = topframe.cappiccino
        self.mocha = topframe.mocha
        self.traSenVang = topframe.traSenVang
        self.traThachDao = topframe.traThachDao
        self.traThachVai = topframe.traThachVai
        self.xanhDauDo = topframe.xanhDauDo
        self.freezeTraXanh = topframe.freezeTraXanh
        self.freezeSocola = topframe.freezeSocola
        self.freezeCookies = topframe.freezeCookies
        self.freezeXanhDauDo = topframe.freezeXanhDauDo
        self.freezeClassicPhin = topframe.freezeClassicPhin
        self.chanhDaXay = topframe.chanhDaXay
        self.chanhDayDa = topframe.chanhDayDa
        self.tacDaVien = topframe.tacDaVien
        self.socola = topframe.socola
        self.suaChuaDa = topframe.suaChuaDa

    def showButton(self):
        self.date = StringVar()
        self.id = StringVar()

        self.wrapper2 = LabelFrame(self.root, bd=5, bg="#FFE699")
        self.wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)

        #Label: Nhập ngày
        self.label_name = Label(self.wrapper2, text="Nhập ngày: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=0, column=0, pady=(10,0), padx=(10,0), sticky="w")
        #Entry: Nhập ngày
        self.entry = ttk.Entry(self.wrapper2, width=16, font=('Calibri(Body) 12'), textvariable=self.date)
        self.entry.grid(row=0, column=1, pady=(10,0))


        #Button: Tìm kiếm
        self.btn_search = Button(self.wrapper2, text="Tìm kiếm", bg="#FF6600", fg="#000000", font=('Calibri(Body) 11 bold'), bd=5, highlightcolor="#000000", width=25)
        self.btn_search.grid(row=1, column=0, columnspan=2, pady=(10,0), padx=(10,0), sticky="w")

        #Button: Xem tất cả hóa đơn
        self.btn_search = Button(self.wrapper2, text="Xem tất cả hóa đơn", bg="#FF6600", fg="#000000", font=('Calibri(Body) 11 bold'), bd=5, highlightcolor="#000000", width=25)
        self.btn_search.grid(row=2, column=0, columnspan=2, pady=(10,0), padx=(10,0), sticky="w")

        #Label: Nhập ID
        self.label_name = Label(self.wrapper2, text="Nhập ID: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=0, column=3, pady=(10,0), padx=(130,0), sticky="w")
        #Entry: Nhập ID
        self.entry_name = ttk.Entry(self.wrapper2, width=18, font=('Calibri(Body) 12'), textvariable=self.id)
        self.entry_name.grid(row=0, column=4, pady=(10,0))

        #Button: Chi tiết hóa đơn
        self.btn_search = Button(self.wrapper2, text="Chi tiết hóa đơn", bg="#FF6600", fg="#000000", font=('Calibri(Body) 11 bold'), bd=5, highlightcolor="#000000", width=26, command=self.query)
        self.btn_search.grid(row=1, column=3, columnspan=2, pady=(10,0), padx=(130,0), sticky="w")

        #Button: Xóa
        self.btn_search = Button(self.wrapper2, text="Xóa", bg="#FF6600", fg="#000000", font=('Calibri(Body) 11 bold'), bd=5, highlightcolor="#000000", width=7)
        self.btn_search.grid(row=2, column=3, pady=(10,0), padx=(130,0), sticky="w")

        #Button: Chỉnh sửa
        self.btn_search = Button(self.wrapper2, text="Chỉnh sửa", bg="#FF6600", fg="#000000", font=('Calibri(Body) 11 bold'), bd=5, highlightcolor="#000000", width=16, command=self.edit)
        self.btn_search.grid(row=2, column=4, columnspan=2, pady=(10,0), padx=(10,0), sticky="w")

        #Label: ID
        self.label_name = Label(self.wrapper2, text="ID: ", bg="#FFE699", font=('Calibri(Body) 11 bold '))
        self.label_name.grid(row=0, column=5, pady=(10,0), padx=(130,0), sticky="w")
        #Entry: ID - DISABLED
        self.entry_name = ttk.Entry(self.wrapper2, width=18 ,font=('Calibri(Body) 12 bold'))
        self.entry_name.insert(0, "HT280822NB00001")
        #self.entry_name.config(state=DISABLED)
        self.entry_name.grid(row=0, column=6, pady=(10,0))

        #Button: Thêm hóa đơn
        self.btn_search = Button(self.wrapper2, text="Thêm", bg="#FF6600", fg="#000000", font=('Calibri(Body) 11 bold'), bd=5, highlightcolor="#000000", width=20, height=4, command=self.submit)
        self.btn_search.grid(row=1, column=5, rowspan=2, columnspan=2, pady=(10,0), padx=(130,0), sticky="w")

    def submit(self):
        self.connect = sqlite3.connect('data.db') # Kết nối với database
        self.cursor = connect.cursor()

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
            :suaChuaDa1, :suaChuaDa2, :suaChuaDa3 
            )""",
                {
                    'name': self.khachhang[0].get(), 'phone': self.khachhang[1].get(), 'email': self.khachhang[2].get(),
                    'phinSuaDa1': self.phinSuaDa[0].get(), 'phinSuaDa2': self.phinSuaDa[1].get(), 'phinSuaDa3': self.phinSuaDa[2].get(), 
                    'phinDenDa1': self.phinDenDa[0].get(), 'phinDenDa2': self.phinDenDa[1].get(), 'phinDenDa3': self.phinDenDa[2].get(),
                    'bacXiuDa1': self.bacXiuDa[0].get(), 'bacXiuDa2': self.bacXiuDa[1].get(), 'bacXiuDa3': self.bacXiuDa[2].get(),
                    'espresso1': self.espresso[0].get(), 'espresso2': self.espresso[1].get(), 'espresso3': self.espresso[2].get(),
                    'cappiccino1': self.cappiccino[0].get(), 'cappiccino2': self.cappiccino[1].get(), 'cappiccino3': self.cappiccino[2].get(),
                    'mocha1': self.mocha[0].get(), 'mocha2': self.mocha[1].get(), 'mocha3': self.mocha[2].get(),
                    'traSenVang1': self.traSenVang[0].get(), 'traSenVang2': self.traSenVang[1].get(), 'traSenVang3': self.traSenVang[2].get(), 
                    'traThachDao1': self.traThachDao[0].get(), 'traThachDao2': self.traThachDao[1].get(), 'traThachDao3': self.traThachDao[2].get(), 
                    'traThachVai1': self.traThachVai[0].get(), 'traThachVai2': self.traThachVai[1].get(), 'traThachVai3': self.traThachVai[2].get(),
                    'xanhDauDo1': self.xanhDauDo[0].get(), 'xanhDauDo2': self.xanhDauDo[1].get(), 'xanhDauDo3': self.xanhDauDo[2].get(), 
                    'freezeTraXanh1': self.freezeTraXanh[0].get(), 'freezeTraXanh2': self.freezeTraXanh[1].get(), 'freezeTraXanh3': self.freezeTraXanh[2].get(), 
                    'freezeSocola1': self.freezeSocola[0].get(), 'freezeSocola2': self.freezeSocola[1].get(), 'freezeSocola3': self.freezeSocola[2].get(), 
                    'freezeCookies1': self.freezeCookies[0].get(), 'freezeCookies2': self.freezeCookies[1].get(), 'freezeCookies3': self.freezeCookies[2].get(),
                    'freezeXanhDauDo1': self.freezeXanhDauDo[0].get(), 'freezeXanhDauDo2': self.freezeXanhDauDo[1].get(), 'freezeXanhDauDo3': self.freezeXanhDauDo[2].get(), 
                    'freezeClassicPhin1': self.freezeClassicPhin[0].get(), 'freezeClassicPhin2': self.freezeClassicPhin[1].get(), 'freezeClassicPhin3': self.freezeClassicPhin[2].get(),
                    'chanhDaXay1': self.chanhDaXay[0].get(), 'chanhDaXay2': self.chanhDaXay[1].get(), 'chanhDaXay3': self.chanhDaXay[2].get(),
                    'chanhDayDa1': self.chanhDayDa[0].get(), 'chanhDayDa2': self.chanhDayDa[1].get(), 'chanhDayDa3': self.chanhDayDa[2].get(),
                    'tacDaVien1': self.tacDaVien[0].get(), 'tacDaVien2': self.tacDaVien[1].get(), 'tacDaVien3': self.tacDaVien[2].get(),
                    'socola1': self.socola[0].get(), 'socola2': self.socola[1].get(), 'socola3': self.socola[2].get(), 
                    'suaChuaDa1': self.suaChuaDa[0].get(), 'suaChuaDa2': self.suaChuaDa[1].get(), 'suaChuaDa3': self.suaChuaDa[2].get() 
                })

        connect.commit()
        # Clear the text boxes
        self.topframe.entry1_1.delete(0, END)
        self.topframe.entry1_1.insert(0, 0)
    
    def query(self):
        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()

        # Query the database
        cursor.execute("SELECT *, oid FROM addresses")
        records = cursor.fetchall()

        # Loop through results
        for record in records:
            print(record)
        
        # Commit changes
        connect.commit()

    def edit(self): 
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
        record_id = str(int(self.id.get()[10:])) #HT290822NB0001
        
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
            
        # Create the lower frame
        # self.wrapper4 = LabelFrame(editor, bd=5, bg="#FFE699")
        # self.wrapper4.pack(fill="both", expand="yes", padx=10, pady=10)

        # Button: Lưu thông tin
        self.btn_save = Button(editor, text="Lưu thông tin", bg="#FF6600", fg="#000000", font=('Calibri(Body) 11 bold'), bd=5, highlightcolor="#000000", width=26, command=self.update)
        self.btn_save.pack(fill="both", expand="yes", padx=10, pady=(5,10))

    def update(self):
        # Create a database or connection to one
        connect = sqlite3.connect('data.db')
        # Create cursor (in a fuction)
        cursor = connect.cursor()
        # Convert the ID into index number in database
        record_id = str(int(self.id.get()[10:])) #HT290822NB0001

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
            suaChuaDa1 = :suaChuaDa1, suaChuaDa2 = :suaChuaDa2, suaChuaDa3 = :suaChuaDa3
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

                'oid': record_id
            }
        )

        # Commit changes
        connect.commit()
        # Close the editor window
        editor.destroy()

        



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
        suaChuaDa1 int, suaChuaDa2 int, suaChuaDa3 int
        )""") 
    
# def submit(self):
#     connect = sqlite3.connect('address_book.db') # Kết nối với database
#     cursor = connect.cursor()

#     # Insert into table
#     cursor.execute("""INSERT INTO addresses VALUES (:name, :phone, :email,
#         :phinSuaDa1 , :phinSuaDa2 , :phinSuaDa3 , 
#         :phinDenDa1 , :phinDenDa2 , :phinDenDa3 ,
#         :bacXiuDa1 , :bacXiuDa2 , :bacXiuDa3 ,
#         :espresso1 , :espresso2 , :espresso3 ,
#         :cappiccino1 , :cappiccino2 , :cappiccino3 ,
#         :mocha1 , :mocha2 , :mocha3 ,
#         :traSenVang1 , :traSenVang2 , :traSenVang3 , 
#         :traThachDao1 , :traThachDao2 , :traThachDao3 , 
#         :traThachVai1 , :traThachVai2 , :traThachVai3,
#         :xanhDauDo1 , :xanhDauDo2 , :xanhDauDo3 , 
#         :freezeTraXanh1 , :freezeTraXanh2 , :freezeTraXanh3 , 
#         :freezeSocola1 , :freezeSocola2 , :freezeSocola3 , 
#         :freezeCookies1 , :freezeCookies2 , :freezeCookies3 ,
#         :freezeXanhDauDo1 , :freezeXanhDauDo2 , :freezeXanhDauDo3 , 
#         :freezeClassicPhin1 , :freezeClassicPhin2 , :freezeClassicPhin3
#         )""",
# 			{
# 				'name': bill.
# 				'l_name': l_name.get(),
# 				'address': address.get(),
# 				'city': city.get(),
# 				'state': state.get(),
# 				'zipcode': zipcode.get()
# 			})
    
    

#     # Commit changes
#     conn.commit()
#     # Close database file, or close connection
#     conn.close()

#     # Clear the text boxes
#     f_name.delete(0, END)
#     l_name.delete(0, END)
#     address.delete(0, END)
#     city.delete(0, END)
#     state.delete(0, END)
#     zipcode.delete(0, END)



if __name__ == "__main__": 
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
    
    