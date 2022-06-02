import json

from collections import namedtuple

from model.Persona import Persona
from webservice.web_service import WebService


def custom_data_decoder(response_data_dictionary):
    return namedtuple("X", response_data_dictionary.keys())(*response_data_dictionary.values())


def get_all_personas() -> list:
    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/persona/ObtenerTodasPersonasSinBorrado").get_request_json()
    return json.loads(json_elementos, object_hook=custom_data_decoder)


def delete_persona_by_id_logic(id_persona: int) -> bool:
    dict_data = {
        "Id": id_persona
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/persona/BorradoLogicoPersona").put_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def reactivar_persona_by_id_logic(id_persona: int) -> bool:
    dict_data = {
        "Id": id_persona
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/persona/ReactivarPersona").put_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def delete_persona_by_id(id_persona: int) -> bool:
    dict_data = {
        "Id": id_persona
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/persona/BorradoRealPersona").delete_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def insert_persona(persona: Persona) -> bool:
    dict_data = Persona.to_dict_data(persona)
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/persona/InsertarPersona").post_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def update_persona(persona: Persona) -> bool:
    dict_data = Persona.to_dict_data(persona)
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/persona/ActualizarPersona").put_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True
