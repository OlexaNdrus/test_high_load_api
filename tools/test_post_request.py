"""Module for sending test POST request"""

from app.helpers import test_post_request

TEST_JSON_FILE_PATH = 'post.json'
URL = "http://127.0.0.1:8000/clients"

if __name__ == "__main__":
    response = test_post_request(URL, TEST_JSON_FILE_PATH)
    print(response)
