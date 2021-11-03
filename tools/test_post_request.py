"""Module for sending test POST request"""

from app.helpers import test_post_request

TEST_JSON_FILE_PATH = 'post.json'

if __name__ == "__main__":
    response = test_post_request(TEST_JSON_FILE_PATH)
    print(response)
