from flask import Flask, request, json


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    @app.route('/emby_webhook', methods=['POST'])
    def index():
        request_json = json.loads(request.form.get('data', {}))
        event = request_json.get('Event', None)
        if not event:
            print('Missing event.')
        print('Got event: {}'.format(event))
        event_category = event.split('.')[0]
        event_action = event.split('.')[1]

        message = None

        # System
        if event_category == 'system':
            if event_action == 'webhooktest':
                message = 'Test.'

        # Playback
        elif event_category == 'playback':
            user_name = request_json.get('User', {}).get('Name', None)
            item_name = request_json.get('Item', {}).get('Name', None)
            if event_action == 'start':
                message = 'User `{}` started playing `{}`.'.format(user_name, item_name)
            elif event_action == 'pause':
                message = 'User `{}` paused `{}`.'.format(user_name, item_name)
            elif event_action == 'unpause':
                message = 'User `{}` unpaused `{}`.'.format(user_name, item_name)
            elif event_action == 'stop':
                message = 'User `{}` stopped `{}`.'.format(user_name, item_name)

        print(message)
        return ''

    return app
