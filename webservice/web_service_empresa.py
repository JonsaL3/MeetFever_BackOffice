import json

from collections import namedtuple

from model.Empresa import Empresa
from webservice.web_service import WebService


def custom_data_decoder(response_data_dictionary):
    print(response_data_dictionary)
    return namedtuple("Empresa", response_data_dictionary.keys())(*response_data_dictionary.values())


def get_all_empresas() -> list[Empresa]:
    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/empresa/ObtenerEmpresasSinBorrado").get_request_json()
    return json.loads(json_elementos, object_hook=custom_data_decoder)


def delete_empresa_by_id_logic(id_empresa: int) -> bool:
    dict_data = {
        "Id": id_empresa
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/empresa/BorradoLogicoEmpresa").put_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def reactivar_empresa_by_id_logic(id_empresa: int) -> bool:
    dict_data = {
        "Id": id_empresa
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/empresa/ReactivarEmpresa").put_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def delete_empresa_by_id(id_empresa: int) -> bool:
    dict_data = {
        "Id": id_empresa
    }
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/empresa/BorradoRealEmpresa").delete_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


# En un lenguaje normal me crearía una funcion en empresa que fuese to dict data...
def update_empresa(empresa: Empresa) -> bool:
    dict_data = Empresa.to_dict_data(empresa)
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/empresa/ActualizarEmpresa").put_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True


def insert_empresa(empresa: Empresa) -> bool:
    dict_data = Empresa.to_dict_data(empresa)
    print(json.dumps(dict_data))

    json_elementos = WebService(
        "https://meetfever.eu/interface/api/meetfever/empresa/InsertarEmpresa").post_request_json(dict_data)

    if json_elementos is None:
        return False
    else:
        return True
