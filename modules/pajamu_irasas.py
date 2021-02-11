
from modules.irasas import Irasas

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, tipas):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.tipas = tipas

    def __str__(self):
        return f"Pajamos: {self.suma}, siuntėjas: {self.siuntejas}, tipas: {self.tipas}"

    def __repr__(self):
        return f"Pajamos: {self.suma}, siuntėjas: {self.siuntejas}, tipas: {self.tipas}"