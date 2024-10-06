import requests
import datetime
import os
from get_image import get_image

PAGE_ID = os.getenv("FACEBOOK_PAGE_ID")
ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")
CAPTION = 'Its a wonderful world!'

def upload_insta():
    media_url = f"https://graph.facebook.com/v21.0/{PAGE_ID}/media"
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    img_path = "https://raw.githubusercontent.com/kshitij-halankar/InstaQuotes/refs/heads/master/InstaQuotes/images/" + current_date + ".png"
    print(img_path)
    media_payload = {
        'image_url': img_path,
        'captoin': CAPTION,
        'access_token': ACCESS_TOKEN
    }
    media_response = requests.post(media_url, data=media_payload)
    media_result = media_response.json()

    if 'id' in media_result:
        media_id = media_result['id']

        publish_url = f"https://graph.facebook.com/v21.0/{PAGE_ID}/media_publish"
        publish_payload = {
            'creation_id': media_id,
            'access_token': ACCESS_TOKEN
        }
        publish_response = requests.post(publish_url, data=publish_payload)
        publish_result = publish_response.json()
        print(publish_result)

get_image()
upload_insta()