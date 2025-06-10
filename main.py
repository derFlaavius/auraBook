# from dbm import whichdb
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import sys
import klassen
import sql_befehle


def clearwdw():
    for widget in root.winfo_children():
        widget.place_forget()

def verlauf(person):
    def zurueck(tabelle):
        tabelle.destroy()
        bn_zurueck.destroy()
        mainscreen(pliste)
    
    def tabelle_erzeugen(daten):
        spalten = ("Datum", "Aura", "Grund")
        tabelle = ttk.Treeview(columns=spalten, show="headings")
        for spalte in spalten:
            tabelle.heading(spalte, text=spalte)
            tabelle.column(spalte, anchor="center", width=50)
        # Daten einfügen
        for eintrag in daten:
            tabelle.insert("", tk.END, values=eintrag)

        tabelle.pack(expand=False, fill="both")
        return tabelle

    clearwdw()
    # Tabelle
    tabelle = tabelle_erzeugen(person.ereignisse)   

    # Button
    bn_zurueck = ttk.Button(root, text="Zurück", width=gui_werte.abst_buty, command=lambda:zurueck(tabelle))
    bn_zurueck.pack()


def person_hinzufg():
    def check_eingabe():
        eingabe = tf_name.get()
        if eingabe == "":
            messagebox.showwarning("Fehlende Eingabe", "Bitte gib einen Namen ein.")
            return
        rm = sql_befehle.person_anlegen(eingabe)
        if rm == 1:
            messagebox.showerror("Fehler", "Dieser Name existiert bereits.")
            return
        elif rm == 2:
            messagebox.showerror("DB Fehler", "Es gab ein Problem mit der Datenbank")
            return
        messagebox.showinfo("Speicherung erfolgreich", "Der Name wurde erfolgreich gespeichert.")
        pliste = sql_befehle.personen_laden() # Personen neu laden
        mainscreen(pliste)
        
    clearwdw()
    pic_logo4.pack()

    # Label
    lb_eingabe = tk.Label(root, text="Wie lautet der Name?")

    # Button
    bn_bestaetigen = ttk.Button(root, text="Bestätigen", command=check_eingabe, width=gui_werte.bnwidth)
    bn_abbrechen = ttk.Button(root, text="Abbrechen", width=gui_werte.bnwidth, command=lambda:mainscreen(pliste))

    # Entry
    tf_name = ttk.Entry(root, width=gui_werte.bnwidth + 1)

    # Platzierung
    xwert = 40
    ywert = 170

    lb_eingabe.place(x=xwert, y=ywert)
    ywert += gui_werte.abst_lby
    tf_name.place(x=xwert, y=ywert)
    ywert += gui_werte.abst_buty
    bn_bestaetigen.place(x=xwert, y=ywert)
    ywert += gui_werte.abst_buty
    bn_abbrechen.place(x=xwert, y=ywert)
    ywert += gui_werte.abst_buty

