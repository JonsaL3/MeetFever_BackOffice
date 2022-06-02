import json

from collections import namedtuple

from model.Opinion import Opinion
from webservice.web_service import WebService


def custom_data_decoder(response_data_dictionary):
    return namedtuple("Opinion", response_data_dictionary.keys())(*response_data_dictionary.values())


def get_all_opiniones() -> list:
    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/opinion/ObtenerTodasLasOpinionesSinBorrado").get_request_json()
    return json.loads(json_elementos, object_hook=custom_data_decoder)


def delete_opinion_by_id_logic(id_opinion: int) -> bool:
    dict_data = {
        "Id": id_opinion
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/opinion/BorradoLogicoOpinion").put_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def reactivar_opinion_by_id_logic(id_opinion: int) -> bool:
    dict_data = {
        "Id": id_opinion
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/opinion/ReactivarOpinion").put_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def delete_opinion_by_id(id_opinion: int) -> bool:
    dict_data = {
        "Id": id_opinion
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/opinion/BorradoRealOpinion").delete_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def insert_opinion(opinion: Opinion) -> bool:
    dict_data = Opinion.to_dict_data(opinion)
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/opinion/InsertarOpinion").post_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def update_opinion(opinion: Opinion) -> bool:
    dict_data = Opinion.to_dict_data(opinion)
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/opinion/ActualizarOpinion").put_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True
