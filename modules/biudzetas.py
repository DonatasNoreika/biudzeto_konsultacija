from modules.pajamu_irasas import PajamuIrasas
from modules.islaidu_irasas import IslaiduIrasas
import pickle

class Biudzetas:
    def __init__(self):
        self.zurnalas = self._gauti_zurnala()

    def _gauti_zurnala(self):
        try:
            with open('biudzetas.pkl', 'rb') as failas:
                zurnalas = pickle.load(failas)
                return zurnalas
        except:
            zurnalas = []
            return zurnalas

    def _issaugoti_i_zurnala(self):
        try:
            with open('biudzetas.pkl', 'wb') as failas:
                pickle.dump(self.zurnalas, failas)
        except:
            print("Nepavyko atidaryti failo")

    def prideti_pajamu_irasa(self, nauja_suma, naujas_siuntejas="Darbovietė", naujas_tipas="Atlyginimas"):
        irasas = PajamuIrasas(nauja_suma, naujas_siuntejas, naujas_tipas)
        self.zurnalas.append(irasas)
        self._issaugoti_i_zurnala()

    def prideti_islaidu_irasa(self, nauja_suma, naujas_apmokejimo_budas="Kortele", nauja_preke_paslauga="Maistas"):
        irasas = IslaiduIrasas(nauja_suma, naujas_apmokejimo_budas, nauja_preke_paslauga)
        self.zurnalas.append(irasas)
        self._issaugoti_i_zurnala()

    def parodyti_ataskaita(self):
        print("Pajamų/išlaidų sąrašas:")
        for irasas in self.zurnalas:
            print(irasas)

    def gauti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                balansas += irasas.suma
            if type(irasas) is IslaiduIrasas:
                balansas -= irasas.suma
        print("Balansas", balansas)
