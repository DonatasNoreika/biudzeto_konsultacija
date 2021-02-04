
from modules.biudzetas import Biudzetas

biudzetas = Biudzetas()

biudzetas.prideti_pajamu_irasa(25, "Jotautas", "Skola")
biudzetas.prideti_pajamu_irasa(500, naujas_tipas="Avansas")
biudzetas.prideti_islaidu_irasa(200, "Grynais", "Batonas")
biudzetas.parodyti_ataskaita()
biudzetas.gauti_balansa()

