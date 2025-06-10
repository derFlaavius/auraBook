from tkinter import messagebox

def digit(wert, name): # Prüfung, ob Intager eingehalten wurde
    for c in wert:
        if c.isdigit == False:
            messagebox.showwarning("Ungültige Eingabe", f"Bitte gib in dem Feld {name} nur Zahlen ein!")
            return False
    return True

def char50(wert, name): # Begrenzung auf 50 Zeichen
    i = 0
    for c in wert:
        i += 1
    if i >= 50:
        messagebox.showwarning("Ungültige Eingabe", f"Du hast in dem Feld {name} das Zeichenlimit von 50 überschritten.")
        return False
    else:
        return True