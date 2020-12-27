import requests


class DiscordReport:
    def __init__(self, webhook_url, event):
        self.webhook_url = webhook_url
        self.create_message(event)

    def create_message(self, event):
        # System
        if event.category == 'system':
            if event.action == 'webhooktest':
                self.message = 'Test.'
        # Playback
        elif event.category == 'playback':
            if event.action == 'start':
                self.message = 'User `{}` started playing `{}`.'.format(event.user_name, event.item_name)
            elif event.action == 'pause':
                self.message = 'User `{}` paused `{}`.'.format(event.user_name, event.item_name)
            elif event.action == 'unpause':
                self.message = 'User `{}` unpaused `{}`.'.format(event.user_name, event.item_name)
            elif event.action == 'stop':
                self.message = 'User `{}` stopped `{}`.'.format(event.user_name, event.item_name)

    def send(self):
        requests.post(
            url=self.webhook_url,
            data={'content': self.message}
        )