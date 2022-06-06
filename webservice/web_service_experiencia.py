import json

from collections import namedtuple

from model.Experiencia import Experiencia
from webservice.web_service import WebService


def custom_data_decoder(response_data_dictionary):
    return namedtuple("Experiencia", response_data_dictionary.keys())(*response_data_dictionary.values())


def get_all_experiencias() -> list:
    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/experiencia/ObtenerTodasExperienciasSinBorrado").get_request_json()
    return json.loads(json_elementos, object_hook=custom_data_decoder)


def delete_experiencia_by_id_logic(id: int) -> bool:
    dict_data = {
        "Id": id
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/experiencia/BorradoLogicoExperiencia").put_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def delete_experiencia_by_id(id: int) -> bool:
    dict_data = {
        "Id": id
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/experiencia/BorradoRealExperiencia").delete_request_json(
        dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def reactivar_experiencia_by_id(id: int) -> bool:
    dict_data = {
        "Id": id
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/experiencia/ReactivarExperiencia").put_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def insertar_experiencia(experiencia: Experiencia):
    dict_data = Experiencia.to_dict_data(experiencia)
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/experiencia/InsertarExperiencia").post_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def actualizar_experiencia(experiencia: Experiencia):
    dict_data = Experiencia.to_dict_data(experiencia)
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/experiencia/ActualizarExperiencia").put_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def confirmar_solicitud_borrado(id: int) -> bool:
    dict_data = {
        "Id": id
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/experiencia/SolicitarBorradoEperiencia").put_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True
