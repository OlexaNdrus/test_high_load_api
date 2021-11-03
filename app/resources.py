"""Module has methods that triggers for corresponding http methods"""

import falcon
import falcon.asgi

from app.helpers import create_clients_json, validate_request_body
from app.schemas import ClientsListSchema


class MessageResource:
    def __init__(self):
        self._clients = 'Empty List'

    async def on_post(self, req, resp):
        """
        This method invokes on post request
        """

        media = await req.get_media()
        validate_request_body(schema=ClientsListSchema, request_body=media)
        message = media.get('clients')

        self._clients = create_clients_json(message)

        resp.status = falcon.HTTP_200
        resp.media = {
            "clients": self._clients
        }
