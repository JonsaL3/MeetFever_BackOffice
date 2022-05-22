import json

from collections import namedtuple

from model.Persona import Persona
from webservice.web_service import WebService


def custom_data_decoder(response_data_dictionary):
    return namedtuple("X", response_data_dictionary.keys())(*response_data_dictionary.values())


def get_all_personas() -> list:
    json_elementos = WebService("https://meetfever.eu/interface/api/meetfever/persona/ObtenerTodasLasPersonas").get_request_json()
    return json.loads(json_elementos, object_hook=custom_data_decoder)
