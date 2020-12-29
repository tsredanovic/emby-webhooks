import requests

import settings


def report_to_discord(event):
    # Create message
    message = None

    # System
    if event.category == 'system':
        if event.action == 'webhooktest':
            message = 'Test.'
    # Playback
    elif event.category == 'playback':
        if event.action == 'start':
            message = 'User `{}` started playing `{}`.'.format(event.user_name, event.item_name)
        elif event.action == 'pause':
            message = 'User `{}` paused `{}`.'.format(event.user_name, event.item_name)
        elif event.action == 'unpause':
            message = 'User `{}` unpaused `{}`.'.format(event.user_name, event.item_name)
        elif event.action == 'stop':
            message = 'User `{}` stopped `{}`.'.format(event.user_name, event.item_name)

    if not message:
        return

    # Report
    requests.post(
        url=settings.DISCORD_WEBHOOK_URL,
        data={'content': message}
    )
