import pymongo


class MongoUpload:
    def __init__(self, username, password, db_name, event):
        self.connect_url = 'mongodb+srv://{}:{}@cluster0.vwwky.mongodb.net/{}?retryWrites=true&w=majority'.format(
            username,
            password,
            db_name,
        )
        self.create_payload(event)

    def create_payload(self, event):
        if event.category == 'playback':
            self.payload = {
                'category': event.category,
                'action': event.action,
                'user_name': event.user_name,
                'item_name': event.item_name,
                'provider_ids': event.provider_ids,
                'ip': event.ip,
                'device_name': event.device_name,
            }

    def upload(self):
        if not self.payload:
            return
        client = pymongo.MongoClient(self.connect_url)
        db = client.Emby
        collection = db.webhook_event
        collection.insert_one(self.payload)
        client.close()
