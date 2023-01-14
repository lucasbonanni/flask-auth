import os
from flask import Flask

SECRET_KEY = os.environ.get('SECRET_KEY', 'changeme')
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASS')

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        DB_SERVER=DB_HOST,
    )

    @app.route('/')
    def hello_geek():
        return '<h1>Hello from Flask & Docker</h2>'

    return app

if __name__ == "__main__":
    create_app().run()
