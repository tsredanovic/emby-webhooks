from datetime import datetime


class EmbyEvent:
    def __init__(self, input_json):
        event = input_json['Event']
        self.category = event.split('.')[0]
        self.action = event.split('.')[1]
        self.timestamp = datetime.now()

        if self.category == 'playback':
            self.user_name = input_json.get('User', {}).get('Name')
            self.item_name = input_json.get('Item', {}).get('Path', '').split('/')[-1]
            self.provider_ids = input_json.get('Item', {}).get('ProviderIds')
            self.ip = input_json.get('Session', {}).get('RemoteEndPoint')
            self.device_name = input_json.get('Session', {}).get('DeviceName')
