import pymongo

import settings


def upload_to_mongo(event):
    # Create payload
    payload = None

    # Playback
    if event.category == 'playback':
        payload = {
            'category': event.category,
            'action': event.action,
            'user_name': event.user_name,
            'item_name': event.item_name,
            'provider_ids': event.provider_ids,
            'ip': event.ip,
            'device_name': event.device_name,
        }

    if not payload:
        return

    # Upload
    client = pymongo.MongoClient(settings.MONGO_CONNECT_URL)
    db = client.Emby
    collection = db.webhook_event
    collection.insert_one(payload)
    client.close()
