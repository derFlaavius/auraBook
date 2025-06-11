import mariadb
import klassen

def personen_laden():
    pliste = [[1, "Person1"], [2, "Person2"]] # Testweise, wird durch SQL Befehl ersetzt
    return pliste, 0 # Erfolg
    return pliste, 1 # Fehler beim Abrufen der Daten

def person_laden(id):
    def test():
        pdaten.id = 1
        pdaten.name = "Max"
        pdaten.aura = -50000000
        pdaten.rang_festlegen()
        pdaten.ereignisse = [[2025-12-12, -50, "In GTA verloren"], [2025-12-13, -30, "Dummer Spruch"]] # Tag des ereignisses, Aurapunkte add/diff, Kommentar
        return pdaten
    
    pdaten = klassen.Person()
    pdaten = test()
    return pdaten, 0 # 0=i.o.
    return pdaten, 1 # 1=Fehler
    
def person_anlegen(name):
    return 0 # i.o.
    return 1 # Fehler: Name vorhanden
    return 2 # Fehler: Sonstige Fehler

def person_bearbeiten(eintrag):
    return 0 # i.o.
    return 1 # Fehler