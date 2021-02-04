from modules.irasas import Irasas


class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, nauja_suma):
        irasas = Irasas("Pajamos", nauja_suma)
        self.zurnalas.append(irasas)

    def prideti_islaidu_irasa(self, nauja_suma):
        irasas = Irasas("Išlaidos", nauja_suma)
        self.zurnalas.append(irasas)

    def parodyti_ataskaita(self):
        print("Pajamų/išlaidų sąrašas:")
        for irasas in self.zurnalas:
            print(irasas)

    def gauti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if irasas.tipas == "Pajamos":
                balansas += irasas.suma
            if irasas.tipas == "Išlaidos":
                balansas -= irasas.suma
        print("Balansas", balansas)
