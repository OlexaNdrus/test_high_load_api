High Load Api

# High Load Api

High Load Api it is testing task written in Falcon

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages.

```bash
pip install requirements.txt
```

## Used tools and libraries

- Falcon
- Requests
- Pytest
- Uvicorn
- Httpie
- Marshmallow

## Usage

```shell
#For running app server:
uvicorn app.asgi:app
```

```python
# For testing one specific post request run:
# Specify variables or use default value 
# in tools/test_post_request.py file:
TEST_JSON_FILE_PATH = 'post.json'
URL = "http://127.0.0.1:8000/clients"
# Run script:
python tools/test_post_request.py

#Alternative way to test one post request with http tool:
http POST "URL/clients" < "PATH_TO_JSON_FILE"
# Where URL is url where app server is running and 
# PATH_TO_JSON_FILE is path to specific JSON file

#For testing performance load of this API, use predefined module tools/test_post_request.py
#Specify global variables in this module:
JSON_PATH = 'post.json'
NUM_OF_SIMULT_REQUESTS = 1000
URL = "http://127.0.0.1:8000/clients"
#Run script:
python tools/performance_test.py
```

### Requirements for test json object:
**POST method**
Request body should be specified according JSON schema in app/schemas.py file.
Basic sample:
```json
{
  "clients": [
    {
      "id": "59761c23b30d971669fb42ff",
      "isActive": true,
      "age": 36,
      "name": "Dunlap Hubbard",
      "gender": "male",
      "company": "CEDWARD",
      "email": "dunlaphubbard@cedward.com",
      "phone": "+1 (890) 543-2508",
      "address": "169 Rutledge Street, Konterra"
    }
  ]
}
```

