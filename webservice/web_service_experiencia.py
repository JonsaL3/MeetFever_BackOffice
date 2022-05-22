import json

from collections import namedtuple

from webservice.web_service import WebService


def custom_data_decoder(response_data_dictionary):
    return namedtuple("X", response_data_dictionary.keys())(*response_data_dictionary.values())


def get_all_experiencias() -> list:
    json_elementos = WebService("https://meetfever.eu/interface/api/meetfever/experiencia/ObtenerTodasLasExperiencias").get_request_json()
    return json.loads(json_elementos, object_hook=custom_data_decoder)
