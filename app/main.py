"""This module contains main method which starts app and add routes"""

import falcon.asgi

from app.resources import MessageResource


def create_app():
    app = falcon.asgi.App()
    app.add_route('/clients', MessageResource())
    return app
