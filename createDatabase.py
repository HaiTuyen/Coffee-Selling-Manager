from tkinter import *
from tkinter import ttk
import sqlite3


if __name__ == "__main__": 
    connect = sqlite3.connect('data.db')
    cursor = connect.cursor()

    cursor.execute( """ CREATE TABLE addresses (
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
        
        totalCost int, id text
        )""") 

    connect.commit()
    connect.close()

    
    