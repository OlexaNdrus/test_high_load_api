"""This module contains different helper fuctions"""

import os
import json
import typing

import falcon
import requests


def create_clients_json(json_data):
    """
    This is method to create POST response body

    :param json_data: this is json_data from request
    :returns: dictionary
    :raises TypeError: if json_data is not a list
            TypeError: if client is not a dictionary
    """

    output_data = []
    for client in json_data:
        output_data.append(f"{client.get('id', 'NOT_FOUND')} - {client.get('email', 'NOT_FOUND')}")
    return output_data


def read_json(file_path):
    """
    This method parse json from local file

    :param file_path: path to json file
    :returns: json object as dictionary
    :raises OSError: if file_path is not valid
            JSONDecodeError: if data in file isnt json
    """

    if os.path.exists(file_path):
        with open(file_path) as file:
            try:
                data = json.load(file)
            except BaseException:
                raise json.decoder.JSONDecodeError('Data in test json file isnt json')
        return data
    else:
        raise OSError('Wrong path for json testfile')


def test_post_request(json_path):
    """
    This method simulates post request

    :param json_path: path to json file
    :returns: json body from response
    :raises Exception: if response status is not ok
    """

    json_data = read_json(json_path)
    resp = requests.post("http://127.0.0.1:8000/clients", json=json_data)
    if not resp.status_code == 200:
        raise Exception(f'Bad status code : {resp.status_code, resp.text}')
    return resp.json()

# def json_validator(json_data: typing.Dict):
#     if 'client' in json_data.keys():
#         clients = json_data['client']
#         if not isinstance(clients, list):
#             return TypeError('Expected list as value for "clients" key')
#         return True
#     return TypeError('Required "clients" attribute is missing')
#
# def item_validator(item_data: typing.Dict):
#     string_attributes = ["id", "age", "name", "gender", "company", "email", "phone", "address"]
#     int_attributes = ["age"]
#     boolean_attributes = ["isActive"]
#     required_attributes = ["id", "email"]
#     validations_errors = []
#
#     if not isinstance(item_data, dict):
#         validations_errors.append(f"Client data expected to ne in dictionary format")
#
#     if not all(True if attr in item_data else False for attr in required_attributes):
#         validations_errors.append(f"One of required attributes is missing {required_attributes}")
#
#     for attribute in string_attributes:
#         if attribute in item_data:
#             if attribute in string_attributes and not isinstance(item_data.get(attribute), str):
#                 validations_errors.append(f"key {attribute} is not a string, got {item_data.get(attribute)}")
#
#     for attribute in int_attributes:
#         if attribute in item_data:
#             if attribute in string_attributes and not isinstance(item_data.get(attribute), int):
#                 validations_errors.append(f"key {attribute} is not a integer, got {item_data.get(attribute)}")
#
#     for attribute in boolean_attributes:
#         if attribute in item_data:
#             if attribute in string_attributes and not isinstance(item_data.get(attribute), bool):
#                 validations_errors.append(f"key {attribute} is not a boolean, got {item_data.get(attribute)}")
#
#     return validations_errors


def validate_request_body(schema, request_body: dict, partial=None):
    """
    Validate request body using Marshmallow schema.

    :param schema: marshmallow schema class
    :param request_body: parsed json from request body
    :param partial: whether to ignore missing fields. If None, the value for self.partial is used.
        If its value is an iterable, only missing fields listed in that iterable will be ignored.
    :returns: None
    :raises ValidationError: raises an exception if data does not match the schema
    """
    error = schema().validate(request_body, partial=partial)

    if error:
        raise falcon.HTTPBadRequest(f'Bad request caused by invalid json structure: {error}')


