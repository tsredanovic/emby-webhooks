from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    @app.route('/emby_webhook', methods=['POST'])
    def index():
        print('GOT SOMETHING')
        return ''

    return app
