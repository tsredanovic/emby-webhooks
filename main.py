from flask import Flask, request, json

import settings
from discord import DiscordReport
from emby import EmbyEvent
from mongo import MongoUpload


def create_app():
    app = Flask(__name__)

    @app.route('/emby_webhook', methods=['POST'])
    def index():
        request_json = json.loads(request.form.get('data', {}))

        event = EmbyEvent(request_json)
        DiscordReport(settings.DISCORD_WEBHOOK_URL, event).send()
        MongoUpload(settings.MONGO_DB_USERNAME, settings.MONGO_DB_PASSWORD, settings.MONGO_DB_NAME, event).upload()

        return ''

    return app
