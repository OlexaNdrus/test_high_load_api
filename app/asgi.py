"""ASGI entrypoint. Configures Falcon and then runs the application"""

from app.main import create_app

app = create_app()
