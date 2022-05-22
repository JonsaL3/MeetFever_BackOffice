import webservice.web_service_opinion as wso
import webservice.web_service_persona as wsp
import webservice.web_service_sexo as wss
import webservice.web_service_experiencia as wse
from gui.edition_gui import EditionGui

from gui.main_gui import MainGui


lista = wse.get_all_experiencias()

for elemento in lista:
    print(elemento.Titulo)


MainGui().iniciar_ventana()
# EditionGui().iniciar_ventana()