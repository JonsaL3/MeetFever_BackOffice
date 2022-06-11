import json

from collections import namedtuple

from webservice.web_service import WebService


def custom_data_decoder(response_data_dictionary):
    return namedtuple("Log", response_data_dictionary.keys())(*response_data_dictionary.values())


def get_all_logs() -> list:  # TODO CONTROLADOR FIND ALL
    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/registroerrorcontroler/ObtenerRegistros").get_request_json()
    return json.loads(json_elementos, object_hook=custom_data_decoder)


def delete_log_by_id(id: int) -> bool:
    dict_data = {
        "Id": id
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/registroerrorcontroler/BorrarRegistroDeError").delete_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True
