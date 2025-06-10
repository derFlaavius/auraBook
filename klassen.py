from datetime import date

class Guiwerte:
    def __init__(self):
        self.bnwidth = 21
        self.abst_buty = 40
        self.abst_lby = 25
        self.abst_rby = 30

class Person():
    def __init__(self):
        self.id = None
        self.name = None
        self.aura = None
        self.rang = None
        self.rangclr = None
        self.ereignisse = None

    def rang_festlegen(self):
        if self.aura >= 500000:
            self.rang = "Prof. Dr. Plusaura"
            self.rangclr = "#1418FF"
        elif self.aura >= 300000:
            self.rang = "Dr. Plusaura"
            self.rangclr = "#1466FF"
        elif self.aura >= 150000:
            self.rang = "Master of Plusaura"
            self.rangclr = "#1495FF"
        elif self.aura >= 80000:
            self.rang = "Bachelor Professional of Plusaura"
            self.rangclr = "#14FFB1"
        elif self.aura >= 10000:
            self.rang = "Fachabi Plusaura"
            self.rangclr = "#51FF00"
        elif self.aura >= 0:
            self.rang = "Auf gutem Wege!"
            self.rangclr = "#2B8D04"
        elif self.aura >= -30000:
            self.rang = "Auf schlechtem Wege!"
            self.rangclr = "#FFEF14"
        elif self.aura >= -100000:
            self.rang = "Fachabi Minusaura"
            self.rangclr = "#FF7214"
        elif self.aura >= -250000:
            self.rang = "Bachelor of Minusaura"
            self.rangclr = "#BC14FF"
        elif self.aura >= -500000:
            self.rang = "Dr. Minusaura"
            self.rangclr = "#FF14EB"
        elif self.aura >= -1000000:
            self.rang = "Prof. Dr. Minusaura"
            self.rangclr = "#FF1462"
        elif self.aura <= -1000000:
            self.rang = "Hopfen und Malz ist verloren!!!"
            self.rangclr = "#FF1414"
        return
    
class Eintrag:
    def __init__(self):
        self.datum = self.heute()
        self.pkt = None
        self.kommentar = None

    def heute(self):
        datum = date.today().strftime("%Y-%m-%d")
        return datum