def auswaehlen(lib_personen):
    # Abfrage Personendaten
    #lib_personen.get()
    index = lib_personen.curselection()
    print(index)
    global person
    person, rw = sql_befehle.person_laden(index)
    if rw == 1:
        messagebox.showwarning("Eingabe fehlt", "Bitte wähle zuvor einen Namen aus")
        return
    elif rw == 2:
        messagebox.showerror("Datenbank Fehler", "Es gab ein Problem mit der Datenverarbeitung")
        return
    
    # Elemente
    # Labels
    lb_pinfo = tk.Label(root, text=person.rang, fg=person.rangclr)
    lb_alternativ = tk.Label(root, text="Manuelle Eingabe")
    lb_punkte = tk.Label(root, text="Aura:")
    lb_kommentar= tk.Label(root, text="Kommentar:")

    # Buttons
    bnwidth = gui_werte.bnwidth
    bn_bestaetigen = ttk.Button(root, text="Bestätigen", width=bnwidth)
    bn_abbruch = ttk.Button(root, text="Abbruch", width=bnwidth, command=lambda:mainscreen(pliste))

    # Radioboxen
    cases = tk.IntVar(value=0)
    rb_case1 = ttk.Radiobutton(root, text="Case1", variable=cases, value=1)
    rb_case2 = ttk.Radiobutton(root, text="Case2", variable=cases, value=2)
    rb_case3 = ttk.Radiobutton(root, text="Case3", variable=cases, value=3)
    rb_case4 = ttk.Radiobutton(root, text="Case4", variable=cases, value=4)

    # Entry
    tf_punkte = ttk.Entry(root, width=bnwidth + 1)
    tf_kommentar = ttk.Entry(root, width=bnwidth + 1)

    # Platzierung
    xwert = 350
    ywert = 170
    lb_pinfo.place(x=xwert, y=ywert)
    ywert += gui_werte.abst_lby
    rb_case1.place(x=xwert, y=ywert)
    ywert += gui_werte.abst_rby
    rb_case2.place(x=xwert, y=ywert)
    ywert += gui_werte.abst_rby
    rb_case3.place(x=xwert, y=ywert)
    ywert += gui_werte.abst_rby
    rb_case4.place(x=xwert, y=ywert)
    ywert += gui_werte.abst_rby + 10
    lb_alternativ.place(x=xwert, y=ywert)
    ywert += gui_werte.abst_lby
    lb_punkte.place(x=xwert, y=ywert)
    ywert += gui_werte.abst_lby
    tf_punkte.place(x=xwert, y=ywert)
    ywert += gui_werte.abst_buty
    lb_kommentar.place(x=xwert, y=ywert)
    ywert += gui_werte.abst_lby
    tf_kommentar.place(x=xwert, y=ywert)
    ywert += gui_werte.abst_buty
    bn_bestaetigen.place(x=xwert, y=ywert)
    ywert += gui_werte.abst_buty
    bn_abbruch.place(x=xwert, y=ywert)

def mainscreen(pliste):
    def listbox(liste, xwert, ywert):
        listbox_widget = tk.Listbox(root, height=6, width=24, activestyle='none')
        if liste != []:
            for item in liste:
                listbox_widget.insert(tk.END, item)
        listbox_widget.place(x=xwert, y=ywert)
        return listbox_widget
    
    clearwdw()
    pic_logo4.pack()
    bnwidth = gui_werte.bnwidth

    # +++ Elemente +++
    # Labels
    lb_personen = tk.Label(root, text="Mensch*innen")

    # Buttons
    bn_auswaehlen = ttk.Button(root, text="Auswählen", width=bnwidth, command=lambda:auswaehlen(lib_personen))
    bn_personhnzfg = ttk.Button(root, text="Person hinzufügen", width=bnwidth, command=person_hinzufg)
    bn_verlauf = ttk.Button(root, text="Verlauf einsehen", width=bnwidth, command=lambda:verlauf(person))
    bn_beenden = ttk.Button(root, text="Beenden", width=bnwidth, command=sys.exit)

    # Platzieren
    xwert = 40 # Startwert
    ywert = 170 # Startwert

    global lib_personen
    lb_personen.place(x=xwert, y=ywert)
    ywert += gui_werte.abst_lby
    lib_personen = listbox(pliste, xwert, ywert)
    ywert += 130
    bn_auswaehlen.place(x=xwert, y=ywert)
    ywert += gui_werte.abst_buty
    bn_verlauf.place(x=xwert, y=ywert)
    ywert += gui_werte.abst_buty
    bn_personhnzfg.place(x=xwert, y=ywert)
    ywert += gui_werte.abst_buty
    bn_beenden.place(x=xwert, y=ywert)

# Deklaration Pfade
lnk_azure = os.path.join(os.path.dirname(__file__), "themes", "azure", "azure.tcl")
lnk_logo4 = os.path.join(os.path.dirname(__file__), "images", "logo4.png")

# Objekte und Listen vorladen
global pliste
gui_werte = klassen.Guiwerte()
pliste = sql_befehle.personen_laden()

# Erzeugung des Fensters
root = tk.Tk()
root.geometry("600x600")
root.title("auraBook v1.0.0 - Lass es raus!")

# Einstellung GUI
root.tk.call("source", lnk_azure)
root.tk.call("set_theme", "dark")

# Implementierung der Grafiken
logo4 = Image.open(lnk_logo4)
logo4 = logo4.resize((120, 140))
logo4 = ImageTk.PhotoImage(logo4)
pic_logo4 = tk.Label(root, image=logo4)

mainscreen(pliste)

root.mainloop()