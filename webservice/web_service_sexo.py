import json

from collections import namedtuple

from model.Sexo import Sexo
from webservice.web_service import WebService


def custom_data_decoder(response_data_dictionary):
    return namedtuple("Sexos", response_data_dictionary.keys())(*response_data_dictionary.values())


def get_all_sexos() -> list:
    json_elementos = WebService("https://meetfever.eu/interface/api/meetfever/sexo/ObtenerTodosLosSexosSinBorrado") \
        .get_request_json()
    return json.loads(json_elementos, object_hook=custom_data_decoder)


def insert_sexo(empresa: Sexo) -> bool:
    dict_data = Sexo.to_dict_data(empresa)
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/sexo/InsertarSexo").post_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def update_sexo(empresa: Sexo) -> bool:
    dict_data = Sexo.to_dict_data(empresa)
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/sexo/ActualizarSexo").put_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def delete_sexo_by_id(id_sexo: int) -> bool:
    dict_data = {
        "Id": id_sexo
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/sexo/BorradoRealSexo").delete_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def delete_sexo_by_id_logico(id_sexo: int) -> bool:
    dict_data = {
        "Id": id_sexo
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/sexo/BorradoLogicoSexo").put_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def reactivar_sexo_by_id_logico(id_sexo: int) -> bool:
    dict_data = {
        "Id": id_sexo
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/sexo/ReactivarSexo").put_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True
