
from modules.irasas import Irasas

class IslaiduIrasas(Irasas):
    def __init__(self, suma, apmokejimo_budas, preke_paslauga):
        super().__init__(suma)
        self.apmokejimo_budas = apmokejimo_budas
        self.preke_paslauga = preke_paslauga

    def __str__(self):
        return f"Išlaidos: {self.suma} apmokėjimo būdas: {self.apmokejimo_budas}, įgyta prekė/paslauga: {self.preke_paslauga}"

    def __repr__(self):
        return f"Išlaidos: {self.suma} apmokėjimo būdas: {self.apmokejimo_budas}, įgyta prekė/paslauga: {self.preke_paslauga}"