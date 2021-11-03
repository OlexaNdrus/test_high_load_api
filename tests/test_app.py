import json

from falcon import testing
import pytest

from app import main

@pytest.fixture()
def client():
    return testing.TestClient(main.create_app())


def test_post_message(client):
    test_inputs = [
                      {'clients': [{'name': 'John'}]},
                      {'clients': [{'name': 'John', 'email': 'john@mail.com'}]},
                      {'clients': [{'name': 'John', 'email': 'john@mail.com'},
                                   {'name': 'Jill', 'email': 'jill@mail.com'}]}]

    results = [
               {'clients': ['John - NOT_FOUND']},
               {'clients': ['John - john@mail.com']},
               {'clients': ['John - john@mail.com', 'Jill - jill@mail.com']}
               ]

    for test_input, expected_result in zip(test_inputs, results):
        json_data = json.dumps(test_input)
        result = client.simulate_post(path='/clients', body=json_data)
        assert result.json == expected_result

def test_post_message_on_exceptions(client):
    test_inputs = [
                      {'': ['']},
                      {'clients': ['name']},
                      {'clients': [None]},
                      {'no-clients': [{'name': 'John', 'email': 'john@mail.com'},
                                   {'name': 'Jill', 'email': 'jill@mail.com'}]}]

    for test_input in test_inputs:
        json_data = json.dumps(test_input)
        result = client.simulate_post(path='/clients', body=json_data)
        assert result.status == '400 Bad Request' or '500 Internal Server Error'


