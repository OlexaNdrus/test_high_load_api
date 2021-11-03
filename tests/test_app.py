import json

from falcon import testing
import pytest

from app import main, helpers

@pytest.fixture()
def client():
    return testing.TestClient(main.create_app())


def test_post_message(client):
    test_inputs = [
                      {'clients': [{'id': '123', 'name': 'John', 'email': 'test@mail.com'}]},
                      {'clients': [{'id': 'John', 'email': 'john@mail.com'}]},
                      {'clients': [{'id': '0', 'name': 'John', 'email': 'john@mail.com'},
                                   {'id': '1', 'name': 'Jill', 'email': 'jill@mail.com'}]}]

    results = [
               {'clients': ['123 - test@mail.com']},
               {'clients': ['John - john@mail.com']},
               {'clients': ['0 - john@mail.com', '1 - jill@mail.com']}
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
        assert result.status == '400 Bad Request'

def test_read_json_wrong_path():
    for path in ['/', '//', 'path', '', ""]:
        with pytest.raises(OSError):
            helpers.read_json(path)



