import json

from collections import namedtuple

from model.Emoticono import Emoticono
from webservice.web_service import WebService


def custom_data_decoder(response_data_dictionary):
    return namedtuple("Emoticono", response_data_dictionary.keys())(*response_data_dictionary.values())


def get_all_emoticonos() -> list:
    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/emoticono/ObtenerTodosLosEmoticonosSinBorrado").get_request_json()
    return json.loads(json_elementos, object_hook=custom_data_decoder)


def delete_emoticono_by_id_logic(id_emoticono: int) -> bool:
    dict_data = {
        "Id": id_emoticono
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/emoticono/BorradoLogicoEmoticono").put_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def reactivar_emoticono_by_id_logic(id_emoticono: int) -> bool:
    dict_data = {
        "Id": id_emoticono
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/emoticono/ReactivarEmoticono").put_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def eliminar_emoticono(id_emoticono: int) -> bool:
    dict_data = {
        "Id": id_emoticono
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/emoticono/BorradoRealEmoticono").delete_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def actualizar_emoticono(emoticono: Emoticono) -> bool:
    dict_data = Emoticono.to_dict_data(emoticono)
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/emoticono/ActualizarEmoticono").put_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def insertar_emoticono(emoticono: Emoticono) -> bool:
    dict_data = Emoticono.to_dict_data(emoticono)
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/emoticono/InsertarEmoticono").post_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True
