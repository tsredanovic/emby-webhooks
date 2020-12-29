from flask import Flask, request, json

from discord import report_to_discord
from emby import EmbyEvent
from mongo import upload_to_mongo


def create_app():
    app = Flask(__name__)

    @app.route('/emby_webhook', methods=['POST'])
    def index():
        request_json = json.loads(request.form.get('data', {}))

        event = EmbyEvent(request_json)
        report_to_discord(event)
        upload_to_mongo(event)

        return ''

    return app
