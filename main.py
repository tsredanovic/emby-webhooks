import os
from pathlib import Path
from flask import Flask, request, json
import jinja2
import requests


### Config

CONFIG_PATH = os.environ.get('EW_CONFIG_PATH', Path.joinpath(Path(__file__).resolve().parent, 'config.json'))

Path.joinpath(Path(__file__).resolve().parent, 'config.json')

with open(CONFIG_PATH) as f:
    config_json = json.load(f)

DISCORD_WEBHOOK_URLS = config_json.get('discord_webhook_urls', [])


### Templates

TEMPLATES_DIR_PATH = os.environ.get('EW_TEMPLATES_DIR_PATH', Path.joinpath(Path(__file__).resolve().parent, 'templates'))

template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATES_DIR_PATH)
template_env = jinja2.Environment(loader=template_loader)


### Helpers

def report_to_discord(message):
    for discord_webhook_url in DISCORD_WEBHOOK_URLS:
        requests.post(
            url=discord_webhook_url,
            data={
                'content': message
            }
        )

def create_app():
    app = Flask(__name__)

    @app.route('/emby_webhook', methods=['POST'])
    def index():
        event_data = json.loads(request.form.get('data', {}))

        template = template_env.get_template('{}.txt'.format(event_data['Event']))
        message = template.render(event_data)

        report_to_discord(message)

        return ''

    return app
