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
        self.rangclr = "green"
        self.ereignisse = None

    def rang_festlegen(self):
        self.rang = "Rang: Depp oida"
        self.rangclr = "green"
        return