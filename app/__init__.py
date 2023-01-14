from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def hello_geek():
        return '<h1>Hello from Flask & Docker</h2>'

    return app

if __name__ == "__main__":
    create_app().run()
