import requests
import json

from model.Data import Data
from collections import namedtuple
from tkinter import messagebox


# example url https://meetfever.eu/interface/api/meetfever/sexo/ObtenerTodosLosSexos


def custom_data_decoder(response_data_dictionary):
    return namedtuple("X", response_data_dictionary.keys())(*response_data_dictionary.values())


class WebService:

    def __init__(self, url: str):
        self.url = url

    def get_request_json(self):
        resp = requests.get(self.url, timeout=5)
        print(resp.text)
        json_string = resp.text
        x: Data = json.loads(json_string, object_hook=custom_data_decoder)
        if x.data.RETCODE == 0:
            return x.data.JSON_OUT
        else:
            messagebox.showerror("Error", x.data.MENSAJE)
            return None

    def put_request_json(self, dictionary: dict):
        resp = requests.put(self.url, json=dictionary, timeout=5)
        print(resp.text)
        json_string = resp.text
        x: Data = json.loads(json_string, object_hook=custom_data_decoder)
        if x.data.RETCODE == 0:
            return x.data.JSON_OUT
        else:
            messagebox.showerror("Error", x.data.MENSAJE)
            return None

    def post_request_json(self, dictionary: dict):
        resp = requests.post(self.url, json=dictionary, timeout=5)
        print(resp.text)
        json_string = resp.text
        x: Data = json.loads(json_string, object_hook=custom_data_decoder)
        if x.data.RETCODE == 0:
            return x.data.JSON_OUT
        else:
            messagebox.showerror("Error", x.data.MENSAJE)
            return None

    def delete_request_json(self, dictionary: dict):
        resp = requests.delete(self.url, json=dictionary, timeout=5)
        print(resp.text)
        json_string = resp.text
        x: Data = json.loads(json_string, object_hook=custom_data_decoder)
        if x.data.RETCODE == 0:
            return x.data.JSON_OUT
        else:
            messagebox.showerror("Error", x.data.MENSAJE)
