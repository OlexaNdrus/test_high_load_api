import falcon.asgi, os

from app.resources import MessageResource


def create_app():
    app = falcon.asgi.App()
    app.add_route('/clients', MessageResource())
    return app

